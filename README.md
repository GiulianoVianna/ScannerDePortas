# Scanner de Portas
Ferramenta para escanear portas 

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="100" heigth="100"  />  

## Definição da Aplicação
A ferramenta "Scanner de Portas" é uma aplicação gráfica simples desenvolvida em Python usando a biblioteca PyQt5, que permite aos usuários verificar o status das portas (abertas ou fechadas) em um determinado host, utilizando um intervalo de portas específico.

A ferramenta possui uma interface de usuário intuitiva com campos de entrada para o endereço IP do host e um intervalo de portas (por exemplo, 1-1024). Ao clicar no botão "Verificar Portas", a ferramenta tentará estabelecer uma conexão com cada porta no intervalo especificado e determinará se a porta está aberta ou fechada. Os resultados da verificação são exibidos em um campo de texto na interface do usuário, facilitando a visualização e a análise do status das portas.

## Bibliotecas
<ul>
    <li>sys</li>
    <li>socket</li>
    <li>PyQt5.QtWidgets</li>
</ul>

#### Biblioteca que precisa ser instalada:
```bash
pip install PyQt5
```
## Imagem da Aplicação
![image](https://user-images.githubusercontent.com/101942554/229948633-790f13ce-e63b-4c92-bfda-70c201f8b541.png)
![image](https://user-images.githubusercontent.com/101942554/229963445-dda305f2-873e-4b50-b55f-ce5fddf6a799.png)



