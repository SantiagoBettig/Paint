#!/usr/bin/env python3

from tkinter import *
from PIL import Image

def BACK():
    if(len(Lista_Objetos)>1):
        Dibujo.delete(Lista_Objetos[-1])
        if(type(Lista_Objetos[-1]) == list):
            Lista_Ovalos = Lista_Objetos[-1]
            for i in range(len(Lista_Ovalos)):
                Dibujo.delete(Lista_Ovalos[i])
        Lista_Objetos.pop()

def Movimiento(event):
    global Inicio, Coordenada_X, Coordenada_Y, Linea, Objeto, Lista_Ovalos, Ovalo
    if(Seleccion == 1):
        if(Inicio == 1):
            Coordenada_X, Coordenada_Y = event.x, event.y
            Inicio = 0
            Objeto += 1
            Lista_Objetos.append(Dibujo.create_line(Coordenada_X, Coordenada_Y, event.x, event.y, fill = color, width = Ajuste))
        else:
            Dibujo.delete(Lista_Objetos[-1])
            Lista_Objetos[-1] = Dibujo.create_line(Coordenada_X, Coordenada_Y, event.x, event.y, fill = color, width = Ajuste)
            
    if(Seleccion == 2):
        if(Inicio == 1):
            Coordenada_X, Coordenada_Y = event.x, event.y
            Inicio = 0
            Objeto += 1
            Lista_Objetos.append(Dibujo.create_polygon(Coordenada_X, Coordenada_Y,Coordenada_X, Coordenada_Y,event.x, event.y, event.x, event.y, fill = "", outline = color, width = Ajuste))
        else:
            Ancho_X, Alto_Y = event.x - Coordenada_X, event.y - Coordenada_Y
            Dibujo.delete(Lista_Objetos[-1])
            Lista_Objetos[-1] = Dibujo.create_polygon(Coordenada_X, Coordenada_Y, Coordenada_X, Coordenada_Y + Alto_Y, event.x, event.y,Coordenada_X + Ancho_X, Coordenada_Y, fill = "", outline = color, width = Ajuste)
            
    if(Seleccion == 3):
        if(Inicio == 1):
            Coordenada_X, Coordenada_Y = event.x, event.y
            Inicio = 0
            Objeto += 1
            Lista_Objetos.append(Dibujo.create_oval(Coordenada_X, Coordenada_Y, event.x, event.y, fill = "",outline = color, width = Ajuste))
        else:
            Dibujo.delete(Lista_Objetos[-1])
            Lista_Objetos[-1] = Dibujo.create_oval(Coordenada_X, Coordenada_Y, event.x, event.y, fill = "", outline = color, width = Ajuste)
                
    elif(Seleccion == 4):
        Lista_Ovalos.append(Dibujo.create_oval( event.x - Ajuste, event.y - Ajuste, event.x + Ajuste, event.y + Ajuste, fill = color, outline = color))

    
def Scroll(event):
    global Ajuste
    if(event.num == 4 or event.delta == 120):
        if(Ajuste < 30):
            Ajuste += 1
    elif(event.num == 5 or event.delta == -120):
        if(Ajuste > 1):
            Ajuste -= 1

def Release(event):
    global Inicio, Lista_Objetos, Lista_Ovalos, Objeto
    Inicio = 1
    if(Seleccion == 4):
        Lista_Objetos.append(Lista_Ovalos)
        Lista_Ovalos = []

########################################################## Aca Termina el Uso del Mouse ########################################################################

