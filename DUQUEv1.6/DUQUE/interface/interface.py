from tkinter import*
import speech_recognition as sr
import requests
import json
import pyautogui as pg
from time import sleep
import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
import pyttsx3
import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

servico = Service(ChromeDriverManager().install())

largura_maxima = 20
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.google.com/search?q=clima+hoje")
tempoAgora = navegador.find_element('xpath', '//*[@id="wob_dc"]')
tempoTexto = tempoAgora.text
temperatura = navegador.find_element('xpath', '//*[@id="wob_tm"]')
temperaturaTexto = temperatura.text
temperaturasimbol = navegador.find_element('xpath', '//*[@id="wob_wc"]/div[1]/div[1]/div/div[2]/span[1]')
simboltemp = temperaturasimbol.text
#Pegando conteudo de notícias

#DESBUGAR PRINT
navegador.get("https://www.gov.br/pt-br/noticias/meio-ambiente-e-clima/2023/08/fundo-amazonia-dinamarca-anuncia-doacao-de-r-110-milhoes")

resgateDesbug = navegador.find_element('xpath', '//*[@id="parent-fieldname-text"]/div/p[2]')
resgateDesbug_texto = resgateDesbug.text

#Voltar aos conteudos
navegador.get("https://www.gov.br/pt-br/noticias/assistencia-social/2023/08/bolsa-familia-ja-destinou-mais-de-r-10-bilhoes-para-criancas-adolescentes-e-gestantes-entre-marco-e-agosto")

# Obtenha o texto do elemento web
resgateTituloNews1_texto = navegador.find_element('xpath', '//*[@id="content"]/article/h1').text

