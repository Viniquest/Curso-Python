# introdução

import tkinter as tk

""" root = tk.Tk()

lbl = tk.Label(root, text="Ola Mundo!")
lbl.pack()

root.mainloop() """

# mudando titulo da janela

""" root = tk.Tk()

root.title("Teste de Título")

titulo = root.title()

lbl = tk.Label(root, text=titulo)
lbl.pack()

root.mainloop() """

# alterar o tamanho e localização da janela

""" root = tk.Tk()
root.title("Minha Aplicação GUI")

root.geometry("600x400-100+300") 
#root.geometry("600x400+100-300") 

root.mainloop() """

# centralizando a janela

""" root = tk.Tk()
root.title("Minha Aplicação GUI")

window_width = 600
window_heigth = 400

# obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# encontrar o ponto central
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_heigth / 2)

# definir a posição da janela no centro da tela
root.geometry(f"{window_width}x{window_heigth}+{center_x}+{center_y}")

root.mainloop() """

# comportamento de redimensionamento

""" root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300") 

# janela.metodo(largura, altura) 
root.resizable(True,True)
#root.resizable(False,False)
#root.resizable(False,True)

# definir limites de tamanho
root.minsize(300, 200)
root.maxsize(1200,800)

root.mainloop() """

# estado inicial da janela

""" root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300") """

# apresentar maximizada
#root.state("zoomed")

# apresentar minimizada
#root.state("iconic")

# apresentar normal (para casos onde a janela inicia de algum modo diferente)
#root.state("normal")

#print(root.state())
#root.title(root.state())

# Transparência da janela

# canal alpha valores entre 0.0 e 1.0
#root.attributes("-alpha", 0.5)

# Ordem de empilhamento da janela

""" # para garantir que a janela esteja sempre no topo
#root.attributes("-topmost", 1)

# para mover uma janela para cima
#root.lift()

# para mover uma janela para baixo
#root.lower() """

# Alterando o ícone padrão

#root.iconbitmap("C:/Users/NGI/Desktop/Curso Python/tkinter/imagens/python.ico")

# Introdução aos widgets temáticos do Tk

from tkinter import ttk

""" root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300") """

""" tk.Label(root, text="Label Classico").pack()
ttk.Label(root, text="Label Temático").pack()

tk.Button(root, text="Button Classico").pack()
ttk.Button(root, text="Button Temático").pack()"""

# definindo opções para um widget temático

""" # usando argumentos de palavra-chave ao criar o widget
ttk.Label(root, text="Olá Mundo!").pack() 

# usando um índice de dicionário após a criação do widget
lbl1 = ttk.Label(root)
lbl1["text"] = "Outro Olá Mundo!"
lbl1.pack()

# usando o método config() com atributos de palavra chave
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um Olá Mundo!")
lbl2.pack() """

# Introdução à vinculação de comandos Tkinter

""" def button_clicked():
    root.config(background="blue")
    print("Botão clicado!")

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300")

btn = ttk.Button(root, text="Click me!", command=button_clicked)
btn.pack()

root.mainloop() """

# Argumento de comando do botão tkinter

""" root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300")

def select(arg):
    root.config(background=arg)

btn1 = ttk.Button(root, text="Vermelho", command=lambda:select("red"))
btn1.pack()

btn2 = ttk.Button(root, text="Verde", command=lambda:select("green"))
btn2.pack()

btn3 = ttk.Button(root, text="Azul", command=lambda:select("blue"))
btn3.pack()

root.mainloop() """

# Introdução à associação de eventos Tkinter

""" def return_pressed(event):
    print("Tecla enter pressionada")

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300")

btn1 = ttk.Button(root, text="Executar")
btn1.bind("<Return>", return_pressed)
btn1.focus()
btn1.pack(expand=True)

root.mainloop() """

# Registrar vários manipuladores para o mesmo evento

""" def return_pressed(event):
    print("Tecla enter pressionada")

def log(event):
    print(event)

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300")

btn1 = ttk.Button(root, text="Executar")
btn1.bind("<Return>", return_pressed)
btn1.bind("<Return>", log, add="+")
btn1.focus()
btn1.pack(expand=True)

root.mainloop() """

# Padroes de eventos

""" def log(event):
    print(event)
    print(f"keysym....: {event.keysym}")
    print(f"keycode...: {event.keycode}")
    print(f"keysym_num: {event.keysym_num}")
    print(f"char......: {event.char}")

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+100+300")

btn1 = ttk.Button(root, text="Executar")
btn1.bind("<Any-KeyPress>", log, add="+")
btn1.focus()
btn1.pack(expand=True)

root.mainloop() """

# Vinculando eventos à janela raiz

""" def log(event):
    print(event)

root=tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")
root.bind("<Any-KeyPress>", log)

root.mainloop() """

# Os Níveis de ligação

""" def log(event):
    print(event)

root=tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

root.bind_class("Button","<Any-KeyPress>", log) #vincula esse bind a qualquer outro botão

btn1= tk.Button(root, text="Executar 1")
btn1.focus()
btn1.pack()

btn2= tk.Button(root, text="Executar 2")
btn2.pack()

btn3= tk.Button(root, text="Executar 3")
btn3.pack()

root.mainloop() """

# Desvinculação de eventos

""" def log(event):
    print("Evento Disparado...")

root=tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn1= ttk.Button(root, text="Executar 1")
btn1.bind("<Any-KeyPress>", log)
btn1.focus()
btn1.pack()

btn2= ttk.Button(root, text="Desvincular evento de executar", command=lambda: btn1.unbind("<Any-KeyPress>"))
btn2.pack()

btn3= ttk.Button(root, text="Vincular evento de executar", command=lambda: btn1.bind("<Any-KeyPress>", log)) # reativar
btn3.pack()

root.mainloop() """