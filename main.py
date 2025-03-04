#Se importan las librerias que se van a usar
import tkinter as tk
import random

#Tablero representado por una matriz, donde se ubican las posiciones iniciales de las fichas
pos = [
        ["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "rojo1", "rojo2", "--", "--", "--", "--", "verde1", "verde2", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "rojo3", "rojo4", "--", "--", "--", "--", "verde3", "verde4", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "azul1", "azul2", "--", "--", "--", "--", "amarillo1", "amarillo2", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "azul3", "azul4", "--", "--", "--", "--", "amarillo3", "amarillo4", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ]
#crear una clase que cree una nueva ventana
class tablero():
    def __init__(self, cuadrado):
        """crea un método que se ejecuta solo cuando formamos un objeto de la clase"""
        #self hace referecia a los atributos de la clase misma, a los que pertenecen a ese objeto en especifico

        #renombrar el parámetro cuadrado, que recibe un tamaño en pixeles
        self.cuadrado = cuadrado
        #Crear un diccionario en donde se almacenan las imagenes junto a su numbre
        self.imagenes = {}

        #Crear la ventana y su nombre
        self.ventana = tk.Tk()
        self.ventana.title("Parqués")

        #geometry establece las dimensiones de la ventana
        self.ventana.geometry(f"{str(cuadrado*26)}x{str(cuadrado*17)}")
        #En este caso resizable evita que se redimensione la ventana
        self.ventana.resizable(0,0)

        #canvas en tkinter nos brinda una superficie sobre la que podemos dibujar distintas figuras
        self.interfaz = tk.Canvas(self.ventana, width=26*self.cuadrado, height=17*self.cuadrado, background="white")
        #pack es un gestor de geometría que organiza widgets en bloques. Expand llena cualquier espacio que no se esta usando. Fill determina si un widget llena el espacio extra, en este caso lo hace vertical y horizontalmente
        self.interfaz.pack(fill="both",expand=True)

        #Determinar los jugadores
        self.jugadores = ["azul","amarillo","verde","rojo"]
        #Variable que enlaza los RadioButtons de seleccion del jugador
        self.jugador = tk.StringVar()

        #Variable que enlaza los radioButton de fichaseleccionada
        self.fichaselec = tk.StringVar()

        #Posicion inicial de cada ficha en forma (y,x)
        self.posicionini = {"azul1":(10,5),"azul2":(10,6),"azul3":(11,5),"azul4":(11,6),
                         "amarillo1":(11,11),"amarillo2":(10,12),"amarillo3":(11,11),"amarillo4":(11,12),
                         "verde1":(5,11),"verde2":(5,12),"verde3":(6,11),"verde4":(6,12),
                         "rojo1":(5,5),"rojo2":(5,6),"rojo3":(6,5),"rojo4":(6,6)}

        #posicion actual de cada ficha (y,x), se actualiza a medida que se mueven las fichas
        self.posicionfin = {"azul1":(10,5),"azul2":(10,6),"azul3":(11,5),"azul4":(11,6),
                         "amarillo1":(11,11),"amarillo2":(10,12),"amarillo3":(11,11),"amarillo4":(11,12),
                         "verde1":(5,11),"verde2":(5,12),"verde3":(6,11),"verde4":(6,12),
                         "rojo1":(5,5),"rojo2":(5,6),"rojo3":(6,5),"rojo4":(6,6)}

    def __call__(self):
        """método que permite que las instancias de una clase se comporten como funciones"""
        # Correr/Abrir la ventana
        self.ventana.mainloop()

    def dibujarTablero(self):
        """crea el tablero del juego"""
        #Aqui se generan las casillas normales
        for i in range(17):
            for j in range(17):
                #create_rectangle() genera un rectángulo en el canvas, recibe (x0,y0,x1,y1,fill)
                self.interfaz.create_rectangle(i * self.cuadrado, j * self.cuadrado, (i + 1) * self.cuadrado,(j + 1) * self.cuadrado, fill="white")
        #Aqui se generan las casillas especiales de llegada de cada ficha
        for i in range(17):
            for j in range(17):
                #Casillas de llegada azules
                if i == 0 and j == 8:
                    for x in range(8):
                        self.interfaz.create_rectangle((i + x)* self.cuadrado, j * self.cuadrado, (1+x)*self.cuadrado,9*self.cuadrado, fill="#3a7ef7")
                #Casillas de llegada rojas
                elif i == 8 and j == 0:
                    for x in range(8):
                        self.interfaz.create_rectangle(8 * self.cuadrado, (0+x) * self.cuadrado, 9*self.cuadrado,(1+x)*self.cuadrado, fill="#ef2e2e")
                #Casillas de llegada verdes
                elif i == 9 and j == 8:
                    for x in range(8):
                        self.interfaz.create_rectangle((i + x) * self.cuadrado, j * self.cuadrado,(10 + x) * self.cuadrado, 9 * self.cuadrado, fill="#46ef2e")
                #Casillas de llegada amarillas
                elif i == 8 and j == 9:
                    for x in range(8):
                        self.interfaz.create_rectangle(i * self.cuadrado, (j+x) * self.cuadrado, 9*self.cuadrado,(10+x)*self.cuadrado, fill="#f7f53a")

        #Aqui se generan las casillas especiales de salida y seguro
                #Salida y seguro azul
                elif i ==4 and j ==9:
                    self.interfaz.create_rectangle(i * self.cuadrado, j * self.cuadrado, 5 * self.cuadrado,10 * self.cuadrado, fill="#006382")
                    self.interfaz.create_rectangle(7 * self.cuadrado, 12 * self.cuadrado, 8 * self.cuadrado,13 * self.cuadrado, fill="#006382")
                #Salida y seguro amarillo
                elif i ==9 and j ==12:
                    self.interfaz.create_rectangle(i * self.cuadrado, j * self.cuadrado, 10 * self.cuadrado, 13 * self.cuadrado, fill="#c0ae00")
                    self.interfaz.create_rectangle(j * self.cuadrado, i * self.cuadrado, 13 * self.cuadrado,10* self.cuadrado, fill="#c0ae00")
                #Salida y seguro verde
                elif i ==12 and j ==7:
                    self.interfaz.create_rectangle(i * self.cuadrado, j * self.cuadrado, 13 * self.cuadrado,8 * self.cuadrado, fill="#2aa03b")
                    self.interfaz.create_rectangle(9 * self.cuadrado, 4 * self.cuadrado, 10 * self.cuadrado,5 * self.cuadrado, fill="#2aa03b")
                #Salida y seguro roja
                elif i ==7 and j==4:
                    self.interfaz.create_rectangle(i * self.cuadrado, j * self.cuadrado, 8 * self.cuadrado,5 * self.cuadrado, fill="#a11")
                    self.interfaz.create_rectangle(j * self.cuadrado, i * self.cuadrado, 5 * self.cuadrado,8 * self.cuadrado, fill="#a11")

        #Aqui se generan las casillas "carcel"
        #carcel roja
        self.interfaz.create_rectangle(0*self.cuadrado,0*self.cuadrado,7*self.cuadrado,7*self.cuadrado,fill="#ef2e2e")
        #carcel azul
        self.interfaz.create_rectangle(0 * self.cuadrado, 10 * self.cuadrado, 7 * self.cuadrado, 17 * self.cuadrado,fill="#3a7ef7")
        #carcel amarilla
        self.interfaz.create_rectangle(10 * self.cuadrado, 10 * self.cuadrado, 17 * self.cuadrado, 17 * self.cuadrado,fill="#f7f53a")
        #carcel verde
        self.interfaz.create_rectangle(10 * self.cuadrado, 0 * self.cuadrado, 17 * self.cuadrado, 7 * self.cuadrado,fill="#46ef2e")

    #cargamos las fichas, esto es experimental. Lee una imagen
    def cargarImagenes(self):
        """carga al sistema las imagenes de las fichas"""
        #PhotoImage lee una imagen
        piezas = ["amarillo1","amarillo2","amarillo3","amarillo4","azul1","azul2","azul3","azul4","rojo1","rojo2","rojo3","rojo4","verde1","verde2","verde3","verde4"]
        for ficha in piezas:
            self.imagenes[ficha] = tk.PhotoImage(file="./Imagenes/"+ficha+".png")
    def mostrarImagenes(self):
        """Ubica las imagenes de las fichas en el tablero"""
        #indice_i accede a la lista, i al copntenido de la lista
        #enumerate agrega un contador a cada item de una lista
        for indice_i, i in enumerate(pos):
            for indice_j, j in enumerate(i):
                if j != "--":
                    #icreate_image permite visualizar una imagen
                    #anchor ="nw" es para que la imagen quede centrada
                    self.interfaz.create_image(indice_j*self.cuadrado, indice_i*self.cuadrado, image = self.imagenes[j], anchor="nw")

    def comandoJugador(self):
        """Retorna el valor del color que representa al jugador"""
        seleccion = self.jugador.get()
        return seleccion
    def seleccionJugador(self):
        """Seleccionar el color que va a representar al jugador"""
        #RadioButton le permite al usuario seleccionar una entre varias opciones, las cuales se asocian a una variable especial
        for i in range(len(self.jugadores)):
            tk.Radiobutton(text=self.jugadores[i], variable=self.jugador, value=self.jugadores[i],command=self.comandoJugador).place(x=(18 + 2 * i) * self.cuadrado, y=3 * self.cuadrado)
    def turno(self):
        """Boton que permite seleccionar que jugador va a ejecutar su turno"""
        #Button recuadro de texto que puede ser presionado por el usuario para que ejecute un comando
        boton3 = tk.Button(text="Seleccione el jugador de turno", command=self.seleccionJugador)
        boton3.place(x=19 * self.cuadrado, y=2 * self.cuadrado)

    def dados(self):
        """Simula un lanzamiento de dados"""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1,dado2
    def comandoDados(self,dado1,dado2):
        """Genera una etiqueta con los resultados del lanzamiento"""
        #Label se usa para implementar cajas de visualización donde se pueden ubicar texto o imágenes
        tk.Label(text="Resultado dado 1: "+str(dado1)).place(x=19*self.cuadrado, y=5*self.cuadrado)
        tk.Label(text="Resultado dado 2: "+str(dado2)).place(x=19 * self.cuadrado, y=6 * self.cuadrado)#lambda permite hacer 'mini funciones' y eso hará que todo se comprima en ella misma

    def interaccion1(self,dado1,dado2):
        """genera un botón con el cual el usuario interacciona para visualizar el resultado del lanzamiento de dos dados"""
        #lambda permite agregar parametros al comando sin que se ejecute de inmediato
        boton1 = tk.Button(text = "Tirar los dados",command= lambda : self.comandoDados(dado1,dado2))
        boton1.place(x=19*self.cuadrado, y=4*self.cuadrado)

    def resultadoFicha(self):
        """Retorna el resultado de la ficha seleccionada"""
        seleccion = self.fichaselec.get()
        return seleccion

    def seleccionFicha(self):
        """genera distintas opciones para que el usuario elija qué ficha particular desea mover"""
        seleccion = self.jugador.get()
        for i in range(1, 5):
            tk.Radiobutton(text=seleccion + str(i), variable=self.fichaselec,value=seleccion + str(i),command=self.resultadoFicha).place(x=(16 + 2*i) * self.cuadrado, y=8 * self.cuadrado)

    def interaccion2(self):
        """Crea un botón para que aparezcan las opciones de que fichas puede mover el jugador"""
        #creamos el boton de movimiento de la ficha
        boton2 = tk.Button(text="¿Qué ficha desea mover?",command=self.seleccionFicha)
        boton2.place(x=19*self.cuadrado,y=7*self.cuadrado)

    def encontrarPosicion(self,selec):
        """Actualiza la posicion de la ficha. Recibe el string de la ficha que se quiere verificar"""
        for i in range(len(pos)):
            if selec in pos[i]:
                y = i
                x = pos[i].index(selec)
                self.posicionfin[selec]=(y,x)
    def mainloop(self):
        """ejecuta en bucle el código principal"""
        #mostrar imagenes se llama internamente debido a que es una funcion que debe estar actualizandose
        self.mostrarImagenes()
        self.turno()
        dado1,dado2=self.dados()
        self.interaccion1(dado1,dado2)
        self.interaccion2()


#Al iniciar se le debe pasar la longitud del cuadrado, un ejemplo es 40
MotorJuego = tablero(40)
MotorJuego.dibujarTablero()
MotorJuego.cargarImagenes()
MotorJuego.mainloop()

MotorJuego()








