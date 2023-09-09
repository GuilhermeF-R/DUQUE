from tkinter import*
import speech_recognition as sr
import requests
import json
import pyautogui as pg
from time import sleep
import webbrowser

#API do ChatGPT

API_KEY_CHATGPT = "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"
headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def telaPrincipal():
    janelaPrincipal = Tk()

    janelaPrincipal.geometry("300x500")
    janelaPrincipal.title("DUQUE")
    janelaPrincipal.config(bg="#242424")


    iconClima = PhotoImage(file=r"clima\clima.png")
    imageClima = Label(janelaPrincipal, width=0, height=0)
    imageClima.place (x=0, y=0)
    imageClima.config(image=iconClima, highlightthickness=0, bd=0)
    
    def abrirClima():
        webbrowser.open(url='https://openweathermap.org/')

    abrirclima= Button(janelaPrincipal, text="Abrir site", width=20, height=1, background="#242424", foreground="cyan")
    abrirclima.place (x=80, y=310)
    abrirclima.config(command=abrirClima)
    

    voltar= Button(janelaPrincipal, text="voltar", width=10, height=1, background="#242424", foreground="cyan",) #command=backClima)
    voltar.place (x=200, y=10)
    

    janelaPrincipal.mainloop()

telaPrincipal()
