#RESOLUÇÃO
buttonfantasma = Button(perfil, width=20, height=1 , font="arial")
buttonfantasma.place (x=80, y=400)
buttonfantasma.config(background="#242424", highlightthickness=0, bd=0)

perfil.mainloop()

#Ao introduzir um botão fantasma, conseguimos resolver o problema de exibição da imagem que anteriormente não estava sendo exibida na tela.
#Ao adicionar esse elemento invisível, a imagem passou a ser exibida corretamente, solucionando assim o bug de forma eficaz.