def Botones_Dibujo():
    Tamaño = 6
    B_Linea = Button(V_Dibujo, text = "LINEA", width = Tamaño, command = LINEA)
    B_Linea.pack()
    
    B_RECT = Button(V_Dibujo, text = "RECT", width = Tamaño, command = RECT)
    B_RECT.pack()
    
    B_OVAL = Button(V_Dibujo, text = "OVALO", width = Tamaño, command = OVAL)
    B_OVAL.pack()
    
    B_LIBRE = Button(V_Dibujo, text = "LIBRE", width = Tamaño, command = LIBRE)
    B_LIBRE.pack()

    Label(V_Dibujo).pack() ## Para Separar y que quede lindo
    
    B_ROJO = Button(V_Dibujo, width = Tamaño, bg = "red", command = ROJO)
    B_ROJO.pack()
    
    B_AZUL = Button(V_Dibujo, width = Tamaño, bg = "blue", command = AZUL)
    B_AZUL.pack()
    
    B_VERDE = Button(V_Dibujo, width = Tamaño, bg = "green", command = VERDE)
    B_VERDE.pack()
    
    B_AMARILLO = Button(V_Dibujo, width = Tamaño, bg = "yellow", command = AMARILLO)
    B_AMARILLO.pack()

    B_VIOLETA = Button(V_Dibujo, width = Tamaño, bg = "purple", command = VIOLETA)
    B_VIOLETA.pack()

    B_NARANJA = Button(V_Dibujo, width = Tamaño, bg = "orange", command = NARANJA)
    B_NARANJA.pack()
    
    B_ROSA = Button(V_Dibujo, width = Tamaño, bg = "pink", command = ROSA)
    B_ROSA.pack()
    
    B_NEGRO = Button(V_Dibujo, width = Tamaño, bg = "black",command = NEGRO)
    B_NEGRO.pack()
    
    B_BLANCO = Button(V_Dibujo, width = Tamaño, bg = "white", command = BLANCO)
    B_BLANCO.pack()

    B_GRIS = Button(V_Dibujo, width = Tamaño, bg = "grey", command = GRIS)
    B_GRIS.pack()
    
    Label(V_Dibujo).pack() ## Para Separar y que quede lindo

    B_BACK = Button(V_Dibujo,text = "Control+z", width = Tamaño, command = BACK)
    B_BACK.pack()
        
    B_NEW = Button(V_Dibujo,text = "Nuevo", width = Tamaño, command = NEW)
    B_NEW.pack()

    B_OPEN = Button(V_Dibujo,text = "Abrir", width = Tamaño, command = OPEN)
    B_OPEN.pack()

    B_SAVE = Button(V_Dibujo,text = "Guardar", width = Tamaño, command = SAVE)
    B_SAVE.pack()

    B_EXIT = Button(V_Dibujo,text = "Exit", width = Tamaño, command = EXIT)
    B_EXIT.pack()

def V_OPEN():
    global E_DIR, V_IMAGE, Opcion, New
    V_IMAGE = Tk()
    V_IMAGE.title("P.A.I.N.T")
    V_IMAGE.geometry("350x50")
    
    if(Opcion == 1):
        B_ENTER = Button(V_IMAGE, text = "ENTER", command = ENTER)
        B_ENTER.pack(side = LEFT)
    else:
        B_ENTER = Button(V_IMAGE, text = "ENTER", command = ENTER_2)
        B_ENTER.pack(side = LEFT)

    E_DIR = Entry(V_IMAGE, text = "Ingrese la Direccion",bd = 3, width = 100)
    E_DIR.pack(side = RIGHT)

def V_CANVAS():
    global V_Dibujo, Seleccion, Dibujo, color, Ajuste, Inicio, Coordenada_X, Coordenada_Y, Opcion, Lista_Objetos, Objeto, Lista_Ovalos, Ovalo, New
    Ovalo = 0
    Lista_Objetos = [1]
    Lista_Ovalos = []
    Objeto = 0
    Ajuste = 1
    Opcion = 2
    Inicio = 1
    Seleccion = 1
    color = "red"
    V_Dibujo = Tk()
    V_Dibujo.title("P.A.I.N.T")
    
    Dibujo = Canvas(V_Dibujo, width = 600, height = 600)
    Dibujo.pack(side = RIGHT)
    
    Dibujo.bind( "<B1-Motion>", Movimiento) ##Detecto movimiento del Mouse

    Dibujo.bind( "<ButtonRelease-1>", Release)
    
    Dibujo.bind("<Button-4>", Scroll) ## Detecto el Scroll del Mouse
    Dibujo.bind("<Button-5>", Scroll) ##

    Dibujo.bind("<Control-z>", BACK)
    
    if New == 0 :
        Photo = PhotoImage(file = Direccion)
        
        Label_Photo = Label(image = Photo) ## Con Estas dos Lineas hago una referencia a la Imagen
        Label_Photo.image = Photo          ##
    
        Imagen = Dibujo.create_image(300,300,image = Photo)
        New = 0
    else:
       Dibujo.configure(bg = "white")
       New = 0
    Botones_Dibujo()    