# Divida o texto em três partes
parte1 = resgateTituloNews1_texto[:len(resgateTituloNews1_texto)//3]
parte2 = resgateTituloNews1_texto[len(resgateTituloNews1_texto)//3:2*len(resgateTituloNews1_texto)//3]
parte3 = resgateTituloNews1_texto[2*len(resgateTituloNews1_texto)//3:]

navegador.get("https://agenciagov.ebc.com.br/noticias/202401/publicado-resultado-do-sisu-2024")

resgateTituloNews2_texto = navegador.find_element('xpath', '//*[@id="content"]/section/h1').text

parte4 = resgateTituloNews2_texto[:len(resgateTituloNews2_texto)//3]
parte5 = resgateTituloNews2_texto[len(resgateTituloNews2_texto)//3:2*len(resgateTituloNews2_texto)//3]
parte6 = resgateTituloNews2_texto[2*len(resgateTituloNews2_texto)//3:]



navegador.get("https://www.gov.br/pt-br/noticias/assistencia-social/2023/08/pesquisa-da-fgv-aponta-que-programa-cisternas-melhora-saude-dos-bebes-no-semiarido-brasileiro")

resgateTituloNews3_texto = navegador.find_element('xpath', '//*[@id="content"]/article/h1').text

parte7 = resgateTituloNews3_texto[:len(resgateTituloNews3_texto)//3]
parte8 = resgateTituloNews3_texto[len(resgateTituloNews3_texto)//3:2*len(resgateTituloNews3_texto)//3]
parte9 = resgateTituloNews3_texto[2*len(resgateTituloNews3_texto)//3:]

navegador.quit()

def telaPrincipal():
    def clima():
        janelaPrincipal.destroy()
        
        clima=Tk()
        clima.geometry("300x500")   
        clima.title("DUQUEclima")
        climafundo = PhotoImage(file=r"clima\climafundo.png")
        Label(clima, image=climafundo).pack()

        if tempoTexto == 'Parcialmente nublado':
            iconParcialNub = PhotoImage(file=r"clima/parcialmente nublado.png") 
            imageParcialNub = Label(clima, image=iconParcialNub, bg="#285070", width=70, height=70)
            imageParcialNub.place (x=110, y=180)

        if tempoTexto == 'Nublado':
            iconNub = PhotoImage(file=r"clima/Nublado.png")
            imageNub = Label(clima, image=iconNub, bg="#285070", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Pancadas de chuva' or tempoTexto == 'Chuva fraca':
            iconPancChuva = PhotoImage(file=r"clima/Pancadas de chuva.png")
            imageNub = Label(clima, image=iconPancChuva, bg="#285070", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Pancadas esparsas de chuva' or tempoTexto == 'Tempestade leve de raios e trovões':
            iconPossiChuva = PhotoImage(file=r"clima/Possibilidade chuvas.png")
            imageNub = Label(clima, image=iconPossiChuva, bg="#285070", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Céu limpo com poucas nuvens':
            iconPoucasNuvens = PhotoImage(file=r"clima/Poucas nuvens.png")
            imageNub = Label(clima, image=iconPoucasNuvens, bg="#285070", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Sol' or tempoTexto == 'Céu aberto':
            iconSol = PhotoImage(file=r"clima/Sol.png")
            imageNub = Label(clima, image=iconSol, bg="#285070", width=70, height=70)
            imageNub.place(x=110, y=180)

        
        def abrirClima():
            webbrowser.open(url='https://www.google.com/search?q=clima+hoje')
       
        abrirclima= Button(clima, text="Abrir site", width=15, height=1, background="#203545", foreground="white",font="arial")
        abrirclima.place (x=73, y=310)
        abrirclima.config(command=abrirClima)

        def backClima():
            clima.destroy()
            telaPrincipal()

        voltar= Button(clima, text="voltar", width=6, height=1, background="#234561", foreground="white", command=backClima, bd=0, font="arial")
        voltar.place (x=235, y=2)

        temperaturaLabel = Label(clima, text=f"{temperaturaTexto}{simboltemp}", bg="#285070", fg="white", font=("Helvetica", 28))
        temperaturaLabel.place(x=103, y=130)

        if tempoTexto == 'Sol':
            tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#285070", fg="white", font=("Helbetica", 12))
            tempoAgoraLabel.place(x=130, y=260)

        if tempoTexto == 'Nublado':
            tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#285070", fg="white", font=("Helbetica", 12))
            tempoAgoraLabel.place(x=115, y=260)
        
        if tempoTexto == 'Céu limpo com poucas nuvens' or tempoTexto== 'Pancadas esparsas de chuva':
            tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#285070", fg="white", font=("Helbetica", 12))
            tempoAgoraLabel.place(x=40, y=260)

        if tempoTexto == 'Pancadas de chuva' or tempoTexto=='Parcialmente nublado':
            tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#285070", fg="white", font=("Helbetica", 12))
            tempoAgoraLabel.place(x=70, y=260)

        if tempoTexto == 'Chuva fraca' or tempoTexto == 'Céu aberto':
            tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#285070", fg="white", font=("Helbetica", 12))
            tempoAgoraLabel.place(x=110, y=260)


        #RESOLUÇÃO
        buttonfantasma = Button(janelaPrincipal, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)


    janelaPrincipal = Tk()

    janelaPrincipal.geometry("300x500")   
    janelaPrincipal.title("DUQUE")
    img = PhotoImage (file=r"tela inicial\fundo.png")
    Label(janelaPrincipal, image=img).pack()

   
    olauser = Label(janelaPrincipal, text="Olá!", background="#242424", foreground="white", anchor=W)
    olauser.place(x=20, y=40, width=100, height=20)

    def pesquisar():
        pesquisa = search.get()
        webbrowser.open(url='https://www.google.com/search?q='+pesquisa)

    iconSearch=PhotoImage(file=r"icons principais/barradepesquisa.png")
    iconSearch= Label(janelaPrincipal, image=iconSearch).place(x=5, y=72, width=290, height=20)
    search=Entry(janelaPrincipal)
    search.place(x=20, y=72,width=232,height=20)
    

    iconPesquisa= PhotoImage(file=r"icons principais/setasearch.png")
    buttonPesquisa= Button(janelaPrincipal, width=0, height=0)
    buttonPesquisa.place(x=250, y=65)
    buttonPesquisa.config(image=iconPesquisa, highlightthickness=0, bd=0, command=pesquisar)

    icon_clima= PhotoImage(file=r"iconsVariaveis/clima.png")
    bclima = Button(janelaPrincipal, width=0, height=0, command=clima)
    bclima.place (x=50, y=350)
    bclima.config(image=icon_clima, highlightthickness=0, bd=0)

    def dailyNews():
        janelaPrincipal.destroy()
        Dnews=Tk()
        Dnews.geometry("300x500")   
        Dnews.title("DUQUEDnews")
        Dnews.config(bg="#242424")

        iconDnews = PhotoImage(file=r"news/new.png")
        imageDnews = Label(Dnews, width=0, height=0)
        imageDnews.place (x=0, y=0)
        imageDnews.config(image=iconDnews, highlightthickness=0, bd=0)
        
        def abrirDnews():
            webbrowser.open(url='https://www.fundec.rj.gov.br/noticias.php?id=OTk1')

        abrirdnews= Button(Dnews, text="abrir site", width=20, height=1, background="#284E6C", foreground="white",font="arial")
        abrirdnews.place (x=55, y=450)
        abrirdnews.config(command=abrirDnews)

        def backDaily():
            Dnews.destroy()
            telaPrincipal()

        voltar= Button(Dnews, text="voltar", width=10, height=1, background="#285070", foreground="white", command=backDaily)
        voltar.place (x=10, y=10)

        #RESOLUÇÃO
        buttonfantasma = Button(Dnews, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

    icon_dailyNews= PhotoImage(file=r"iconsVariaveis/dailynews.png")
    dailyNew = Button(janelaPrincipal, width=0, height=0, command=dailyNews)
    dailyNew.place (x=150, y=350)
    dailyNew.config(image=icon_dailyNews, highlightthickness=0, bd=0)

    def chatDuque():
        
        def enviarMensagem_wpp():
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


        def get_current_time():
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            return current_time

        def speak(text):
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()


        def main():
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                print("Diga algo...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

                try:
                    print("Reconhecendo...")
                    command = recognizer.recognize_google(audio, language="pt-BR")
                    print("Comando detectado:", command)
                    process_command(command.lower())

                except sr.UnknownValueError:
                    print("Não foi possível entender o áudio.")
                except sr.RequestError as e:
                    print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

        def process_command(command):
            if "olá" in command:
                speak("Olá! Como posso ajudar?")
                
            elif "como você está" in command:
                speak("Estou bem, obrigada por perguntar!")

            elif "qual é a hora" in command:
                current_time = get_current_time()
                speak(f"Hora atual, {current_time}")
                print(current_time)

            elif "tchau" in command:
                speak("Até logo! Tenha um bom dia.")
                exit()

            elif "você é solteira" in command:
                speak("Não fui criada para esse tipo de coisa.")

            elif "pesquisar" in command:

                recognizer = sr.Recognizer()

                def search_web(query):
                    search_engine = "https://www.google.com/search?q="

                    url = search_engine + query

                    webbrowser.open(url)

                with sr.Microphone() as source:
                    speak("Diga o que você deseja pesquisar na internet.")
                    print('Diga o que você deseja pesquisar na internet.')
                    audio = recognizer.listen(source)

                try:
                    full_query = recognizer.recognize_google(audio, language="pt-BR")
                    print("Você disse: " + full_query)

                    query = full_query.replace("pesquisar", "").strip()

                    search_web(query)
                except sr.UnknownValueError:
                    print("Não foi possível entender o áudio.")
                except sr.RequestError as e:
                    print("Erro no serviço de reconhecimento de voz; {0}".format(e))


            elif "mensagem no whatsapp" in command:
                enviarMensagem_wpp()
                recognizer = sr.Recognizer()

                with sr.Microphone() as source:
                    speak("Para quem quer enviar?")
                    recognizer.adjust_for_ambient_noise(source)
                    audioContato = recognizer.listen(source)

                    try:
                        print("Reconhecendo...")
                        contato_nome = recognizer.recognize_google(audioContato, language="pt-BR")
                        print("Comando detectado:", contato_nome)

                    except sr.UnknownValueError:
                        print("")
                    except sr.RequestError as e:
                        print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

                pg.click(x = 218, y = 199)
                sleep(0.5)
                pg.write(contato_nome)
                sleep(1)
                pg.click(x = 234, y = 331)
                sleep(1.5)

                with sr.Microphone() as source:
                    speak('O que deseja enviar?')
                    recognizer.adjust_for_ambient_noise(source)
                    audioMensagem = recognizer.listen(source)

                    try:
                            print("Reconhecendo...")
                            mensagemContato = recognizer.recognize_google(audioMensagem, language="pt-BR")
                            print("Comando detectado:", mensagemContato)
                            process_command(mensagemContato.lower())

                    except sr.UnknownValueError:
                        print("Não foi possível entender o áudio.")
                    except sr.RequestError as e:
                        print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

                pg.write(mensagemContato)
                sleep(2)
                pg.press('enter')

            else:
                speak("Desculpe, não entendi o comando.")

        janelaPrincipal.destroy()

        janelaChat=Tk()
        janelaChat.geometry("300x500")   
        janelaChat.title("DUQUEchat")
        fundochat=PhotoImage(file=r"tela inicial\fundochat.png")
        Label(janelaChat, image=fundochat).pack()
        

        iconTextoButtons = PhotoImage(file="./imagens/chatImagens/textoButtons.png")
        textoButtons = Label(janelaChat, width=0, height=0)
        textoButtons.place (x=0, y=405)
        textoButtons.config(image=iconTextoButtons, highlightthickness=0, bd=0)

        #Icone de Audio
        iconAudio = PhotoImage(file="./imagens/chatImagens/chatButtonAudio.png")
        buttonAudio = Button(janelaChat, width=0, height=0, command=main)
        buttonAudio.place (x=250, y=400)
        buttonAudio.config(image=iconAudio, highlightthickness=0, bd=0)

        #Icone de Explorar
        iconExplore = PhotoImage(file="./imagens/chatImagens/chatButtonExplore.png")
        buttonExplore = Button(janelaChat, width=0, height=0)
        buttonExplore.place (x=40, y=445)
        buttonExplore.config(image=iconExplore, highlightthickness=0, bd=0)

        #Icone do Histórico
        iconHistoric = PhotoImage(file="./imagens/chatImagens/chatButtonHistoric.png")
        buttonHistoric = Button(janelaChat, width=0, height=0)
        buttonHistoric.place (x=210, y=445)
        buttonHistoric.config(image=iconHistoric, highlightthickness=0, bd=0)

        digitarChat = Entry(janelaChat, background="#285070",bd=0, foreground="white")
        digitarChat.place(x=10, y=415, width=170, height=20)

        enviarimg = PhotoImage(file=r"imagens\chatImagens\enviar.png")
        enviarButton = Button(janelaChat, image=enviarimg,  bd=0, background="#242424",foreground="white")
        enviarButton.place(x=180, y=413, width=50, height=20)

        chat_display = Text(janelaChat, wrap=WORD)
        chat_display.place(x=40, y=80, width=220, height=300)
        chat_display.config(state=DISABLED, background="#284E6D", foreground="white", font="arial")

        def backDuque():
            janelaChat.destroy()
            telaPrincipal()

        iconBack = PhotoImage(file="./imagens/chatImagens/voltar.png")
        buttonBack = Button(janelaChat, width=0, height=0)
        buttonBack.place (x=10, y=15)
        buttonBack.config(image=iconBack, highlightthickness=0, bd=0, command=backDuque)

        buttonfantasma = Button(janelaChat, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)


    icon_chat= PhotoImage(file=r"icons principais/chat.png")
    bchat = Button(janelaPrincipal, width=0, height=0, command= chatDuque)
    bchat.place (x=130, y=445)
    bchat.config(image=icon_chat, highlightthickness=0, bd=0)

    def news():
        janelaPrincipal.destroy()
        news=Tk()
        news.geometry("300x500")   
        news.title("DUQUEnews")
        fundonews = PhotoImage (file=r"news\fundonews.png")
        Label(news, image = fundonews).pack()

        # URL da imagem
        img_url = "https://imgs.search.brave.com/0dsH5a8MV9lxz_OAAlZHD0vD8UHNJaPdnd3fY2e5FvQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTMy/Mzk5OTgyMS9wdC9m/b3RvL2EtNS15ZWFy/LWdpcmwtcGxheWlu/Zy13aXRoLWRhaXNp/ZXMtaW4tYS1maWVs/ZC5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9VjJackNHeUNs/SG1CalJRZjVPV0VO/ZkFzRHVHRmN5dTRf/d1owZ0p3WFVzMD0"
        img2_url = "https://img.freepik.com/fotos-gratis/engracado-feliz-animado-jovem-mulher-bonita-sentada-a-mesa-na-camisa-preta-trabalhando-no-laptop-no-escritorio-de-trabalho-co-usando-oculos_285396-86.jpg?size=626&ext=jpg"
        img3_url = "https://imgs.search.brave.com/StIDZlpIWEfNwu13MNgMZUp7ealCiE5EPiHDHDewW34/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vYmViZS5h/YnJpbC5jb20uYnIv/d3AtY29udGVudC91/cGxvYWRzLzIwMjEv/MDcvZGVzdGFxdWUx/NC5qcGc_cmVzaXpl/PTEzMjQsODg0JnF1/YWxpdHk9OTAmc3Ry/aXA9aW5mbyZzc2w9/MSZ3PTEzNjAmaD05/MDY"

        # Fazer uma solicitação HTTP para obter a imagem
        img_response = requests.get(img_url)
        img2_response = requests.get(img2_url)
        img3_response = requests.get(img3_url)

        if img_response.status_code == 200 and img2_response.status_code == 200 and img3_response.status_code == 200:

            # Carregar a imagem usando a biblioteca Pillow
            img_data = img_response.content 
            img2_data = img2_response.content 
            img3_data = img3_response.content 
            img = Image.open(BytesIO(img_data))
            img2 = Image.open(BytesIO(img2_data))
            img3 = Image.open(BytesIO(img3_data))

            # Aplicar um "zoom" à imagem selecionando uma região ampliada
            zoom_factor = 2  # Ajuste este fator para controlar o zoom
            width, height = img.size
            new_width = width // zoom_factor
            new_height = height // zoom_factor
            left = (width - new_width) // 2
            top = (height - new_height) // 2
            right = (width + new_width) // 2
            bottom = (height + new_height) // 2
            img = img.crop((left, top, right, bottom))
            img2 = img2.crop((left, top, right, bottom))
            img3 = img3.crop((left, top, right, bottom))

            # Redimensionar a imagem para 50x50 pixels
            img = img.resize((76, 79))
            img2 = img2.resize((76, 79))
            img3 = img3.resize((76, 79))

        else:
            print("Falha ao obter a imagem")

        #voltar
        def backnews():
            news.destroy()
            telaPrincipal()

        voltar= Button(news, text="voltar", width=6, height=1, background="#27445C", foreground="white", command=backnews, bd=0, font="arial")
        voltar.place (x=235, y=2)

        #barra de pesquisa
        def pesquisargov():
            pesquisagov = searchgov.get()
            webbrowser.open(url='https://www.gov.br/pt-br/search?SearchableText='+pesquisagov)

        iconSearchgo=PhotoImage(file=r"news\barradepesquisa.png")
        iconSearchgov= Label(news, image=iconSearchgo)
        iconSearchgov.place(x=5, y=43, width=290, height=31)
        searchgov=Entry(news)
        searchgov.place(x=20, y=45,width=232,height=27)

        iconPesquisagov= PhotoImage(file=r"news\setaazul.png")
        botaoPesquisa= Button(news, width=0, height=0)
        botaoPesquisa.place(x=250, y=42)
        botaoPesquisa.config(image=iconPesquisagov, highlightthickness=0, bd=0, command=pesquisargov)

        #botões
        paravoce= PhotoImage(file=r"news\paravoce.png")
        paraVoce = Button(news, width=0, height=0) #command= )
        paraVoce.place (x=15, y=85)
        paraVoce.config(image=paravoce, highlightthickness=0, bd=0)

        noti= PhotoImage(file=r"news\noticias.png")
        noticia = Button(news, width=0, height=0) #command= )
        noticia.place (x=85, y=85)
        noticia.config(image=noti, highlightthickness=0, bd=0)

        evento= PhotoImage(file=r"news\eventos.png")
        eventos = Button(news, width=0, height=0) #command= )
        eventos.place (x=155, y=85)
        eventos.config(image=evento, highlightthickness=0, bd=0)

        destacado= PhotoImage(file=r"news\destaque.png")
        destaque = Button(news, width=0, height=0) #command= )
        destaque.place (x=225, y=85)
        destaque.config(image=destacado, highlightthickness=0, bd=0)

        #notícias

        notiaba= PhotoImage(file=r"news\noticiaaba.png")

        #abrir ao clicar no titulo
        def abriraba01(event):
            webbrowser.open(url='https://www.gov.br/secom/pt-br/assuntos/noticias/2023/08/bolsa-familia-ja-destinou-mais-de-r-10-bilhoes-para-criancas-adolescentes-e-gestantes-entre-marco-e-agosto')
        #abrir ao clicar no titulo
        def abriraba02(event):
            webbrowser.open(url='https://www.fundec.rj.gov.br/noticias.php?id=MTAwNg==')
        #abrir ao clicar no titulo
        def abriraba03(event):
            webbrowser.open(url='https://www.gov.br/pt-br/noticias/assistencia-social/2023/08/pesquisa-da-fgv-aponta-que-programa-cisternas-melhora-saude-dos-bebes-no-semiarido-brasileiro')
#------------------------------------------------------------------------------------------------------------------------------------------#
        #abrir ao clicar na aba
        def abriraba1():
            webbrowser.open(url='https://www.gov.br/secom/pt-br/assuntos/noticias/2023/08/bolsa-familia-ja-destinou-mais-de-r-10-bilhoes-para-criancas-adolescentes-e-gestantes-entre-marco-e-agosto')
        #abrir ao clicar na aba
        def abriraba2():
            webbrowser.open(url='https://www.fundec.rj.gov.br/noticias.php?id=MTAwNg==')
        #abrir ao clicar na aba
        def abriraba3():
            webbrowser.open(url='https://www.gov.br/pt-br/noticias/assistencia-social/2023/08/pesquisa-da-fgv-aponta-que-programa-cisternas-melhora-saude-dos-bebes-no-semiarido-brasileiro')
        
        #aba
        noticiaaba1 = Button(news, width=0, height=0, command= abriraba1)
        noticiaaba1.place (x=10, y=180)
        noticiaaba1.config(image=notiaba, highlightthickness=0, bd=0)

        #imagem
        img = ImageTk.PhotoImage(img)
        noticia1 = Label(news, image=img, bd=0)
        noticia1.place(x=208, y=190)

        #titulo
        tituloNews1_texto = f"{parte1}\n{parte2}\n{parte3}"
        tituloNews1 = Label(news, text=tituloNews1_texto, bg="#4779A2", foreground='white', font=("arial", 8))
        tituloNews1.place(x=12, y=195)
        #abre ao clicar no título
        tituloNews1.bind("<Button-1>", abriraba01)

        #aba
        noticiaaba2 = Button(news, width=0, height=0, command= abriraba2)
        noticiaaba2.place (x=10, y=280)
        noticiaaba2.config(image=notiaba, highlightthickness=0, bd=0)

        #imagem
        img2 = ImageTk.PhotoImage(img2)
        noticia2 = Label(news, image=img2, bd=0)
        noticia2.place(x=208, y=290)

        #titulo
        tituloNews2_texto = f"{parte4}\n{parte5}\n{parte6}"
        tituloNews2 = Label(news, text= tituloNews2_texto, bg="#4779A2",foreground='white', font=("arial", 8))
        tituloNews2.place(x=12, y=295)
        #abre ao clicar no título
        tituloNews2.bind("<Button-1>", abriraba02)

        #aba
        noticiaaba3 = Button(news, width=0, height=0, command= abriraba3 )
        noticiaaba3.place (x=10, y=380)
        noticiaaba3.config(image=notiaba, highlightthickness=0, bd=0)

        #imagem
        img3 = ImageTk.PhotoImage(img3)
        noticia3 = Label(news, image=img3, bd=0)
        noticia3.place(x=208, y=390)

        #titulo
        tituloNews3_texto = f"{parte7}\n{parte8}\n{parte9}"
        tituloNews3 = Label(news, text=tituloNews3_texto, bg="#4779A2",foreground='white', font=("arial", 8))
        tituloNews3.place(x=12, y=395)
        #abre ao clicar no título
        tituloNews3.bind("<Button-1>", abriraba03)

        buttonfantasma = Button(news, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

    icon_news= PhotoImage(file=r"icons principais/news.png")
    bnews = Button(janelaPrincipal, width=0, height=0,command=news)
    bnews.place (x=50, y=445)
    bnews.config(image=icon_news, highlightthickness=0, bd=0)

    def financas():
        janelaPrincipal.destroy()
        financas=Tk()
        financas.geometry("300x500")   
        financas.title("DUQUEfinancas")
        fundofinancas= PhotoImage(file=r"finanças\fundofinanças.png")
        Label(financas, image=fundofinancas).pack()
        
        #voltar
        def backfinancas():
            financas.destroy()
            telaPrincipal()

        voltarf= Button(financas, text="voltar", width=6, height=1, background="#27445C", foreground="white", command=backfinancas, bd=0, font="arial")
        voltarf.place (x=235, y=2)

        buttonfantasma = Button(financas, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

    icon_financas= PhotoImage(file=r"icons principais/financas.png")
    bfinancas = Button(janelaPrincipal, width=0, height=0, command=financas)
    bfinancas.place (x=210, y=445)
    bfinancas.config(image=icon_financas, highlightthickness=0, bd=0)

    def perfil():
        janelaPrincipal.destroy()
        perfil=Tk()
        perfil.geometry("300x500")   
        perfil.title("DUQUEacount")
        fundoperfil= PhotoImage(file=r"tela inicial\fundoperfil.png")
        Label(perfil, image=fundoperfil).pack()

        #perfil

        iconProfile = PhotoImage(file=r"icons principais/chatButtonPerfil.png")
        buttonProfile = Button(perfil, width=0, height=0)
        buttonProfile.place (x=40, y=40)#
        buttonProfile.config(image=iconProfile, highlightthickness=0, bd=0)
    
        #botãos

        buttonnot = Button(perfil,text="Notificação",background="#285070",foreground="white", width=20, height=1) # font="arial black")#command=)    
        buttonnot.place (x=80, y=200)
        buttonnot.config(highlightthickness=0, bd=0)

        
        buttonconfig = Button(perfil,text="Configuração",foreground="white", width=20, height=1 ,)#command=)
        buttonconfig.place (x=80, y=230)
        buttonconfig.config(background="#285070", highlightthickness=0, bd=0)

        
        buttonhelp = Button(perfil,text="Ajuda", foreground="white", width=20, height=1 ,)#command=)
        buttonhelp.place (x=80, y=260)
        buttonhelp.config(background="#285070", highlightthickness=0, bd=0)
        

        buttonsobre = Button(perfil, text="Sobre", foreground="white", width=20, height=1 ,)#command=)
        buttonsobre.place (x=80, y=290)
        buttonsobre.config(background="#285070", highlightthickness=0, bd=0)

        def backD():
            perfil.destroy()
            telaPrincipal()

        iconBack = PhotoImage(file="./imagens/chatImagens/voltar.png")
        buttonBack = Button(perfil, width=0, height=0)
        buttonBack.place (x=220, y=30)
        buttonBack.config(image=iconBack, highlightthickness=0, bd=0, command=backD)


        #logar
        def logar():
            perfil.destroy()
            login=Tk()
            login.geometry("300x500")   
            login.title("DUQUElogin")
            fundologin= PhotoImage(file=r"tela inicial\fundovazio.png")
            Label(login, image=fundologin).pack()
            

            def criar_conta():
                
                login.destroy()
                criar=Tk()
                criar.geometry("300x500")   
                criar.title("DUQUEcriando-conta")
                fundocriar= PhotoImage(file=r"tela inicial\fundovazio.png")
                Label(criar, image=fundocriar).pack()

                def voltarbutton():
                    criar.destroy()
                    telaPrincipal()

                def enviarConta():
                    emailResgatar = emailEntry.get()
                    senhaResgatar = senha.get()
                    with open("usuarios.txt", "a") as arquivo:
                        arquivo.write(f"{emailResgatar}:{senhaResgatar}\n")
                    print("Conta criada com sucesso!")

                criartext = Label(criar, text="Registre uma conta", background="#24292D", foreground="white",font="arial", anchor=W)
                criartext.place (x=80, y=20, width=150,height=20)


                enviar= Button(criar,  width=10, height=1, command=enviarConta)
                enviar.config(text="ENVIAR", background="red", foreground="white", font="arial")
                enviar.place(x=100,y=180)
            

                emailmsg = Label(criar, text="email", background="#25333E", foreground="white", anchor=W)
                emailmsg.place (x=40, y=60, width=100,height=20)
                emailEntry=Entry(criar)
                emailEntry.place(x=40, y=80,width=232,height=20)

                senhamsg = Label(criar, text="senha", background="#25333E", foreground="white", anchor=W)
                senhamsg.place (x=40, y=100, width=100,height=20)
                senha=Entry(criar)
                senha.place(x=40, y=120,width=232,height=20)

                voltar= Button(criar, text="VOLTAR", width=10, height=1, background="black", foreground="white",font="arial")
                voltar.config(command=voltarbutton)
                voltar.place (x=100, y=220)

                buttonfantasma = Button(criar, width=20, height=1 , font="arial black")
                buttonfantasma.place (x=80, y=400)
                buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)
                

            criarconta= Button(login, text="criar conta", width=20, height=1, command=criar_conta, background="#274760", foreground="White", bd= 0)
            criarconta.place (x=80, y=190)

            def entrarConta():

                login.destroy()
                entrada=Tk()
                entrada.geometry("300x500")
                entrada.title("DUQUEentrar-conta")
                fundoconta = PhotoImage(file=r"tela inicial\fundovazio.png")
                Label(entrada, image=fundoconta).pack()

                def backLogin():
                    entrada.destroy()
                    telaPrincipal()

                def voltarbutton():
                    entrada.destroy()
                    telaPrincipal()

                def fazer_login():
                    email = emaillogin.get()
                    password = senhalogin.get() 
                    with open("usuarios.txt", "r") as arquivo:
                        for linha in arquivo:
                            usuario, senha = linha.strip().split(":")
                            if usuario == email and senha == password:
                                backLogin()
                            else:
                                print('ERRO')
                    return False
                
                
                
                entrartext = Label(entrada, text="Conecte-se a sua conta", background="#24292D", foreground="white",font="arial", anchor=W)
                entrartext.place (x=65, y=20, width=170,height=20)

                emailtext = Label(entrada, text="email", background="#25333E", foreground="white", anchor=W)
                emailtext.place (x=40, y=60, width=100,height=20)
                emaillogin=Entry(entrada)
                emaillogin.place(x=40, y=80,width=232,height=20)

                senhatext = Label(entrada, text="senha", background="#25333E", foreground="white", anchor=W)
                senhatext.place (x=40, y=100, width=100,height=20)
                senhalogin=Entry(entrada)
                senhalogin.place(x=40, y=120,width=232,height=20)

                enviar= Button(entrada,  width=10, height=1, command=fazer_login)
                enviar.config(text="ENVIAR", background="red", foreground="white", font="arial")
                enviar.place(x=100,y=180)

                voltar= Button(entrada, text="VOLTAR", width=10, height=1, background="black", foreground="white",font="arial")
                voltar.config(command=voltarbutton)
                voltar.place (x=100, y=220)

                buttonfantasma = Button(entrada, width=20, height=1 , font="arial black")
                buttonfantasma.place (x=80, y=400)
                buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

            entrar= Button(login, text="entrar na conta", width=20, height=1, command=entrarConta, background="#274C6A", foreground="White", bd= 0)
            entrar.place (x=80, y=220)

            def Voltarlogin():
                login.destroy()
                telaPrincipal()


            voltar= Button(login, text="voltar", width=20, height=1, background="#285070", foreground="White", bd= 0)
            voltar.config(command=Voltarlogin)
            voltar.place (x=80, y=250)

            buttonfantasma = Button(login, width=20, height=1 , font="arial black")
            buttonfantasma.place (x=80, y=400)
            buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

        buttonlogin = Button(perfil, text="Fazer Login", foreground="white", width=20, height=1)
        buttonlogin.place (x=80, y=320)
        buttonlogin.config(background="#285070", highlightthickness=0, bd=0,  command=logar)

        buttonsair = Button(perfil,text="Sair", foreground="white", width=20, height=1)#command=)
        buttonsair.place (x=80, y=350)
        buttonsair.config(background="#234560", highlightthickness=0, bd=0)

        #RESOLUÇÃO
        buttonfantasma = Button(perfil, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)
    
    iconProfile = PhotoImage(file=r"icons principais/chatButtonPerfil.png")
    buttonProfile = Button(janelaPrincipal, width=0, height=0,command= perfil)
    buttonProfile.place (x=240, y=20)
    buttonProfile.config(image=iconProfile, highlightthickness=0, bd=0)









    janelaPrincipal.mainloop()
    

telaPrincipal()




