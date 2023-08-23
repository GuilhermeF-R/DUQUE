from tkinter import*
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

    criarconta= Button(login, text="criar conta", width=20, height=1, command=criar_conta)
    criarconta.place (x=80, y=190)

    entrar= Button(login, text="entrar na conta", width=20, height=1)
    entrar.place (x=80, y=220)

    voltar= Button(login, text="voltar", width=20, height=1)
    voltar.config(command=voltar)
    voltar.place (x=80, y=250)
    #email=Entry(login)
    #email.place(x=20, y=10, width=232,height=20,)

buttonlogin = Button(perfil, text="Fazer Login", foreground="white", width=20, height=1)
buttonlogin.place (x=80, y=320)
buttonlogin.config(background="#242424", highlightthickness=0, bd=0,  command=logar)

buttonsair = Button(perfil,text="Sair", foreground="white", width=20, height=1)#command=)
buttonsair.place (x=80, y=350)
buttonsair.config(background="#242424", highlightthickness=0, bd=0)

#RESOLUÇÃO
buttonfantasma = Button(perfil, width=20, height=1 , font="arial")
buttonfantasma.place (x=80, y=400)
buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

perfil.mainloop()
