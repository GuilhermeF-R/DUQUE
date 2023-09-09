from tkinter import*
import speech_recognition as sr
import requests
import json
import pyautogui as pg
from time import sleep

#API do ChatGPT

API_KEY_CHATGPT = "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"
headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"


def telaPrincipal():

    def clima():
        janelaPrincipal.destroy()
        
        clima=Tk()
        clima.geometry("300x500")   
        clima.title("DUQUEclima")
        clima.config(bg="#242424")

        iconClima = PhotoImage(file=r"clima\clima.png")
        imageClima = Label(clima, width=0, height=0)
        imageClima.place (x=0, y=0)
        imageClima.config(image=iconClima, highlightthickness=0, bd=0)
        
        abrirclima= Button(clima, text="Abrir site", width=20, height=1, background="#242424", foreground="cyan")
        abrirclima.place (x=80, y=310)

        def backClima():
            clima.destroy()
            telaPrincipal()

        voltar= Button(clima, text="voltar", width=10, height=1, background="#242424", foreground="cyan", command=backClima)
        voltar.place (x=200, y=10)

        #RESOLUÇÃO
        buttonfantasma = Button(janelaPrincipal, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)


    janelaPrincipal = Tk()

    janelaPrincipal.geometry("300x500")   
    janelaPrincipal.title("DUQUE")
    janelaPrincipal.config(bg="#242424")

    olauser = Label(janelaPrincipal, text="Olá!", background="#242424", foreground="white", anchor=W)
    olauser.place (x=20, y=40, width=100,height=20)

    iconVoice= PhotoImage(file=r"icons principais/voice.png")
    buttonVoice= Button(janelaPrincipal, width=0, height=0)
    buttonVoice.place(x=250, y=65)
    buttonVoice.config(image=iconVoice, highlightthickness=0, bd=0)

    iconSearch=PhotoImage(file=r"icons principais/barradepesquisa.png")
    iconSearch= Label(janelaPrincipal, image=iconSearch).place(x=5, y=72, width=290, height=20)
    search=Entry(janelaPrincipal)
    search.place(x=20, y=72,width=232,height=20)

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
        
        abrirdnews= Button(Dnews, text="Abrir site", width=20, height=1, background="gray", foreground="white")
        abrirdnews.place (x=80, y=450)

        def backDaily():
            Dnews.destroy()
            telaPrincipal()

        voltar= Button(Dnews, text="voltar", width=10, height=1, background="DodgerBlue", foreground="white", command=backDaily)
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
        

        def send_message():
            import tkinter as tk
            
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

        janelaPrincipal.destroy()

        janelaChat=Tk()
        janelaChat.geometry("300x500")   
        janelaChat.title("DUQUEchat")
        janelaChat.config(bg="#242424")

        iconTextoButtons = PhotoImage(file="./imagens/chatImagens/textoButtons.png")
        textoButtons = Label(janelaChat, width=0, height=0)
        textoButtons.place (x=0, y=410)
        textoButtons.config(image=iconTextoButtons, highlightthickness=0, bd=0)

        #Icone de Audio
        iconAudio = PhotoImage(file="./imagens/chatImagens/chatButtonAudio.png")
        buttonAudio = Button(janelaChat, width=0, height=0)
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

        digitarChat = Entry(janelaChat)
        digitarChat.place(x=10, y=420, width=220, height=20)

        enviarButton = Button(janelaChat, text="Enviar", command=send_message)
        enviarButton.place(x=240, y=420, width=50, height=20)

        chat_display = Text(janelaChat, wrap=WORD)
        chat_display.place(x=40, y=80, width=220, height=300)
        chat_display.config(state=DISABLED)

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
        news.config(bg="#242424")

    icon_news= PhotoImage(file=r"icons principais/news.png")
    bnews = Button(janelaPrincipal, width=0, height=0,command=news)
    bnews.place (x=50, y=445)
    bnews.config(image=icon_news, highlightthickness=0, bd=0)

    def financas():
        janelaPrincipal.destroy()
        financas=Tk()
        financas.geometry("300x500")   
        financas.title("DUQUEfinancas")
        financas.config(bg="#242424")

    icon_financas= PhotoImage(file=r"icons principais/financas.png")
    bfinancas = Button(janelaPrincipal, width=0, height=0, command=financas)
    bfinancas.place (x=210, y=445)
    bfinancas.config(image=icon_financas, highlightthickness=0, bd=0)

    def perfil():
        janelaPrincipal.destroy()
        perfil=Tk()
        perfil.geometry("300x500")   
        perfil.title("DUQUEacount")
        perfil.config(bg="#242424")

        #perfil

        iconProfile = PhotoImage(file=r"icons principais/chatButtonPerfil.png")
        buttonProfile = Button(perfil, width=0, height=0)
        buttonProfile.place (x=40, y=40)#
        buttonProfile.config(image=iconProfile, highlightthickness=0, bd=0)
    
        #botãos

        buttonnot = Button(perfil,text="Notificação",foreground="white", width=20, height=1) # font="arial black")#command=)    
        buttonnot.place (x=80, y=200)
        buttonnot.config(background="#242424", highlightthickness=0, bd=0)

        
        buttonconfig = Button(perfil,text="Configuração",foreground="white", width=20, height=1 ,)#command=)
        buttonconfig.place (x=80, y=230)
        buttonconfig.config(background="#242424", highlightthickness=0, bd=0)

        
        buttonhelp = Button(perfil,text="Ajuda", foreground="white", width=20, height=1 ,)#command=)
        buttonhelp.place (x=80, y=260)
        buttonhelp.config(background="#242424", highlightthickness=0, bd=0)
        

        buttonsobre = Button(perfil, text="Sobre", foreground="white", width=20, height=1 ,)#command=)
        buttonsobre.place (x=80, y=290)
        buttonsobre.config(background="#242424", highlightthickness=0, bd=0)

        #logar
        def logar():
            perfil.destroy()
            login=Tk()
            login.geometry("300x500")   
            login.title("DUQUElogin")
            login.config(bg="#242424")

            def criar_conta():
                
                login.destroy()
                criar=Tk()
                criar.geometry("300x500")   
                criar.title("DUQUEcriando-conta")
                criar.config(bg="#242424")

                def enviarConta():
                    emailResgatar = emailEntry.get()
                    senhaResgatar = senha.get()
                    with open("usuarios.txt", "a") as arquivo:
                        arquivo.write(f"{emailResgatar}:{senhaResgatar}\n")
                    print("Conta criada com sucesso!")



                enviar= Button(criar,  width=10, height=1, command=enviarConta)
                enviar.config(text="ENVIAR", background="black", foreground="white")
                enviar.place(x=120,y=180)
            

                emailmsg = Label(criar, text="email", background="#242424", foreground="white", anchor=W)
                emailmsg.place (x=40, y=60, width=100,height=20)
                emailEntry=Entry(criar)
                emailEntry.place(x=40, y=80,width=232,height=20)

                    

                senhamsg = Label(criar, text="senha", background="#242424", foreground="white", anchor=W)
                senhamsg.place (x=40, y=100, width=100,height=20)
                senha=Entry(criar)
                senha.place(x=40, y=120,width=232,height=20)
                

            criarconta= Button(login, text="criar conta", width=20, height=1, command=criar_conta)
            criarconta.place (x=80, y=190)

            def entrarConta():

                login.destroy()
                entrada=Tk()
                entrada.geometry("300x500")
                entrada.title("DUQUEentrar-conta")
                entrada.config(bg="#242424")

                def backLogin():
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

                emailtext = Label(entrada, text="email", background="#242424", foreground="white", anchor=W)
                emailtext.place (x=40, y=60, width=100,height=20)
                emaillogin=Entry(entrada)
                emaillogin.place(x=40, y=80,width=232,height=20)

                senhatext = Label(entrada, text="senha", background="#242424", foreground="white", anchor=W)
                senhatext.place (x=40, y=100, width=100,height=20)
                senhalogin=Entry(entrada)
                senhalogin.place(x=40, y=120,width=232,height=20)

                enviar= Button(entrada,  width=10, height=1, command=fazer_login)
                enviar.config(text="ENVIAR", background="black", foreground="white")
                enviar.place(x=120,y=180)

            entrar= Button(login, text="entrar na conta", width=20, height=1, command=entrarConta)
            entrar.place (x=80, y=220)

            voltar= Button(login, text="voltar", width=20, height=1)
            voltar.config(command=voltar)
            voltar.place (x=80, y=250)

            

        buttonlogin = Button(perfil, text="Fazer Login", foreground="white", width=20, height=1)
        buttonlogin.place (x=80, y=320)
        buttonlogin.config(background="#242424", highlightthickness=0, bd=0,  command=logar)

        buttonsair = Button(perfil,text="Sair", foreground="white", width=20, height=1)#command=)
        buttonsair.place (x=80, y=350)
        buttonsair.config(background="#242424", highlightthickness=0, bd=0)

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



