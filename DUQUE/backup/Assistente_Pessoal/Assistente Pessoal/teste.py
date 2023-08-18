#importar reconhecimento
import speech_recognition as sr
#importar requisição
import requests
#importar conversor 
import json
#importar pyautogui
import pyautogui as pg
from time import sleep
#import tkinter
import tkinter as tk

#senha da requisição
API_KEY_CLIMA = "8c9039450a923249dbc52102b855616d"
API_KEY_CHATGPT = "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"

headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"


body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "Quem é Michael Jackson"}]
}

body_mensagem = json.dumps(body_mensagem)


requisicao = requests.post(link, headers=headers, data=body_mensagem)
#print(requisicao)
resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)


#USANDO A API DO CLIMA
cidade = "Rio de janeiro"
link_clima = f"https://api.openweathermap.org/data/3.0/onecall?q={cidade}&appid={API_KEY_CLIMA}"
requisicao_clima = requests.get(link_clima)
print(requisicao_clima)
"""


"""









def enviar_Mensagem_Wpp(): 
    #Abrir Zap no Chrome
    pg.press('win')
    sleep(0.8)
    pg.write('brave')
    sleep(1)
    pg.press('enter')
    sleep(2)
    pg.write('https://web.whatsapp.com/')
    sleep(1)
    pg.press('enter')
    sleep(9)

def procurar_contato():
    #Entrar na conversa e enviar o número
    #for c in numeros:
    sleep(1)
    pg.click(x = 218, y = 199)
    sleep(0.5)
    pg.write(nome_contato)
    sleep(1)
    pg.click(x = 234, y = 331)
    sleep(1.5)
# Cria um objeto de reconhecimento de fala
reconhecimento = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo...")
    # Ajusta o ruído de fundo para melhor captura de áudio
    reconhecimento.adjust_for_ambient_noise(source)
    # Captura o áudio do microfone
    audio = reconhecimento.listen(source)

try:
    print("Reconhecendo...")
    # Utiliza o Google Web Speech API para reconhecimento do áudio em texto
    texto = reconhecimento.recognize_google(audio, language='pt-BR').lower()
    print(f"Você disse: '{texto}'")
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print(f"Erro ao fazer a requisição ao serviço de reconhecimento: {e}")

if texto == "enviar mensagem no whatsapp":
    enviar_Mensagem_Wpp()
    sleep(1)
    with sr.Microphone() as source:
        print("Qual o contato que deseja enviar?")
        # Ajusta o ruído de fundo para melhor captura de áudio
        reconhecimento.adjust_for_ambient_noise(source)
        # Captura o áudio do microfone
        audio = reconhecimento.listen(source)

    try:
        print("Reconhecendo...")
        # Utiliza o Google Web Speech API para reconhecimento do áudio em texto
        nome_contato = reconhecimento.recognize_google(audio, language='pt-BR')
        print(f"Você disse: '{texto}'")
        procurar_contato()
    
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao fazer a requisição ao serviço de reconhecimento: {e}")
