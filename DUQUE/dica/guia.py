import tkinter as tk

#criar nossa janela
janela = tk.Tk()
janela.title ("LOGIN")
janela.geometry("300x500")
janela.config(bg="#242424")


#background
imagem = tk.PhotoImage(file = r"perfil\perfillogo.png")
#janela de login
label_fundo = tk.Label(janela, image = imagem)
label_fundo.place(x = 0, y = 0,) #relwidth =1 , relheight = 1)

janela.mainloop()