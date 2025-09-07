
# Esse código tem como objetivo atomatizar um envio de emails, e tendo como horário programado o seu envio, caso seja necessário.

import time as ti 
import pyautogui
import schedule
import pyperclip
import os 

# Código principal

acao_pc = input("O que deseja fazer após o envio? (desligar/reiniciar/nao): ").strip().lower()


print("O código foi iniciado.")
def main():
    # Ir até o navegador... 
    # Ir até o ícone de pesquisa do meu computador.
    ti.sleep(5)
    pyautogui.click(x=55, y=747)
    ti.sleep(1)
    # Digitar o nevagdor desejado.  
    pyautogui.click(x=86, y=719)
    texto1 = "Google Chrome"
    pyperclip.copy(texto1)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("enter")
    # Entrar na conta desejada (no meu caso, precisei escolher uma conta para logar.)
    ti.sleep(2)
    pyautogui.click(x=767, y=365)
    # Aqui eu entrei na página do meu gmail.
    ti.sleep(1)
    pyautogui.click(x=259, y=63)
    texto2 = "www.gmail.com"
    pyperclip.copy(texto2)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("enter")
    # Aqui eu cliquei para escrever um novo email.
    ti.sleep(7)
    pyautogui.click(x=33, y=181)
    ti.sleep(1)
    # Agora eu vou digitar o email desejado para a pessoa/empresa desejada
    destinatario = "mfiaschi36@gmail.com"
    pyperclip.copy(destinatario)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("tab")
    assunto = "Link do site da Nike."
    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("tab")
    corpo= (
        "https://www.nike.com.br/?utm_source=google&utm_medium=cpc&utm_campaign=Google_Search_NIKE-INST-"
        "ROAS&gad_source=1&gad_campaignid=17563577644&gbraid=0AAAAADob9lN8PmZNcnBtCiIxIHjxLeDjO&gclid=CjwKCAjwt-"
        "_FBhBzEiwA7QEqyJf6WP73BjvA0ff_gfrk2olkviz6tYwa_X65Tb64U8lOmhM-"
        "zLmEwBoC7lEQAvD_BwE&utm_referrer=https://www.google.com/"
    )
    pyperclip.copy(corpo)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    # Agora eu vou clicar para enviar o email.
    pyautogui.click(x=837, y=701)
    


# Determinar a ação escolhida no começo para desligar ou não o PC
if acao_pc == "desligar":
    os.system("shutdown /s /t 5")
elif acao_pc == "reiniciar":
    os.system("shutdown /r /t 5")
else:
    print("O computador permanecerá ligado.")


    # Aqui agora acontece o horário do envio do email. 
opcao = input("Deseja enviar agora ou agendar? (agora/agendar): ").strip().lower()

if opcao == "agora":
    main()

elif opcao == "agendar":
    horario = input("Digite o horário (HH:MM): ").strip()

    schedule.every().day.at(horario).do(main)
    print(f"A automação será executada às {horario}.")

    while True:
        schedule.run_pending()
        ti.sleep(1)

else:
    print("Opção inválida.")
