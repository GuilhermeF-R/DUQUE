#interface iniciaL DO PROGRAMA DUQUE
from tkinter import*
root=Tk()


#especificaçâo de interface #background
root.geometry("300x500")   
root.title("DUQUE")
root.config(bg="#242424")

#botões principais


#ola usuario-------------------------------------------------------

#anchor=> N=Norte, S=Sul, L=Leste, W=Oeste
#NE=Noroeste, SE=Sudeste, etc.
olauser = Label(root, text="Seja bem-vindo", background="#242424", foreground="white", anchor=W)
olauser.place (x=20, y=40, width=100,height=20)

#barra de pesquisa-------------------------------------------------------

iconSearch=PhotoImage(file=r"icons principais/barradepesquisa.png")
iconSearch= Label(root, image=iconSearch).place(x=5, y=72, width=290, height=20)
search=Entry(root).place(x=20, y=72,width=232,height=20)

#voice-------------------------------------------------------

iconVoice= PhotoImage(file=r"icons principais/voice.png")
buttonVoice= Button(root,width=0, height=0)
buttonVoice.place(x=250, y=65)
buttonVoice.config(image=iconVoice, highlightthickness=0, bd=0)


#botões variaveis

#clima-------------------------------------------------------

#abrir clima
#def clima():
    

icon_clima= PhotoImage(file=r"icons variaveis/clima.png")
bclima = Button(root, width=0, height=0,)#command=clima)
bclima.place (x=50, y=350)
bclima.config(image=icon_clima, highlightthickness=0, bd=0)


#noticia do dia-------------------------------------------------------

#abrir noticia
#def dailyNews():
    
    

icon_dailyNews= PhotoImage(file=r"icons variaveis/dailynews.png")
dailyNews = Button(root, width=0, height=0, )#command=dailyNews)
dailyNews.place (x=150, y=350)
dailyNews.config(image=icon_dailyNews, highlightthickness=0, bd=0)


#abrir chat-------------------------------------------------------

def chat():
    root.destroy()
    chat=Tk()
    chat.geometry("300x500")   
    chat.title("DUQUEchat")
    chat.config(bg="#242424")

#chat
icon_chat= PhotoImage(file=r"icons principais/chat.png")
bchat = Button(root, width=0, height=0, command= chat)
bchat.place (x=130, y=445)
bchat.config(image=icon_chat, highlightthickness=0, bd=0)

#abrir noticias--------------------------------------------------------

def news():
    root.destroy()
    news=Tk()
    news.geometry("300x500")   
    news.title("DUQUEnews")
    news.config(bg="#242424")

#noticias

icon_news= PhotoImage(file=r"icons principais/news.png")
bnews = Button(root, width=0, height=0,command=news)
bnews.place (x=50, y=445)
bnews.config(image=icon_news, highlightthickness=0, bd=0)

#abrir financas-------------------------------------------------------

def financas():
    root.destroy()
    financas=Tk()
    financas.geometry("300x500")   
    financas.title("DUQUEfinancas")
    financas.config(bg="#242424")

#finanças
icon_financas= PhotoImage(file=r"icons principais/financas.png")
bfinancas = Button(root, width=0, height=0, command=financas)
bfinancas.place (x=210, y=445)
bfinancas.config(image=icon_financas, highlightthickness=0, bd=0)

#perfil-------------------------------------------------------

#abrir perfil
def perfil():
    root.destroy()
    perfil=Tk()
    perfil.geometry("300x500")   
    perfil.title("DUQUEacount")
    perfil.config(bg="#242424")


    buttonnot = Button(perfil, width=20, height=1 ,)#command=)
    buttonnot.place (x=50, y=80)
    buttonnot.config(background="#242424", highlightthickness=0, bd=0)
    notifica= Label(perfil, text="notificação", background="white", foreground="black", anchor=W)
    notifica.place(x=100,y=80)

    
    buttonconfig = Button(perfil, width=20, height=1 ,)#command=)
    buttonconfig.place (x=50, y=110)
    buttonconfig.config(background="#242424", highlightthickness=0, bd=0)
    config= Label(perfil, text="configuração", background="white", foreground="black", anchor=W)
    config.place(x=100,y=110)

    
    buttonhelp = Button(perfil, width=20, height=1 ,)#command=)
    buttonhelp.place (x=50, y=140)
    buttonhelp.config(background="#242424", highlightthickness=0, bd=0)
    helpp= Label(perfil, text="ajuda", background="white", foreground="black", anchor=W)
    helpp.place(x=100,y=140)

    
    buttonnot = Button(perfil, width=20, height=1 ,)#command=)
    buttonnot.place (x=50, y=170)
    buttonnot.config(background="#242424", highlightthickness=0, bd=0)
    notifica= Label(perfil, text="notificação", background="white", foreground="black", anchor=W)
    notifica.place(x=100,y=170)

    buttonsobre = Button(perfil, width=20, height=1 ,)#command=)
    buttonsobre.place (x=50, y=200)
    buttonsobre.config(background="#242424", highlightthickness=0, bd=0)
    sobre= Label(perfil, text="sobre", background="white", foreground="black", anchor=W)
    sobre.place(x=100,y=200)

    def logar():
        perfil.destroy()
        login=Tk()
        login.geometry("300x500")   
        login.title("DUQUElogin")
        login.config(bg="#242424")

    buttonlogin = Button(perfil, width=20, height=1)
    buttonlogin.place (x=50, y=230)
    login= Label(perfil, text="fazer login", background="white", foreground="black", anchor=W).place(x=100,y=230)
    buttonlogin.config(background="#242424", highlightthickness=0, bd=0,  command=logar)

    buttonsair = Button(perfil, width=20, height=1 ,)#command=)
    buttonsair.place (x=50, y=260)
    buttonsair.config(background="#242424", highlightthickness=0, bd=0)
    sair= Label(perfil, text="sair", background="white", foreground="black", anchor=W)
    sair.place(x=100,y=260)

  
iconProfile = PhotoImage(file=r"icons principais/chatButtonPerfil.png")
buttonProfile = Button(root, width=0, height=0,command= perfil)
buttonProfile.place (x=240, y=20)
buttonProfile.config(image=iconProfile, highlightthickness=0, bd=0)






root.mainloop()