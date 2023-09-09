from tkinter import *
import speech_recognition as sr
import requests
import json
import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.google.com/search?q=clima+hoje")
tempoAgora = navegador.find_element('xpath', '//*[@id="wob_dc"]')
tempoTexto = tempoAgora.text

navegador.get("https://www.tempo.com/duque-de-caxias.htm")
temperatura = navegador.find_element('xpath', '/html/body/main/span[1]/span/span[1]/span[3]/span/span[1]/section/span[2]/span[2]')
temperaturaTexto = temperatura.text

navegador.quit()

# API do ChatGPT
API_KEY_CHATGPT = "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"
headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def realizar_login(email, senha):
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario, senha_armazenada = linha.strip().split(":")
            if usuario == email and senha == senha_armazenada:
                return True
    return False

def telaPrincipal(cliente_logado=None):
    def clima():

        janelaPrincipal.destroy()
        
        clima=Tk()
        clima.geometry("300x500")   
        clima.title("DUQUEclima")
        clima.config(bg="#242424")

        if tempoTexto == 'Parcialmente nublado':
            iconParcialNub = PhotoImage(file=r"clima/parcialmente nublado.png") 
            imageParcialNub = Label(clima, image=iconParcialNub, bg="#242424", width=70, height=70)
            imageParcialNub.place (x=110, y=180)

        if tempoTexto == 'Nublado':
            iconNub = PhotoImage(file=r"clima/Nublado.png")
            imageNub = Label(clima, image=iconNub, bg="#242424", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Pancadas de chuva' or tempoTexto == 'Chuva fraca':
            iconPancChuva = PhotoImage(file=r"clima/Pancadas de chuva.png")
            imageNub = Label(clima, image=iconPancChuva, bg="#242424", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Pancadas esparsas de chuva':
            iconPossiChuva = PhotoImage(file=r"clima/Possibilidade chuvas.png")
            imageNub = Label(clima, image=iconPossiChuva, bg="#242424", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Céu limpo com poucas nuvens':
            iconPoucasNuvens = PhotoImage(file=r"clima/Poucas nuvens.png")
            imageNub = Label(clima, image=iconPoucasNuvens, bg="#242424", width=70, height=70)
            imageNub.place(x=110, y=180)

        if tempoTexto == 'Sol':
            iconSol = PhotoImage(file=r"clima/Sol.png")
            imageNub = Label(clima, image=iconSol, bg="#242424", width=70, height=70)
            imageNub.place(x=110, y=180)

        
        #iconClima = PhotoImage(file=r"tela inicial/fundovazio.png")
        #imageClima = Label(clima, width=0, height=0)
        #imageClima.place (x=0, y=0)
        #imageClima.config(image=iconClima, highlightthickness=0, bd=0)
        
        def abrirClima():
            webbrowser.open(url='https://openweathermap.org/')
       
        abrirclima= Button(clima, text="Abrir site", width=20, height=1, background="#203545", foreground="white",font="arial")
        abrirclima.place (x=60, y=310)
        abrirclima.config(command=abrirClima)

        def backClima():
            clima.destroy()
            telaPrincipal()

        voltar= Button(clima, text="voltar", width=10, height=1, background="#242424", foreground="white", command=backClima)
        voltar.place (x=200, y=10)

        temperaturaLabel = Label(clima, text=f"{temperaturaTexto}C", bg="#242424", fg="white", font=("Helvetica", 28))
        temperaturaLabel.place(x=103, y=130)

        tempoAgoraLabel = Label(clima, text=f"{tempoTexto}", bg="#242424", fg="white", font=("Helbetica", 12))
        tempoAgoraLabel.place(x=60, y=260)


        #RESOLUÇÃO
        buttonfantasma = Button(janelaPrincipal, width=20, height=1 , font="arial black")
        buttonfantasma.place (x=80, y=400)
        buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)


    # Resto do código da função telaPrincipal
    janelaPrincipal = Tk()

    janelaPrincipal.geometry("300x500")   
    janelaPrincipal.title("DUQUE")
    img = PhotoImage (file=r"tela inicial\fundo.png")
    Label(janelaPrincipal, image=img).pack()

    # Se o cliente estiver logado, mostre seu nome
    olauser = Label(janelaPrincipal, text="Olá" + f" {cliente_logado}" + "!", background="#242424", foreground="white", anchor=W)
    olauser.place(x=20, y=40, width=100, height=20)
    print(cliente_logado)
        


    # Resto do código da função telaPrincipal

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
            webbrowser.open(url='https://www.fundec.rj.gov.br/noticias.php?id=OTUw')

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
        fundochat=PhotoImage(file=r"tela inicial\fundochat.png")
        Label(janelaChat, image=fundochat).pack()
        

        iconTextoButtons = PhotoImage(file="./imagens/chatImagens/textoButtons.png")
        textoButtons = Label(janelaChat, width=0, height=0)
        textoButtons.place (x=0, y=405)
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

        digitarChat = Entry(janelaChat, background="#285070",bd=0, foreground="white")
        digitarChat.place(x=10, y=415, width=170, height=20)

        enviarimg = PhotoImage(file=r"imagens\chatImagens\enviar.png")
        enviarButton = Button(janelaChat, image=enviarimg, command=send_message, bd=0, background="#242424",foreground="white")
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

                def voltarbutton():#aaaaaaaaa0
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

                voltar= Button(criar, text="VOLTAR", width=10, height=1, background="black", foreground="white",font="arial")#aaaaaaaaaaaaaaaaaaa0
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
                                cliente_logado = "Guilherme"
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

                voltar= Button(entrada, text="VOLTAR", width=10, height=1, background="black", foreground="white",font="arial")#aaaaaaaaaaaaaaaaaaa0
                voltar.config(command=voltarbutton)
                voltar.place (x=100, y=220)

                buttonfantasma = Button(entrada, width=20, height=1 , font="arial black")
                buttonfantasma.place (x=80, y=400)
                buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

            entrar= Button(login, text="entrar na conta", width=20, height=1, command=entrarConta, background="#274C6A", foreground="White", bd= 0)
            entrar.place (x=80, y=220)

            def Voltarlogin():#aaaaaaaaaaaaaaa0
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


def login():
    def fazer_login():
        email = email_entry.get()
        senha = senha_entry.get()
        if realizar_login(email, senha):
            telaPrincipal(email)
            janela_login.destroy()
        else:
            messagebox.showerror("Erro de login", "Email ou senha incorretos")

    janela_login = Tk()
    janela_login.geometry("300x200")
    janela_login.title("Login")

    # Elementos da interface de login
    email_label = Label(janela_login, text="Email:")
    email_label.pack()

    email_entry = Entry(janela_login)
    email_entry.pack()

    senha_label = Label(janela_login, text="Senha:")
    senha_label.pack()

    senha_entry = Entry(janela_login, show="*")
    senha_entry.pack()

    login_button = Button(janela_login, text="Login", command=fazer_login)
    login_button.pack()

    voltar_button = Button(janela_login, text="Voltar", command=janela_login.destroy)
    voltar_button.pack()

    janela_login.mainloop()

def abrir_site():
    webbrowser.open(url='https://www.google.com')

if __name__ == "__main__":
    telaPrincipal()
