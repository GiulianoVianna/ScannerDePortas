import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class VerificadorDePortas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        self.setWindowTitle('Scanner de Portas')

    def inicializar_ui(self):
        self.layout = QVBoxLayout()

        # Rótulo e entrada para o endereço IP do host
        self.rotulo_host = QLabel('Host (endereço IP):')
        self.layout.addWidget(self.rotulo_host)

        self.entrada_host = QLineEdit()
        self.layout.addWidget(self.entrada_host)

        # Rótulo e entrada para o intervalo de portas
        self.rotulo_intervalo_portas = QLabel('Intervalo de Portas (ex: 1-1024):')
        self.layout.addWidget(self.rotulo_intervalo_portas)

        self.entrada_intervalo_portas = QLineEdit()
        self.layout.addWidget(self.entrada_intervalo_portas)

        # Botão para iniciar a verificação das portas
        self.botao_verificar = QPushButton('Verificar Portas')
        self.botao_verificar.clicked.connect(self.verificar_portas)
        self.layout.addWidget(self.botao_verificar)

        # Campo de texto para exibir os resultados da verificação
        self.texto_resultados = QTextEdit()
        self.layout.addWidget(self.texto_resultados)

        self.setLayout(self.layout)

    # Função chamada ao clicar no botão "Verificar Portas"
    def verificar_portas(self):
        host = self.entrada_host.text()
        intervalo_portas = self.entrada_intervalo_portas.text()

        if not host or not intervalo_portas:
            self.texto_resultados.setPlainText("Por favor, insira o host e o intervalo de portas.")
            return

        try:
            porta_inicial, porta_final = [int(porta) for porta in intervalo_portas.split('-')]
        except ValueError:
            self.texto_resultados.setPlainText("Formato de intervalo de portas inválido. Use 'inicial-final'.")
            return

        resultados = self.realizar_verificacao(host, porta_inicial, porta_final)
        self.exibir_resultados(resultados)

    # Função para realizar a verificação das portas
    def realizar_verificacao(self, host, porta_inicial, porta_final):
        resultados = []
        for porta in range(porta_inicial, porta_final + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, porta))
            if resultado == 0:
                resultados.append((porta, 'aberta'))
            else:
                resultados.append((porta, 'fechada'))
            sock.close()
        return resultados

    # Função para exibir os resultados da verificação no campo de texto
    def exibir_resultados(self, resultados):
        texto_resultados = ""
        for porta, status in resultados:
            texto_resultados += f"Porta {porta}: {status}\n"
        self.texto_resultados.setPlainText(texto_resultados)

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    janela = VerificadorDePortas()
    janela.show()
    janela.setFixedSize(250, 350)
    sys.exit(aplicacao.exec_())
