# Importamos los modulos necesarios
import sys # Para acceder a argumentos del sistema viejos para poder utilizar PyQt5(sys.argv)

# Modulo de PyQt5 para la interfaz y navegacion web
from PyQt5.QtCore import QUrl # Funciona para poder  ocupar la url de el navegador
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import QWebEngineView # sirve para poder mostrar el navegador

#Clase principal del navegador que hereda de QMainWindow
class NavegadorWeb(QMainWindow):
    def __init__(self): # constructor de la clase
        super().__init__() #Inicializa la clase base QMainwindow

        #Configuramos la ventana principal
        self.setWindowTitle('Navegador web') # Titulo de la ventana
        self.setGeometry(100,100,1024,768) # Poscicion y tamano de la ventana

        # Creamos el visor web donde se mostraran las paginas
        self.navegador = QWebEngineView()
        self.navegador.setUrl(QUrl('https://www.google.com'))# Pagina de inicio

        #Creamos la barra de herramientas de navegacion
        barra_navegacion = QToolBar('Barra de navegacion')
        self.addToolBar(barra_navegacion) # Anadimos  la barra a la ventana

        # Boton para ir hacia atras 
        boton_atras = QAction('⇐', self)
        boton_atras.setStatusTip('Atras')
        boton_atras.triggered.connect(self.navegador.back) # Conectamos a la funcion back de navegador
        barra_navegacion.addAction(boton_atras) # Anadimos el boton a la barra

        #Boton para ir hacia adelante
        boton_adelante = QAction('⇒', self)
        boton_adelante.setStatusTip('Adelante')
        boton_adelante.triggered.connect(self.navegador.forward)
        barra_navegacion.addAction(boton_adelante)

        #Boton para recargar la pagina
        boton_recargar = QAction('↻', self)
        boton_recargar.setStatusTip('Recargar')
        boton_recargar.triggered.connect(self.navegador.reload)
        barra_navegacion.addAction(boton_recargar)

        #Campo de texto para ingresar direcciones web
        self.barra_direcciones = QLineEdit()
        self.barra_direcciones.setPlaceholderText('Escribe una URL y presiona enter')
        self.barra_direcciones.returnPressed.connect(self.cargar_url) #llama a cargar_url al presionar enter
        barra_navegacion.addWidget(self.barra_direcciones) # anadimos el campo a la barra

        #Actualizamos la barra de direcciones cuando cambia la URL
        self.navegador.urlChanged.connect(self.actualizar_barra_direcciones)

        # Colocamos el navegador como el widget principal de la ventana
        self.setCentralWidget(self.navegador)

    # Funcion que carga la URL ingresada en el campo de texto
    def cargar_url(self):
        url = self.barra_direcciones.text() # Obtenemos el texto escrito
        if url:
            # Si no empieza con http o htpps, le anadimos hptt:// por defecto
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            self.navegador.setUrl(QUrl(url)) # Cargamos la url en el navegador

    # Funcion que actualiza la barra de direcciones cuando cambia la pagina
    def actualizar_barra_direcciones(self, url):
        self.barra_direcciones.setText(url.toString()) # Mostramos la url actual
        self.barra_direcciones.setCursorPosition(0) # Colocamos el cursor al principio

#Codigo principal que se ejecuta si el archivo es el programa principal
if __name__ == '__main__':
    app = QApplication(sys.argv)    #Creamos la aplicacion Qt
    ventana = NavegadorWeb()        #Creamos la ventana del navegador
    ventana.show()                  #Mostramos la ventana
    sys.exit(app.exec_())





