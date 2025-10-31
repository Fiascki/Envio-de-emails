# 💌 Automação de Envio de E-mails com Python

Este projeto automatiza o envio de e-mails pelo Gmail utilizando a biblioteca PyAutoGUI, além de permitir o agendamento do envio e a execução de ações automáticas no computador (como desligar ou reiniciar após o envio).


## 🚀 Funcionalidades
✅ Envio automático de e-mails pelo Gmail
✅ Agendamento de horário para envio
✅ Escolha da ação do PC após o envio:

💻 Manter ligado

🔁 Reiniciar

⏹️ Desligar

✅ Personalização de destinatário, assunto e corpo do e-mail
✅ Execução 100% automatizada via PyAutoGUI


## 🧰 Tecnologias Utilizadas

Python 3.x

PyAutoGUI

Pyperclip

Schedule

OS (nativo do Python)

Time (nativo do Python)


## ⚙️ Como Funciona

O script pergunta o que fazer após o envio (desligar, reiniciar ou nao).

Pergunta se deseja enviar agora ou agendar.

Caso agendado, o envio ocorrerá automaticamente no horário definido.

Após enviar o e-mail, o computador executará a ação escolhida.


## 📦 Instalação

### Clone este repositório:

git clone https://github.com/Fiascki/automacao-email-python.git

### Acesse a pasta do projeto:

cd automacao-email-python

### Instale as dependências:

pip install pyautogui pyperclip schedule

# ▶️ Como Usar

### Execute o script:

python enviar_email.py

### Siga as instruções no terminal:

Escolha a ação após o envio (desligar, reiniciar ou não fazer nada).

Escolha se quer enviar agora ou agendar.

Caso agendado, informe o horário no formato HH:MM.


## 💡 Importante:

O script simula cliques e digitação com base nas coordenadas da tela.

Se a sua resolução for diferente, talvez seja necessário ajustar os valores de x e y nas funções pyautogui.click().


## ⚠️ Aviso e Aprendizado

Este projeto é apenas para fins educacionais e de aprendizado.
É importante lembrar que essa automação é mais para aprender a ter base em automações no Python.
A biblioteca PyAutoGUI é excelente para aprendizado e uso pessoal, mas possui limitações em ambientes corporativos, onde soluções mais robustas (como Selenium ou Playwright) costumam ser mais adequadas.

Essa automação foi criada para uso pessoal, podendo ser executada em seu desktop ou notebook sem riscos.
Mas te garanto — é muito divertido construir essa automação com PyAutoGUI!
Recomendo essa biblioteca (PyAutoGUI) para iniciar nas automações com Python e entender na prática como a interação com o computador pode ser controlada via código.
Importe também saber que essa autmação não envia arquivos, apenas mensagens de texto.


### 👨‍💻 Autor
Miguel Fiaschi Silva
📧 mfiaschi36@gmail.com


### 💻 GitHub: @Fiascki


### 📘 Projeto criado para estudo de automação com Python + PyAutoGUI


# ⭐ Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias!
Se o projeto te ajudou, não esqueça de deixar uma ⭐ no repositório 😄
