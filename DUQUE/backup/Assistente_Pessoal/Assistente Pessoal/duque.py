import speech_recognition as sr
import requests
import json
import pyautogui as pg
from time import sleep
import tkinter as tk

#TKINTER

def fechar_janela():
    janela.destroy()

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
digitarChat.place(x = 10, y = 420, width=220, height=20)


janela.mainloop()