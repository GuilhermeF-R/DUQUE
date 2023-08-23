import speech_recognition as sr
import requests
import json
import pyautogui as pg
from time import sleep
import tkinter as tk

API_KEY_CHATGPT = "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"
#TKINTER

headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def fechar_janela():
    janela.destroy()

def send_message():

    loop = 1

    while loop == 1:

        message = digitarChat.get()

        body_mensagem = {
            "model": id_modelo,
            "messages": [{"role": "user", "content": f"{message}"}]
        }

        body_mensagem = json.dumps(body_mensagem)

        requisicao = requests.post(link, headers=headers, data=body_mensagem)
        #print(requisicao)
        resposta = requisicao.json()
        mensagem = resposta["choices"][0]["message"]["content"]
        
        if message:
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, "Você: " + message + "\n")
            chat_display.insert(tk.END, "ChatGPT: " + mensagem + "\n")
            chat_display.config(state=tk.DISABLED)
            digitarChat.delete(0, tk.END)

            bot_display.config()



janela = tk.Tk()
janela.title ("Testando programa")
janela.geometry("300x500")

#BG de fundo
imagem = tk.PhotoImage(file= "./imagens/chatImagens/fundo.png")

#Tela de Fundo
tela_fundo = tk.Label(janela, image = imagem)
tela_fundo.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#Icone Perfil
iconProfile = tk.PhotoImage(file="./imagens/chatImagens/chatButtonPerfil.png")
buttonProfile = tk.Button(janela, width=0, height=0)
buttonProfile.place (x=240, y=20)
buttonProfile.config(image=iconProfile, highlightthickness=0, bd=0)

#Icone de Voltar
iconBack = tk.PhotoImage(file="./imagens/chatImagens/voltar.png")
buttonBack = tk.Button(janela, width=0, height=0)
buttonBack.place (x=10, y=15)
buttonBack.config(image=iconBack, highlightthickness=0, bd=0)

#Icone do texto lá em baixo
iconTextoButtons = tk.PhotoImage(file="./imagens/chatImagens/textoButtons.png")
textoButtons = tk.Label(janela, width=0, height=0)
textoButtons.place (x=0, y=410)
textoButtons.config(image=iconTextoButtons, highlightthickness=0, bd=0)

#Icone de Audio
iconAudio = tk.PhotoImage(file="./imagens/chatImagens/chatButtonAudio.png")
buttonAudio = tk.Button(janela, width=0, height=0)
buttonAudio.place (x=250, y=400)
buttonAudio.config(image=iconAudio, highlightthickness=0, bd=0)

#Icone de Explorar
iconExplore = tk.PhotoImage(file="./imagens/chatImagens/chatButtonExplore.png")
buttonExplore = tk.Button(janela, width=0, height=0)
buttonExplore.place (x=40, y=445)
buttonExplore.config(image=iconExplore, highlightthickness=0, bd=0)

#Icone do Histórico
iconHistoric = tk.PhotoImage(file="./imagens/chatImagens/chatButtonHistoric.png")
buttonHistoric = tk.Button(janela, width=0, height=0)
buttonHistoric.place (x=210, y=445)
buttonHistoric.config(image=iconHistoric, highlightthickness=0, bd=0)

digitarChat = tk.Entry(janela)
digitarChat.place(x=10, y=420, width=220, height=20)

enviarButton = tk.Button(janela, text="Enviar", command=send_message)
enviarButton.place(x=240, y=420, width=50, height=20)

chat_display = tk.Text(janela, wrap=tk.WORD)
chat_display.place(x=40, y=80, width=220, height=300)
chat_display.config(state=tk.DISABLED)



janela.mainloop()