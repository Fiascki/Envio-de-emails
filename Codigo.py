
# Esse código tem como objetivo atomatizar um envio de emails, e tendo como horário programado o seu envio, caso seja necessário.

import time as ti
import pyautogui
import schedule
import pyperclip
import os

# Pergunta a ação para o PC
acao_pc = input("O que deseja fazer após o envio? (desligar/reiniciar/nao): ").strip().lower()

print("O código foi iniciado.")

def main():
    # Abrir menu iniciar
    ti.sleep(5)
    pyautogui.click(x=55, y=747)
    ti.sleep(1)

    # Abrir navegador
    pyautogui.click(x=86, y=719)
    texto1 = "Google Chrome"
    pyperclip.copy(texto1)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("enter")

    # Escolher conta (se necessário)
    ti.sleep(2)
    pyautogui.click(x=767, y=365)

    # Ir para o Gmail
    ti.sleep(1)
    pyautogui.click(x=259, y=63)
    texto2 = "www.gmail.com"
    pyperclip.copy(texto2)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("enter")

    # Novo email
    ti.sleep(7)
    pyautogui.click(x=33, y=181)
    ti.sleep(1)

    # Destinatário
    destinatario = "mfiaschi36@gmail.com"
    pyperclip.copy(destinatario)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("tab")

    # Assunto
    assunto = "Link do site da Nike."
    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)
    pyautogui.press("tab")

    # Corpo do email
    corpo = (
        "https://www.nike.com.br/?utm_source=google&utm_medium=cpc&utm_campaign=Google_Search_NIKE-INST-"
        "ROAS&gad_source=1&gad_campaignid=17563577644&gbraid=0AAAAADob9lN8PmZNcnBtCiIxIHjxLeDjO&gclid=CjwKCAjwt-"
        "_FBhBzEiwA7QEqyJf6WP73BjvA0ff_gfrk2olkviz6tYwa_X65Tb64U8lOmhM-"
        "zLmEwBoC7lEQAvD_BwE&utm_referrer=https://www.google.com/"
    )
    pyperclip.copy(corpo)
    pyautogui.hotkey("ctrl", "v")
    ti.sleep(1)

    # Enviar
    pyautogui.click(x=837, y=701)

    # Só aqui, depois de enviar, que faz a ação no PC
    if acao_pc == "desligar":
        os.system("shutdown /s /t 10")
    elif acao_pc == "reiniciar":
        os.system("shutdown /r /t 10")
    else:
        print("O computador permanecerá ligado.")

# Pergunta se é envio imediato ou agendado
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