def Principal():
    global V_Princ, Opcion
    Opcion = 1
    V_Princ = Tk()
    V_Princ.title("P.A.I.N.T")
    V_Princ.geometry("200x75")

    F1 = Frame(V_Princ)
    F1.pack(side = TOP)

    F2 = Frame(V_Princ)
    F2.pack()

    F3 = Frame(V_Princ)
    F3.pack()

    Label(F1, text = "WELCOME TO D.E.G.A", fg = "green").pack(side = TOP)

    B_NEW = Button(F2, text = "NEW", width = 9, command = NEW)
    B_NEW.pack(side = LEFT)

    B_OPEN = Button(F2, text = "OPEN", width = 9, command = OPEN)
    B_OPEN.pack(side = RIGHT)

    B_EXIT = Button(F3, text = "EXIT", width = 22, command = EXIT)
    B_EXIT.pack()
    
    V_Princ.mainloop()
    
############################################ ACA EMPIEZAN LOS BOTONES #############################################

def EXIT():
    exit()

def OPEN():
    global Open, New
    if(Opcion == 1):
        V_Princ.destroy()
    if(Opcion == 2):
        Open = 1
    New = 0
    V_OPEN()

def NEW():
    global New
    global Direccion
    if(Opcion == 1):
        V_Princ.destroy()
    elif(Opcion == 2):
        V_Dibujo.destroy()
    New = 1
    V_CANVAS()

def ENTER():
    global Direccion, Opcion
    Direccion = E_DIR.get()
    try:
        Imagen = Image.open(Direccion)
        Imagen = Imagen.resize((600,600), Image.ANTIALIAS)
        Imagen = Imagen.save("DEGA.gif")
    except :
        messagebox.showerror("ERROR", "La Direccion No es Valida O no Existe el Archivo")
    else:
        V_IMAGE.destroy()
        Direccion = "DEGA.gif"
        V_CANVAS()
    

def ENTER_2():
    global Direccion, Open
    Direccion = E_DIR.get()
    if(Open == 1):
        try:
            Imagen = Image.open(Direccion)
            Imagen = Imagen.resize((600,600), Image.ANTIALIAS)
            Imagen = Imagen.save("DEGA.gif")
        except :
            messagebox.showerror("ERROR", "La Direccion No es Valida O no Existe el Archivo")
        else:
            V_IMAGE.destroy()
            V_Dibujo.destroy()
            Direccion = "DEGA.gif"
            V_CANVAS()
    else:
        Dibujo.postscript(file = Direccion + ".ps", colormode = "color")
        Imagen = Image.open(Direccion + ".ps")
        Imagen = Imagen.resize((600,600), Image.ANTIALIAS)
        try:
            Imagen = Imagen.save(Direccion)
        except:
            Imagen = Imagen.save(Direccion + ".jpeg")
        Image.remove(Direccion+".ps")
        V_IMAGE.destroy()

def LINEA():
    global Seleccion, Inicio, Coordenada_X, Coordenada_Y
    Seleccion = 1
    Inicio = 1
    Coordenada_X = 0
    Coordenada_Y = 0

def RECT():
    global Seleccion, Inicio, Coordenada_X, Coordenada_Y
    Seleccion = 2
    Inicio = 1
    Coordenada_X = 0
    Coordenada_Y = 0

def OVAL():
    global Seleccion, Inicio, Coordenada_X, Coordenada_Y
    Seleccion = 3
    Inicio = 1
    Coordenada_X = 0
    Coordenada_Y = 0
    
def LIBRE():
    global Seleccion
    Seleccion = 4

def ROJO():
    global color
    color = "red"

def AZUL():
    global color
    color = "blue"

def VERDE():
    global color
    color = "green"

def AMARILLO():
    global color
    color = "yellow"

def VIOLETA():
    global color
    color = "purple"

def NARANJA():
    global color
    color = "orange"

def ROSA():
    global color
    color = "pink"

def NEGRO():
    global color
    color = "black"

def BLANCO():
    global color
    color = "white"

def GRIS():
    global color
    color = "grey"
    
def SAVE():
    global Opcion, Open
    Open = 0
    V_OPEN()

    
Principal()
