from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib.pyplot as pt
import Conversiones as conv
import numpy as np
from datetime import datetime

window_width = 1200
window_height = 630
side_menu_width = 190
C1_width = 170
C_width = 150
separacion = 10
pos_init = 50


def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def csc(x):
    return 1/np.sin(x)

def sec(x):
    return 1/np.cos(x)

def cot(x):
    return 1/np.tan(x)
def arcsin(x):
    return np.arcsin(x)

def arccos(x):
    return np.arccos(x)

def arctan(x):
    return np.arctan(x)

def sinh(x):
    return np.sinh(x)

def cosh(x):
    return np.cosh(x)

def tanh(x):
    return np.tanh(x)

def csch(x):
    return 1/np.sinh(x)

def sech(x):
    return 1/np.cosh(x)

def coth(x):
    return 1/np.tanh(x)

def arcsinh(x):
    return np.arcsinh(x)

def arccosh(x):
    return np.arccosh(x)

def arctanh(x):
    return np.arctanh(x)

def sqrt(x):
    return np.sqrt(x)

pi = np.pi

class LineEdit(QtWidgets.QLineEdit):
    focus_in_signal = QtCore.pyqtSignal()
    focus_out_signal = QtCore.pyqtSignal()

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.focus_in_signal.emit()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.focus_out_signal.emit()


class Ui_MainWindow(QtWidgets.QWidget):
    font = None
    count = 0
    matriz_tipo = []
    lista_tipo = []
    num_filas = 1
    lista_objetos = []
    lista_estados = []
    sender_val = ""
    componente = ""
    valor = 0
    operacion = None
    estado = ""
    y = 0
    e_actual = ""
    e_actual_1 = ""
    direccion_actual = ""
    flag_conversion = 0
    flag_conversion_unidades = 0
    names = ['Clear', "<--", '',
             '7', '8', '9',
             '4', '5', '6',
             '1', '2', '3',
             '0', '.', 'π']
    botones_calculadora = ["C", "√", "(", ")", "1/x", "mod",
                           '<--', 'x^2', "|x|", "n!", "%", "÷",
                           "floor", "x^3", "7", "8", "9", "x",
                           "ceil", "10^x", "4", "5", "6", "-",
                           "e", "log", "1", "2", "3", "+",
                           "π", "ln", "+/-", "0", ".", "="
                           ]
    lista_materiales = ['OPAMP', "amplificadores de instrumentación", 'Reguladores de tensión',
                        'Transistores', 'Sensores', 'Microcontroladores',
                        'DACs', 'Resistencias', 'Capacitores',
                        'FPGAs', '2', '3',
                        '0', '.', '']
    lista_secciones = ["inicio", "proyecto_actual", "lista_materiales", "calculos", "calculadora",
                       "acerca_de", "Programador", "Volumen", " Temperatura", "nuevo_proyecto",
                       "Velocidad", "Temperatura", "Buscar", "graficas",
                       "Tiempo", "Angulo", "Presion", "Energia", "Fuerza", "Masa", "longitud"]

    lista_componentes_0 = ["LPV511MGX", "AD8542ARZ", "TLV2382", "AD8603", "LMP2231", "TLV2372",
                           "LMP2234", "TLV2371", "LMC6462", "AD8607", "OPA347", "TLV8542", "TLV8541",
                           "LMP2232", "LT1495", "TLV2314QDRQ1", "TLV9102", "LMP7702", "AD8609"
                           ]
    lista_componentes_2 = ["TS9011SCYRMG", "TPS709B50DBVT", "TPS709B33DBVT", "TPS709B30DBVT", "TS9011SCYRMG",
                           "TPS76930DBVT", "TPS70916DBVT", "REF1933AIDDCT", "MAX6018", "REF1930AIDDCT", "TPS7A0515",
                           "TPS78230DDCR", "TPS78225DDCR", "TPS7A0530", "TPS7A0533"
                           ]
    lista_parametros_0 = ["Tipo de amplificador",
                          "Número de circuitos",
                          "Tipo de salida",
                          "Velocidad de respuesta",
                          "Producto de ancho de banda de ganancia",
                          "Corriente - Derivación de entrada",
                          "Voltaje - Desviación de entrada",
                          "Corriente - Suministro",
                          "Corriente - Salida/Canal",
                          "Voltaje - Suministro, simple/doble (±)",
                          "Temperatura de funcionamiento",
                          "Tipo de montaje",
                          "Paquete / Caja carcasa",
                          "Paquete del dispositivo"
                          ]
    lista_parametros_2 = ["Fabricante",
                          "Serie",
                          "Embalaje",
                          "Estado de pieza",
                          "Configuración de salida",
                          "Tipo de salida",
                          "Cantidad de reguladores",
                          "Voltaje - Entrada (máx.)",
                          "Voltaje - Salida (mín/fijo)",
                          "Voltaje - Salida (máx.)",
                          "Caída del voltaje (máx.)",
                          "Corriente - Salida",
                          "Corriente - reposo (lq)",
                          "Corriente - Alimentación (máx.)",
                          "PSRR",
                          "Características de control",
                          "Características de protección",
                          "Temperatura de funcionamiento",
                          "Tipo de montaje", "Paquete / Caja (carcasa)", "Paquete del dispositivo del proveedor"
                          ]
    lista_parametros_3 = []

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width, window_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(182, 14, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)

        self.grupo_menu = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(0, 0, side_menu_width, window_height, "grupo_menu", self.grupo_menu, "rgb(127,127,127)")
        self.grupo_contenido = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_contenido",
                            self.grupo_contenido, "white")

        self.boton = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 75, 171, 75, "Inicio", self.boton, self.label_menu, "rgb(127,127,127)")

        self.boton_menu = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_1 = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 150, 171, 75, "Proyecto actual", self.boton_menu, self.label_menu_1,
                              "rgb(127,127,127)")
        self.boton_menu.setEnabled(False)
        self.boton_menu_1 = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_2 = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 225, 171, 75, "Lista de materiales", self.boton_menu_1, self.label_menu_2,
                              "rgb(127,127,127)")

        self.boton_menu_2 = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_3 = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 300, 171, 75, "Cálculos", self.boton_menu_2, self.label_menu_3,
                              "rgb(127,127,127)")
        self.boton_menu_3 = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_4 = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 375, 171, 75, "Configuración", self.boton_menu_3, self.label_menu_4,
                              "rgb(127,127,127)")
        self.boton_menu_4 = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_4 = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(0, 450, 171, 75, "Acerca de", self.boton_menu_4, self.label_menu_4,
                              "rgb(127,127,127)")


        self.boton_redondo = QtWidgets.QPushButton(self.grupo_contenido)
        self.crear_boton_redondo(pos_init, 100, 200, "Nuevo proyecto", self.boton_redondo, "white", "black")
        self.boton_redondo_1 = QtWidgets.QPushButton(self.grupo_contenido)
        self.crear_boton_redondo(pos_init + 200 + separacion, 100, 200, "Buscar", self.boton_redondo_1, "white",
                                 "black")
        self.boton_redondo_2 = QtWidgets.QPushButton(self.grupo_contenido)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 2, 100, 200, "Abrir", self.boton_redondo_2, "white",
                                 "black")
        self.label_inicial = QtWidgets.QLabel(self.grupo_contenido)
        self.crear_label(10, 10, 400, 50, "¿Que quieres hacer?", self.label_inicial, "white")
        self.label_inicial.setFont(self.set_font(16))
        self.boton_redondo_3 = QtWidgets.QPushButton(self.grupo_contenido)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3, 100, 200, "Guardar", self.boton_redondo_3,
                                 "white", "black")
        self.boton_redondo_atras = QtWidgets.QPushButton(self.grupo_menu)
        self.crear_boton_redondo(side_menu_width - 30, 0, 30, "flecha izquierda", self.boton_redondo_atras,
                                 "rgb(127,127,127)", "black")
        self.boton_redondo_atras.setText("")

        self.grupo_nuevo_proyecto = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_nuevo_proyecto",
                            self.grupo_nuevo_proyecto, "white")
        self.label_nuevo_proyecto = QtWidgets.QLabel(self.grupo_nuevo_proyecto)
        self.crear_label(10, 10, 300, 70, "Primero necesitamos lo siguiente:", self.label_nuevo_proyecto, "white")
        self.edit_label_nombre = QtWidgets.QLineEdit(self.grupo_nuevo_proyecto)
        self.crear_lineEdit(50, 90, 300, 35, "Autor", self.edit_label_nombre)
        self.edit_label_nombre_proyecto = QtWidgets.QLineEdit(self.grupo_nuevo_proyecto)
        self.crear_lineEdit(50, (90 + 40), 300, 35, "Nombre del proyecto", self.edit_label_nombre_proyecto)
        self.edit_label_direccion = QtWidgets.QLineEdit(self.grupo_nuevo_proyecto)
        self.crear_lineEdit(50, (130 + 40), 300, 35, "Dirección", self.edit_label_direccion)
        self.edit_label_direccion.setReadOnly(True)
        self.boton_redondo_direccion = QtWidgets.QPushButton(self.grupo_nuevo_proyecto)
        self.crear_boton_redondo(355, (130 + 40), 30, "Guardar", self.boton_redondo_direccion,
                                 "white", "black")
        self.boton_redondo_direccion.setText("")
        self.boton_redondo_direccion.clicked.connect(lambda: self.funcion_guardar_como())
        self.edit_label_correo = QtWidgets.QLineEdit(self.grupo_nuevo_proyecto)
        self.crear_lineEdit(50, (175 + 35), 300, 35, "Correo electrónico", self.edit_label_correo)
        self.label_descripcion = QtWidgets.QLabel(self.grupo_nuevo_proyecto)
        self.crear_label(50, (210 + 40), 300, 35, "Descripción:", self.label_descripcion, "white")
        self.textedit = QtWidgets.QTextEdit(self.grupo_nuevo_proyecto)
        self.crear_textedit(50, 290, 300, 300, "Número máximo de palabras : 100", self.textedit)
        self.boton_hecho = QtWidgets.QPushButton(self.grupo_nuevo_proyecto)
        self.crear_boton_normal(140, 595, 100, 30, "Hecho", self.boton_hecho, "black", "white", "boton_hecho")

        self.grupo_buscar = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_buscar",
                            self.grupo_buscar, "white")
        self.label_buscar = QtWidgets.QLabel(self.grupo_buscar)
        self.crear_label(10, 10, 300, 70, "Buscar:", self.label_buscar, "white")

        self.grupo_proyectoactual = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_proyecto_actual",
                            self.grupo_proyectoactual, "white")

        self.label_proyectoactual = QtWidgets.QLabel(self.grupo_proyectoactual)
        self.crear_label(10, 10, 500, 40, "Proyecto Actual", self.label_proyectoactual, "white")
        self.label_proyectoactual.setFont(self.set_font(18))

        self.tabla_proyecto = QtWidgets.QTableWidget(self.grupo_proyectoactual)
        self.crear_tableWidget(0, 7, "tabla_proyecto", 10, 90, window_width - side_menu_width - 40, 225,
                               self.tabla_proyecto)
        self.boton_expandir = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_redondo(10, 50, 30, "Triangulo arriba", self.boton_expandir, "white", "black")
        self.boton_expandir.setText("")
        self.boton_agregar_fila = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(10, 320, 200, 30, "Agregar fila", self.boton_agregar_fila, "white", "back",
                                "boton_agregar_fila")
        self.boton_remover_fila = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(210, 320, 200, 30, "Remover fila", self.boton_remover_fila, "white", "back",
                                "boton_remover_fila")

        self.tabla_proyecto.setHorizontalHeaderItem(4, self.define_titulo_columna("Estado  "))
        self.tabla_proyecto.setHorizontalHeaderItem(0, self.define_titulo_columna("Actividad  "))
        self.tabla_proyecto.setHorizontalHeaderItem(1, self.define_titulo_columna("Fecha inicio"))
        self.tabla_proyecto.setHorizontalHeaderItem(2, self.define_titulo_columna("Fecha de finalizacion"))
        self.tabla_proyecto.setHorizontalHeaderItem(3, self.define_titulo_columna("Comentarios  "))
        self.tabla_proyecto.setHorizontalHeaderItem(5, self.define_titulo_columna("Hora de inicio  "))
        self.tabla_proyecto.setHorizontalHeaderItem(6, self.define_titulo_columna("Hora de finalización  "))
        self.tabla_proyecto.resizeColumnsToContents()
        self.tabla_proyecto.setColumnWidth(0, 400)
        self.tabla_proyecto.setColumnWidth(4, 100)

        self.calendario = QtWidgets.QCalendarWidget(self.grupo_proyectoactual)
        self.crear_calendarwidget(500, 350, 355, 270, "Calendario", self.calendario)
        self.calendario.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.progressbar_1 = QtWidgets.QProgressBar(self.grupo_proyectoactual)
        self.crear_progressbar(500, 320, 415, 30, "barra_progreso", self.progressbar_1)
        self.progressbar_1.setValue(0)
        self.boton_arriba = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(10, 360, 200, 30, "Mover hacia arriba", self.boton_arriba, "white", "back",
                                "boton_arriba")
        self.boton_abajo = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(210, 360, 200, 30, "Mover hacia abajo", self.boton_abajo, "white", "back",
                                "boton_abajo")
        self.boton_guardar_proyectoactual = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(650, 50, 150, 30, "Guardar", self.boton_guardar_proyectoactual, "white", "back",
                                "boton_guardar_proyectoactual")
        self.boton_estadisticas = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(800, 50, 150, 30, "Estadísticas", self.boton_estadisticas, "white", "back",
                                "boton_estadisticas")
        self.boton_estadisticas.setEnabled(False)
        self.boton_guardar_como_proyectoactual = QtWidgets.QPushButton(self.grupo_proyectoactual)
        self.crear_boton_normal(500, 50, 150, 30, "Guardar como", self.boton_guardar_como_proyectoactual, "white", "back",
                                "boton_guardar_como_proyectoactual")
        self.boton_guardar_como_proyectoactual.clicked.connect(lambda :self.funcion_guardar_como())

        self.grupo_calculos = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_calculos",
                            self.grupo_calculos, "white")
        self.boton_calculadora = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init, 100, 200, "Calculadora", self.boton_calculadora, "white", "black")
        self.boton_programador = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + 200 + separacion, 100, 200, "Programador", self.boton_programador, "white",
                                 "black")
        self.boton_volumen = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 2, 100, 200, "Volumen", self.boton_volumen, "white",
                                 "black")
        self.boton_longitud = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3, 100, 200, "Longitud", self.boton_longitud,
                                 "white", "black")
        self.boton_temperatura = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 0, 350, 200, "Temperatura", self.boton_temperatura,
                                 "white", "black")
        self.boton_velocidad = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 1, 350, 200, "Velocidad", self.boton_velocidad,
                                 "white", "black")
        self.boton_tiempo = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 2, 350, 200, "Tiempo", self.boton_tiempo,
                                 "white", "black")
        self.boton_angulo = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3, 350, 200, "Angulo", self.boton_angulo,
                                 "white", "black")

        self.boton_mas = QtWidgets.QPushButton(self.grupo_calculos)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3 + 200, 550, 30, "mas", self.boton_mas,
                                 "white", "black")
        self.boton_mas.setText("")

        self.label_inicial_calc = QtWidgets.QLabel(self.grupo_calculos)
        self.crear_label(10, 10, 400, 50, "¿Que quieres calcular?", self.label_inicial_calc, "white")
        self.label_inicial_calc.setFont(self.set_font(16))

        self.grupo_programador = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_programador",
                            self.grupo_programador, "white")
        self.label_programador = QtWidgets.QLabel(self.grupo_programador)
        self.crear_label(10, 10, 300, 30, "Conversión de bases", self.label_programador, "white")
        self.label_programador.setFont(self.set_font(16))
        self.boton_regresa_2 = QtWidgets.QPushButton(self.grupo_programador)
        self.crear_boton_redondo(390, 60, 30, "flecha izquierda",
                                 self.boton_regresa_2, "white", "black")
        self.boton_regresa_2.setText("")

        self.label_decimal = QtWidgets.QLabel(self.grupo_programador)
        self.crear_label(10, 135, 300, 30, "Decimal", self.label_decimal, "white")
        self.label_binario = QtWidgets.QLabel(self.grupo_programador)
        self.crear_label(10, 135 + 1 * (100 + separacion), 300, 30, "Binario", self.label_binario, "white")
        self.label_octal = QtWidgets.QLabel(self.grupo_programador)
        self.crear_label(10, 135 + 2 * (100 + separacion), 300, 30, "Octal", self.label_octal, "white")
        self.label_hexadecimal = QtWidgets.QLabel(self.grupo_programador)
        self.crear_label(10, 135 + 3 * (100 + separacion), 300, 30, "Hexadecimal", self.label_hexadecimal, "white")

        self.edit_decimal = QtWidgets.QLineEdit(self.grupo_programador)
        self.crear_lineEdit(120, 100, 300, 100, "Decimal", self.edit_decimal)

        self.edit_binario = QtWidgets.QLineEdit(self.grupo_programador)
        self.crear_lineEdit(120, 100 + 1 * (100 + separacion), 300, 100, "Binario", self.edit_binario)

        self.edit_octal = QtWidgets.QLineEdit(self.grupo_programador)
        self.crear_lineEdit(120, 100 + 2 * (100 + separacion), 300, 100, "Octal", self.edit_octal)
        self.edit_hexadecimal = QtWidgets.QLineEdit(self.grupo_programador)
        self.crear_lineEdit(120, 100 + 3 * (100 + separacion), 300, 100, "Hexadecimal", self.edit_hexadecimal)

        self.grupo_conversiones = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, side_menu_width + 200, window_height, "grupo_conversiones",
                            self.grupo_conversiones, "white")

        self.label_conversiones = QtWidgets.QLabel(self.grupo_conversiones)
        self.crear_label(10, 10, 300, 30, "", self.label_conversiones, "white")
        self.label_conversiones.setFont(self.set_font(16))

        self.combobox_select = QtWidgets.QComboBox(self.grupo_conversiones)
        self.crear_combobox(50, 200, 200, 30, "combobox_select", self.combobox_select, "white", " black")

        self.edit_conversion = LineEdit(self.grupo_conversiones)
        # self.edit_conversion = QtWidgets.QLineEdit(self.grupo_conversiones)
        self.crear_lineEdit(50, 50, 200, 150, "Introduce el valor", self.edit_conversion, "edit_conversion")

        self.combobox_select_1 = QtWidgets.QComboBox(self.grupo_conversiones)
        self.crear_combobox(50, 430, 200, 30, "combobox_select", self.combobox_select_1, "white", " black")

        self.edit_conversion_1 = LineEdit(self.grupo_conversiones)
        # self.edit_conversion_1 = QtWidgets.QLineEdit(self.grupo_conversiones)
        self.crear_lineEdit(50, 280, 200, 150, "Introduce el valor", self.edit_conversion_1, "edit_conversion_1")
        self.edit_conversion.setFont(self.set_font(14))
        self.edit_conversion_1.setFont(self.set_font(14))

        self.boton_regresa_1 = QtWidgets.QPushButton(self.grupo_conversiones)
        self.crear_boton_redondo(50, 500, 30, "flecha izquierda",
                                 self.boton_regresa_1, "white", "black")
        self.boton_regresa_1.setText("")

        self.grupo_calculos_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_calculos_1",
                            self.grupo_calculos_1, "white")

        self.label_inicial_calc_1 = QtWidgets.QLabel(self.grupo_calculos_1)
        self.crear_label(10, 10, 400, 50, "¿Que quieres calcular?", self.label_inicial_calc_1, "white")
        self.label_inicial_calc_1.setFont(self.set_font(16))

        self.boton_presion = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init, 100, 200, "Presión", self.boton_presion, "white", "black")
        self.boton_energia = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init + (200 + separacion), 100, 200, "Energía", self.boton_energia, "white",
                                 "black")
        self.boton_fuerza = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 2, 100, 200, "Fuerza", self.boton_fuerza, "white",
                                 "black")
        self.boton_masa = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3, 100, 200, "Masa", self.boton_masa, "white", "black")
        self.boton_graficas = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 0, 350, 200, "Gráficas", self.boton_graficas,
                                 "white", "black")

        self.boton_regresa = QtWidgets.QPushButton(self.grupo_calculos_1)
        self.crear_boton_redondo(pos_init + (200 + separacion) * 3 + 200, 550, 30, "flecha izquierda",
                                 self.boton_regresa,
                                 "white", "black")
        self.boton_regresa.setText("")

        self.grupo_lista_de_materiales = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height,
                            "grupo_lista_de_materiales",
                            self.grupo_lista_de_materiales, "white")
        for i in range(0, 100):
            exec(f"self.grupo_materiales_{i} = QtWidgets.QGroupBox(self.grupo_lista_de_materiales)")
            exec(f"self.boton_materiales_{i} = QtWidgets.QPushButton(self.grupo_materiales_{i})")
            exec(f"self.label_materiales_{i} = QtWidgets.QLabel(self.grupo_materiales_{i})")
        self.crear_cuadro_con_contenido_2(20, 20, 200, 250, 15, 10, 2, 4)

        self.grupo_filtrar = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(38, 0, side_menu_width - 38, window_height,
                            "grupo_filtrar", self.grupo_filtrar, "rgb(74,74,74)")
        self.edit_filtrar = QtWidgets.QLineEdit(self.grupo_filtrar)
        self.crear_lineEdit(5, 15, 147, 30, "Filtrar", self.edit_filtrar)
        self.edit_filtrar.setStyleSheet("border-style: solid; border-width: 2px; color: white")

        self.grupo_componentes = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 270, window_width - side_menu_width, window_height - 270,
                            "grupo_componentes", self.grupo_componentes, "rgb(200,200,200)")
        # self.grupo_componentes.setStyleSheet(f"background-color: white; border-style: solid;border-width: 0.5px; border-radius: 15px")
        self.boton_cerrar_1 = QtWidgets.QPushButton(self.grupo_componentes)
        self.crear_boton_redondo(window_width - side_menu_width - 30, 0, 30, "Cerrar", self.boton_cerrar_1,
                                 "transparent", "black")
        self.boton_cerrar_1.setText("")
        self.combobox_componente = QtWidgets.QComboBox(self.grupo_componentes)
        self.crear_combobox(50, 40, 200, 30, "combobox_componente", self.combobox_componente, "white", "black")
        self.tabla_componentes = QtWidgets.QTableWidget(self.grupo_componentes)
        self.crear_tableWidget(10, 2, "tabla_componentes", 300, 20, 600, 340, self.tabla_componentes)
        self.tabla_componentes.setHorizontalHeaderItem(0, self.define_titulo_columna("Parámetro  "))
        self.tabla_componentes.setHorizontalHeaderItem(1, self.define_titulo_columna("Valor"))

        self.grupo_comentarios = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(window_width - side_menu_width, 0, side_menu_width, window_height,
                            "grupo_comentarios", self.grupo_comentarios, "rgb(74,74,74)")
        self.textedit_comentarios = QtWidgets.QTextEdit(self.grupo_comentarios)
        self.crear_textedit(0, 50, side_menu_width, 300, "Agrega comentarios", self.textedit_comentarios, "transparent",
                            "white")
        self.boton_agrega_comentario = QtWidgets.QPushButton(self.grupo_comentarios)
        self.crear_boton_normal(side_menu_width / 2 - 80, 375, 160, 30, "Agrega comentario",
                                self.boton_agrega_comentario, "transparent", "white", "boton_agrega_comentario")
        self.boton_cerrar = QtWidgets.QPushButton(self.grupo_comentarios)
        self.crear_boton_redondo(side_menu_width - 30, 0, 30, "Cerrar", self.boton_cerrar, "transparent", "black")
        self.boton_cerrar.setText("")

        self.grupo_teclado = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width * 2 + 200, 0, window_width - side_menu_width * 2 - 200, window_height,
                            "grupo_teclado", self.grupo_teclado, "white")
        # self.grid = QtWidgets.QGridLayout(self.grupo_teclado)
        # self.grupo_teclado.setLayout(self.grid)

        for i in range(0, 50):
            exec(f"self.boton_teclado_{i} = QtWidgets.QPushButton(self.grupo_teclado)")
        self.acomodar_grid(20, 50, 150, 80, 2, 2, 5, 3)
        #===============================================================================================================
        self.grupo_calculadora = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height,
                            "grupo_calculadora", self.grupo_calculadora, "white")

        for i in range(0, 50):
            exec(f"self.boton_teclado_calculadora_{i} = QtWidgets.QPushButton(self.grupo_calculadora)")

        self.acomodar_grid_1(250, 300, 80, 40, 10, 10, 6, 6)
        self.combobox_funcionesTrig = QtWidgets.QComboBox(self.grupo_calculadora)
        self.crear_combobox(10, 300, 230, 30, "Combobox_funcionesTrig", self.combobox_funcionesTrig, "white", "black" )
        self.combobox_funcionesHyp = QtWidgets.QComboBox(self.grupo_calculadora)
        self.crear_combobox(10, 340, 230, 30, "Combobox_funcionesHyp", self.combobox_funcionesHyp, "white", "black")
        funcionesTrig = ["Funciones Trigonometricas","sin(x)", "cos(x)", "tan(x)", "csc(x)", "sec(x)", "cot(x)" , "arcsin(x)", "arccos(x)", "arctan(x)"]
        funcionesHyp = ["Funciones Hiperbólicas","sinh(x)", "cosh(x)", "tanh(x)", "csch(x)", "sech(x)", "coth(x)", "arcsinh(x)", "arccosh(x)", "arctanh(x)"]
        self.combobox_funcionesTrig.addItems(funcionesTrig)
        self.combobox_funcionesHyp.addItems(funcionesHyp)


        self.boton_teclado_calculadora_0.setShortcut("Del")
        self.boton_teclado_calculadora_5.setShortcut("M")
        self.boton_teclado_calculadora_11.setShortcut("/")
        self.boton_teclado_calculadora_17.setShortcut("*")
        self.boton_teclado_calculadora_23.setShortcut("-")
        self.boton_teclado_calculadora_29.setShortcut("+")
        self.boton_teclado_calculadora_35.setShortcut("Enter")
        self.boton_teclado_calculadora_14.setShortcut("7")
        self.boton_teclado_calculadora_15.setShortcut("8")
        self.boton_teclado_calculadora_16.setShortcut("9")
        self.boton_teclado_calculadora_20.setShortcut("4")
        self.boton_teclado_calculadora_21.setShortcut("5")
        self.boton_teclado_calculadora_22.setShortcut("6")
        self.boton_teclado_calculadora_26.setShortcut("1")
        self.boton_teclado_calculadora_27.setShortcut("2")
        self.boton_teclado_calculadora_28.setShortcut("3")
        self.boton_teclado_calculadora_33.setShortcut("0")
        self.boton_teclado_calculadora_34.setShortcut(".")
        self.boton_teclado_calculadora_6.setShortcut("Backspace")

        self.edit_calculadora = QtWidgets.QLineEdit(self.grupo_calculadora)
        self.crear_lineEdit(250, 100, 530, 149, "Introduce Número", self.edit_calculadora)
        self.edit_calculadora.setAlignment(QtCore.Qt.AlignRight)
        self.edit_calculadora.setFont(self.set_font(18))
        self.label_calculadora = QtWidgets.QLabel(self.grupo_calculadora)
        self.crear_label(250, 70, 500, 30, "", self.label_calculadora, "white")
        self.label_calculadora.setAlignment(QtCore.Qt.AlignRight)
        self.label_calculadora_inicio = QtWidgets.QLabel(self.grupo_calculadora)
        self.crear_label(10, 10, 300, 50, "Calculadora", self.label_calculadora_inicio, "white")
        self.label_calculadora_inicio.setFont(self.set_font(16))
        # ==============================================================================================================
        self.grupo_graficas = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_graficas",
                            self.grupo_graficas, "white")
        self.label_graficas_inicio = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(10, 10, 300, 50, "Gráficas", self.label_graficas_inicio, "white")
        self.label_graficas_inicio.setFont(self.set_font(16))
        self.label_variable = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(20, 50, 100, 30, "Variable", self.label_variable, "white")
        self.label_expresión = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(20, 90, 300, 30, "Expresión", self.label_expresión, "white")
        self.label_inicio = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(20, 130, 100, 30, "Inicio", self.label_inicio, "white")
        self.label_final = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(20, 170, 100, 30, "Fin", self.label_final, "white")
        self.label_incremento = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(20, 210, 100, 30, "Incremento", self.label_incremento, "white")

        self.edit_variable = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(120, 50, 100, 30, "Variable", self.edit_variable)
        self.edit_variable.setText("x")

        self.checkbox_grid = QtWidgets.QCheckBox(self.grupo_graficas)
        self.crear_checkBox(450, 50, 100, 30, "Grid", self.checkbox_grid, "white")
        self.checkbox_grid.setChecked(True)
        self.edit_titulo = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(600, 50, 250, 30, "Título", self.edit_titulo)
        self.edit_expresion = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(120, 90, 300, 30, "Función", self.edit_expresion)
        self.edit_expresion.setText("(x**3)*sin(x)")
        self.combobox_estiloGrafica = QtWidgets.QComboBox(self.grupo_graficas)
        self.crear_combobox(450, 90, 100, 30, "combobox_estilosgrafica", self.combobox_estiloGrafica, "white", "black")
        self.combobox_estiloGrafica.addItem("plot")
        self.combobox_estiloGrafica.addItem("scatter")
        self.combobox_estiloGrafica.addItem("bar")
        self.combobox_estiloGrafica.addItem("stem")
        self.edit_titulo_x = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(600, 90, 250, 30, "Eje x", self.edit_titulo_x)
        self.edit_inicio = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(120, 130, 100, 30, "Inicio", self.edit_inicio)
        self.edit_inicio.setText("-10")
        self.combobox_marker = QtWidgets.QComboBox(self.grupo_graficas)
        self.crear_combobox(450, 130, 100, 30, "combobox_marker", self.combobox_marker, "white", "black")
        self.combobox_marker.addItem("")
        self.combobox_marker.addItem(",")
        self.combobox_marker.addItem(".")
        self.combobox_marker.addItem("^")
        self.combobox_marker.addItem("+")
        self.combobox_marker.addItem("v")
        self.combobox_marker.addItem("<")
        self.combobox_marker.addItem(">")
        self.combobox_marker.addItem("*")
        self.combobox_marker.addItem("s")
        self.combobox_marker.addItem("p")
        self.combobox_marker.addItem("d")
        self.combobox_marker.addItem("x")
        self.edit_titulo_y = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(600, 130, 250, 30, "Eje y", self.edit_titulo_y)
        self.label_escala_x = QtWidgets.QLabel(self.grupo_graficas)
        self.label_escala_y = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(600, 170, 100, 30, "Escala eje x:", self.label_escala_x, "white")
        self.crear_label(600, 210, 100, 30, "Escala eje y:", self.label_escala_y, "white")
        self.combobox_escala_y = QtWidgets.QComboBox(self.grupo_graficas)
        self.crear_combobox(710, 210, 250, 30, "combobox_escala_y", self.combobox_escala_y, "white", "black")
        self.combobox_escala_x = QtWidgets.QComboBox(self.grupo_graficas)
        self.crear_combobox(710, 170, 250, 30, "combobox_escala_x", self.combobox_escala_x, "white", "black")
        escala = ["linear", "log", "symlog", "logit"]
        self.combobox_escala_x.addItems(escala)
        self.combobox_escala_y.addItems(escala)
        self.edit_final = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(120, 170, 100, 30, "Fin", self.edit_final)
        self.edit_final.setText("10")
        self.combobox_linestyle = QtWidgets.QComboBox(self.grupo_graficas)
        self.crear_combobox(450, 170, 100, 30, "combobox_linestyle", self.combobox_linestyle, "white", "black")
        self.combobox_linestyle.addItem("-")
        self.combobox_linestyle.addItem("--")
        self.combobox_linestyle.addItem("-.")
        self.combobox_linestyle.addItem(":")
        self.combobox_linestyle.addItem("steps")

        self.edit_incremento = QtWidgets.QLineEdit(self.grupo_graficas)
        self.crear_lineEdit(120, 210, 100, 30, "Incremento", self.edit_incremento)
        self.edit_incremento.setText("0.1")
        self.checkbox_concatenar = QtWidgets.QCheckBox(self.grupo_graficas)
        self.crear_checkBox(450, 210, 150, 30, "Concatenar", self.checkbox_concatenar, "white")
        self.checkbox_concatenar.setChecked(False)
        self.checkbox_concatenar.stateChanged.connect(lambda: self.funcion_concatena())

        self.checkbox_nuevaVentana = QtWidgets.QCheckBox(self.grupo_graficas)
        self.crear_checkBox(450, 240, 150, 30, "Ventana nueva", self.checkbox_nuevaVentana, "white")
        self.checkbox_nuevaVentana.setChecked(False)
        #self.checkbox_concatenar.stateChanged.connect(lambda: self.funcion_nuevaVentana())

        self.label_imagen = QtWidgets.QLabel(self.grupo_graficas)
        self.crear_label(600,300, 400, 300, "", self.label_imagen, "white")
        self.label_imagen.setPixmap(QtGui.QPixmap('iconos/función seno.png'))

        self.boton_grafica = QtWidgets.QPushButton(self.grupo_graficas)
        self.crear_boton_normal(20, 250, 250, 30, "Grafica la función", self.boton_grafica, "white", "black",
                                "boton_grafica", "solid")

        self.boton_abrir = QtWidgets.QPushButton(self.grupo_graficas)
        self.crear_boton_normal(20, 290, 250, 30, "Graficar desde archivo .csv", self.boton_abrir, "white", "black",
                                "boton_grafica", "solid")

        self.boton_exportar = QtWidgets.QPushButton(self.grupo_graficas)
        self.crear_boton_normal(125, 590, 250, 30, "Exportar datos a .csv", self.boton_exportar, "white", "black",
                                "boton_exportar", "solid")


        self.abrir = QtWidgets.QFileDialog(self.centralwidget)

        self.mensaje_guarda = QtWidgets.QMessageBox(self.centralwidget)
        self.crear_mensaje("Se guardo el proyecto correctamente", self.mensaje_guarda)

        self.mensaje_error = QtWidgets.QMessageBox(self.centralwidget)
        self.crear_mensaje("Falta información", self.mensaje_error)

        self.tabla_grafica = QtWidgets.QTableWidget(self.grupo_graficas)
        self.crear_tableWidget(0, 2, "tabla_grafica", 20, 340, 500, 230, self.tabla_grafica)

        self.grupo_acerca_de = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 450, window_width - side_menu_width - 300, window_height - 450,
                            "grupo_acerca_de", self.grupo_acerca_de, "rgb(65,105,225)")
        self.label_acerca_de = QtWidgets.QLabel(self.grupo_acerca_de)
        self.crear_label(10, 10, window_width - side_menu_width, window_height - 460,
                         "Acerca de\nGestor de proyectos\nConversiones de unidades, Conversion de bases, Calculadora científica, Gráficas 2D\n2020\nDesarrollado por: Edgar Sáenz Zubía\nEmail: edgar.sz189@gmail.com\nVersión: 1.0",
                         self.label_acerca_de, "transparent", "white")
        # señales:
        self.set_visible(self.grupo_menu)
        self.set_visible(self.grupo_contenido)
        self.cambia_color(self.label_menu)
        self.boton_redondo_2.clicked.connect(lambda: self.cargar_tabla())
        self.boton_redondo_3.clicked.connect(lambda: self.funcion_guardar_como())
        self.boton_exportar.clicked.connect(lambda: self.funcion_exportar())
        self.boton_abrir.clicked.connect(lambda: self.funcion_abrir())
        self.boton_grafica.clicked.connect(lambda: self.crea_lista())
        self.boton_graficas.clicked.connect(lambda: self.funcion_graficas())
        self.boton.clicked.connect(lambda: self.funcion_inicio())
        self.boton_redondo_1.clicked.connect(lambda: self.set_visible(self.grupo_buscar))
        self.boton_redondo_atras.clicked.connect(lambda: self.change_size())  # conecta el boton  con la función
        self.boton_redondo.clicked.connect(
            lambda: self.funcion_nuevo_proyecto())  # conecta el boton  con la función
        self.boton_hecho.clicked.connect(lambda: self.hecho(self.edit_label_direccion.text()))
        self.boton_menu.clicked.connect(lambda: self.funcion_proyecto_actual())
        self.boton_menu_1.clicked.connect(lambda: self.funcion_lista_materiales())
        self.boton_expandir.clicked.connect(lambda: self.ocultar())
        self.boton_menu_2.clicked.connect(lambda: self.funcion_calculos())
        self.boton_programador.clicked.connect(lambda: self.funcion_programador())
        self.boton_temperatura.clicked.connect(lambda: self.funcion_temperatura())
        self.edit_decimal.textEdited.connect(lambda: self.convierte(self.edit_decimal))
        self.edit_binario.textEdited.connect(lambda: self.convierte(self.edit_binario))
        self.edit_octal.textEdited.connect(lambda: self.convierte(self.edit_octal))
        self.edit_hexadecimal.textEdited.connect(lambda: self.convierte(self.edit_hexadecimal))
        self.boton_menu_4.clicked.connect(lambda: self.funcion_acerca_de())
        self.boton_regresa_2.clicked.connect(lambda: self.set_visible(self.grupo_calculos))
        self.edit_conversion.textEdited.connect(
            lambda: self.convierte_unidades(self.edit_conversion.text(), self.combobox_select.currentText(),
                                            self.combobox_select_1.currentText(), self.edit_conversion,
                                            self.matriz_tipo, self.lista_tipo))
        self.edit_conversion_1.textEdited.connect(
            lambda: self.convierte_unidades(self.edit_conversion_1.text(), self.combobox_select_1.currentText(),
                                            self.combobox_select.currentText(), self.edit_conversion_1,
                                            self.matriz_tipo, self.lista_tipo))
        self.combobox_select.activated.connect(
            lambda: self.convierte_unidades(self.edit_conversion_1.text(), self.combobox_select_1.currentText(),
                                            self.combobox_select.currentText(), self.edit_conversion_1,
                                            self.matriz_tipo, self.lista_tipo))
        self.combobox_select_1.activated.connect(
            lambda: self.convierte_unidades(self.edit_conversion.text(), self.combobox_select.currentText(),
                                            self.combobox_select_1.currentText(), self.edit_conversion,
                                            self.matriz_tipo, self.lista_tipo))
        self.combobox_componente.activated.connect(lambda: self.funcion_caracteristicas())
        self.combobox_funcionesTrig.activated.connect(lambda: self.funcion_calculoTrig())
        self.combobox_funcionesHyp.activated.connect(lambda: self.funcion_calculoHyp())
        self.boton_mas.clicked.connect(lambda: self.set_visible(self.grupo_calculos_1))
        self.boton_regresa.clicked.connect(lambda: self.set_visible(self.grupo_calculos))
        self.boton_regresa_1.clicked.connect(lambda: self.set_visible(self.grupo_calculos))
        self.boton_volumen.clicked.connect(lambda: self.funcion_volumen())
        self.boton_tiempo.clicked.connect(lambda: self.funcion_tiempo())
        self.boton_longitud.clicked.connect(lambda: self.funcion_longitud())
        self.boton_energia.clicked.connect(lambda: self.funcion_energia())
        self.boton_presion.clicked.connect(lambda: self.funcion_presion())
        self.boton_fuerza.clicked.connect(lambda: self.funcion_fuerza())
        self.boton_masa.clicked.connect(lambda: self.funcion_masa())
        self.boton_angulo.clicked.connect(lambda: self.funcion_angulo())
        self.boton_velocidad.clicked.connect(lambda: self.funcion_velocidad())
        self.boton_calculadora.clicked.connect(lambda: self.funcion_calculadora())

        self.boton_agregar_fila.clicked.connect(lambda: self.agrega_fila())
        self.boton_remover_fila.clicked.connect(lambda: self.remueve_fila())

        self.boton_cerrar.clicked.connect(lambda: self.funcion_comentarios())
        self.boton_cerrar_1.clicked.connect(lambda: self.funcion_cerrar_componentes())
        self.boton_agrega_comentario.clicked.connect(lambda: self.funcion_agrega_comentario())

        self.edit_filtrar.textEdited.connect(lambda: self.funcion_buscar_seccion())

        self.calendario.activated.connect(lambda: self.funcion_calendario())
        self.tabla_proyecto.cellClicked.connect(lambda: self.funcion_ver_calendario())
        self.tabla_proyecto.cellClicked.connect(lambda: self.funcion_ver_calendario())

        self.boton_teclado_14.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_13.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_12.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_11.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_10.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_9.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_8.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_7.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_6.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_5.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_4.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_3.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_1.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_0.clicked.connect(lambda: self.funcion_teclado())
        self.boton_teclado_calculadora_35.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_34.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_33.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_32.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_31.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_30.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_29.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_28.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_27.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_26.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_25.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_24.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_23.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_22.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_21.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_20.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_19.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_18.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_17.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_16.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_15.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_14.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_13.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_12.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_11.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_10.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_9.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_8.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_7.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_6.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_5.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_4.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_3.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_2.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_1.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.boton_teclado_calculadora_0.clicked.connect(lambda: self.funcion_teclado_calculadora())
        self.edit_calculadora.textChanged.connect(lambda: self.funcion_verifica())
        self.boton_materiales_0.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_1.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_2.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_3.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_4.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_5.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_6.clicked.connect(lambda: self.funcion_leer_componente("reguladores de voltaje"))
        self.boton_materiales_7.clicked.connect(lambda: self.funcion_resistencias())
        self.boton_estadisticas.clicked.connect(lambda: self.calcular_tiempo_transcurrido())

        self.boton_guardar_proyectoactual.clicked.connect(lambda: self.funcion_guardar_tabla(self.direccion_actual))
        self.boton_abajo.clicked.connect(lambda: self.funcion_mover_fila())
        self.boton_arriba.clicked.connect(lambda: self.funcion_mover_fila())
        self.edit_conversion.focus_in_signal.connect(lambda: self.funcion_focus())
        self.edit_conversion_1.focus_in_signal.connect(lambda: self.funcion_focus())

        self.retranslateUi(MainWindow)

    # QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def calcular_tiempo_transcurrido(self):
        duracion_actividad = []
        actividades = []
        for i in range(self.tabla_proyecto.rowCount()):
            hora_inicio = self.leer_item(i, 5, self.tabla_proyecto)
            hora_final = self.leer_item(i, 6, self.tabla_proyecto)
            lista_hora_inicio = hora_inicio.split(":")
            lista_hora_final = hora_final.split(":")
            print(lista_hora_final)
            h_transcurridas = int(lista_hora_final[0]) - int(lista_hora_inicio[0])
            inicio = int(lista_hora_inicio[0])*60*60 + int(lista_hora_inicio[1])*60 + int(lista_hora_inicio[2])
            final = int(lista_hora_final[0]) * 60 * 60 + int(lista_hora_final[1]) * 60 + int(lista_hora_final[2])


            # guardar los datos calculados en una lista y calcular los segundos trascurridos:
            duracion_actividad.append(final - inicio)
            # extraer actividades:
            actividades.append(self.leer_item(i, 0, self.tabla_proyecto))
        print(duracion_actividad)
        self.graficar_pie_chart(duracion_actividad, actividades)
    def graficar_pie_chart(self, sizes, labels):
        #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', "hey"
        #sizes = [15, 30, 45, 10, 100]
        #explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = pt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        pt.show()
    def crear_mensaje(self, texto, nombre_objeto):
        nombre_objeto.setIcon(QtWidgets.QMessageBox.Information)
        nombre_objeto.setText(texto)
        #self.mensaje_guarda.setInformativeText("This is additional information")
        nombre_objeto.setWindowTitle("Gestor de proyectos")
        #self.mensaje_guarda.setDetailedText("The details are as follows:")
        nombre_objeto.setStandardButtons(QtWidgets.QMessageBox.Ok )
        nombre_objeto.setFont(self.set_font())

    def muestra_mensaje(self):
        self.mensaje_guarda.exec_()

    def funcion_guardar_como(self):
        sender = self.sender()
        archivo = self.abrir.getSaveFileName(self, 'Guardar proyecto', "", "CSV files (*.csv)")  # obtendra la dirección y el nombre del archivo

        if archivo[0] != "":
            self.direccion_actual = archivo[0]
            self.funcion_guardar_tabla(self.direccion_actual)          # le paso la direccion del archivo
            if sender.text() == "":
                self.edit_label_direccion.setText(archivo[0])

    def funcion_guardar_tabla(self, archivo):
        # recorrer toda la tabla:
        tabla = []
        lista_items = []
        r = self.tabla_proyecto.rowCount()
        c = self.tabla_proyecto.columnCount()

        for i in range(r):
            for j in range(c):
                lista_items.append(self.leer_item(i,j,self.tabla_proyecto))
            tabla.append(lista_items)
            lista_items = []

        # guardar estado actuales de botones:
        for i in range(r):
            exec(f"self.estado = self.boton_estado_{i}.text()")
            tabla[i][4] = self.estado
        # guardar comentarios:

        # guarda en un archivo CSV:
        with open(archivo, "w") as data:
            for i in range(r):
                for j in range(c):
                    data.writelines(tabla[i][j])
                    if j < c-1:
                        data.writelines(",")
                    else:
                        data.writelines("\n")
        self.muestra_mensaje()
    def cargar_tabla(self):
        #Seleccionar dinamicamente el archivo a cargar:
        archivo = self.abrir.getOpenFileName(self, 'Selecciona proyecto', "", "All files (*)")

        if archivo[0] != '':
            self.direccion_actual = archivo[0]
            informacion = archivo[0][: -4] + "_info.csv"
            with open(informacion, "r") as info:
                label = info.readlines()
                self.label_proyectoactual.setText("Proyecto actual: " + label[1].strip())
            #leer archivo:
            with open(archivo[0], "r") as data:
                tabla = data.readlines()
                if tabla != []:
                    size = len(tabla)
                    lista_estados = []
                    lista_colores = []
                    self.tabla_proyecto.setRowCount(size)
                    for r, i in enumerate(tabla):
                        row_data = i.split(",")
                        for c, j in enumerate(row_data):
                            self.poblar_tabla(r, c, j.strip(), self.tabla_proyecto)     # rellena tabla con items
                            if c == 4:
                                lista_estados.append(j)
                                if j == "Hecho":
                                    lista_colores.append("green")
                                elif j == "En curso":
                                    lista_colores.append("yellow")
                                elif j == "Pendiente":
                                    lista_colores.append("red")
                #Rellenar tabla con los botones (comentarios y estado):
                #crear los botones:
                    self.crear_botones(0, size)
                    for i in range(size):
                        exec(
                            f"self.crear_boton_normal(0, 0, 16,16, lista_estados[i], self.boton_estado_{i} , lista_colores[i], 'black', 'boton_estado_{i}')")
                        exec(
                            f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{i} , 'white', 'black', 'boton_comentario_{i}')")
                        exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                        exec(f"self.tabla_proyecto.setCellWidget({i} , 3, self.boton_comentario_{i})")
                        exec(f"self.boton_comentario_{i}.setText('')")
                    # calcular progreso:
                    self.verificar_estado()
                    self.boton_menu.setEnabled(True)      # habilito boton
                    self.funcion_proyecto_actual()
                else:
                    self.boton_menu.setEnabled(True)  # habilito boton
                    self.funcion_proyecto_actual()

    def leer_item(self, row, column, tabla):
        if tabla.item(row, column) != None:
            return tabla.item(row, column).text().strip()
        else:
            return ""

    def funcion_exportar(self):
        archivo = self.abrir.getSaveFileName(self, 'Guardar valores', "","CSV files (*.csv)")  # obtendra la dirección y el nombre del archivo
        if archivo[0] != "":
            with open(archivo[0], "w") as data:
                size = self.tabla_grafica.rowCount()
                print(size)
                for i in range(size):
                    value_x = self.leer_item(i, 0, self.tabla_grafica)
                    value_y = self.leer_item(i, 1, self.tabla_grafica)
                    data.writelines(value_x)
                    data.writelines(",")
                    data.writelines(value_y + "\n")

    def funcion_concatena(self):
        # self.edit_expresion.clear()
        self.edit_expresion.setFocus()

    def funcion_abrir(self):
        archivo = self.abrir.getOpenFileName(self, 'Selecciona datos a graficar', "",  "CSV files (*.csv)")
        if archivo[0] != '':
            with open(archivo[0], 'r') as data:
                valores = data.readlines()
                size = len(valores)
                self.tabla_grafica.clearContents()
                self.tabla_grafica.setRowCount(size)
                r = 0
                x = []
                y = []
                for i in valores:
                    valores_1 = i.split(",")
                    self.poblar_tabla(r, 0, valores_1[0].strip(), self.tabla_grafica)
                    x.append(float(valores_1[0].strip()))
                    self.poblar_tabla(r, 1, valores_1[1].strip(), self.tabla_grafica)
                    y.append(float(valores_1[1].strip()))
                    r += 1

                pt.plot(x, y)
                pt.grid(True)
                pt.show()

    def funcion_graficas(self):
        self.cambia_color(self.label_menu_3)
        self.set_visible(self.grupo_graficas)

    def crea_lista(self):
        try:
            x_1 = []
            y_1 = []
            run = True

            if self.edit_inicio.text().strip() == "pi":
                inicio = pi
            elif self.edit_inicio.text().strip() == "-pi":
                inicio = -pi
            else:
                inicio = float(self.edit_inicio.text().strip())
            numero = inicio
            if self.edit_final.text().strip() == "pi":
                fin = pi
            elif self.edit_final.text().strip() == "-pi":
                fin: -pi
            else:
                fin = float(self.edit_final.text().strip())
            if self.edit_incremento.text().strip() == "pi":
                incremento = pi
            else:
                incremento = float(self.edit_incremento.text().strip())
            while run:
                x_1.append(numero)
                numero +=  incremento
                if numero >= fin:
                    x_1.append(numero)
                    run = False

            expresion = self.edit_expresion.text().strip()
            variable = self.edit_variable.text().strip()
            r = 0
            size = len(x_1)
            self.tabla_grafica.clearContents()
            self.tabla_grafica.setRowCount(size)
            for globals()[variable] in x_1:
                self.y = eval(f"{expresion}")
                y_1.append(self.y)
                self.poblar_tabla(r, 0, str(globals()[variable]), self.tabla_grafica)
                self.poblar_tabla(r, 1, str(self.y), self.tabla_grafica)
                r += 1

            self.tabla_grafica.resizeColumnsToContents()
            self.tabla_grafica.setHorizontalHeaderItem(0, self.define_titulo_columna(variable))
            self.tabla_grafica.setHorizontalHeaderItem(1, self.define_titulo_columna("f(" + variable + ")"))
            # pt.plot(x_1,y_1)
            estilo = self.combobox_estiloGrafica.currentText()
            marker = self.combobox_marker.currentText()
            linestyle = self.combobox_linestyle.currentText()
            self.lista_parametros_3.append(estilo)

            if self.checkbox_concatenar.isChecked() == False:
                pt.close()
                exec(f"pt.{estilo}(x_1,y_1, marker= '{marker}', linestyle = '{linestyle}')")
                pt.title(self.edit_titulo.text())
                pt.xlabel(self.edit_titulo_x.text())
                pt.ylabel(self.edit_titulo_y.text())
                pt.grid(self.checkbox_grid.isChecked())
                pt.yscale(self.combobox_escala_y.currentText())
                pt.xscale(self.combobox_escala_x.currentText())
                #pt.legend("Hola",loc='upper right')
                pt.show()
            else:
                if pt.fignum_exists(1):
                    exec(f"pt.{estilo}(x_1,y_1, marker= '{marker}', linestyle = '{linestyle}')")
                    pt.draw()
                else:
                    exec(f"pt.{estilo}(x_1,y_1, marker= '{marker}', linestyle = '{linestyle}')")
                    pt.title(self.edit_titulo.text())
                    pt.xlabel(self.edit_titulo_x.text())
                    pt.ylabel(self.edit_titulo_y.text())
                    pt.grid(self.checkbox_grid.isChecked())
                    pt.yscale(self.combobox_escala_y.currentText())
                    pt.xscale(self.combobox_escala_x.currentText())
                    pt.show()

        except:
            print("error")  # abrir un mensaje que diga: error de sintaxis

    def verificar_estado(self):
        count = 0
        row_count = self.tabla_proyecto.rowCount()
        for i in range(row_count):
            exec(f"self.estado = self.boton_estado_{i}.text()")
            if self.estado == "Hecho":
                count += 1
        valor = (count / row_count) * 100
        self.progressbar_1.setValue(valor)
        if valor == 100:
            self.boton_estadisticas.setEnabled(True)
        else:
            self.boton_estadisticas.setEnabled(False)
    def funcion_programador(self):
        self.set_visible(self.grupo_programador)
        self.cambia_color(self.label_menu_3)

    def funcion_calculadora(self):
        self.set_visible(self.grupo_calculadora)

    def funcion_buscar(self):
        self.set_visible(self.grupo_buscar)

    def funcion_nuevo_proyecto(self):
        self.set_visible(self.grupo_nuevo_proyecto)

    def funcion_buscar_seccion(self):
        texto = self.edit_filtrar.text()
        size = len(texto)

        try:
            for i in self.lista_secciones:
                if i[0:size].lower().strip() == texto.lower().strip():
                    grupo = i.lower().strip()
                    print(grupo)
                    # self.funcion_masa()
                    exec(f"self.funcion_{grupo}()")
                    break
        except:
            print("No existe esa sección")

    def funcion_acerca_de(self):
        if self.grupo_acerca_de.isVisible():
            self.grupo_acerca_de.setVisible(False)
        else:
            self.grupo_acerca_de.setVisible(True)

    def funcion_cerrar_componentes(self):
        if self.grupo_componentes.isVisible():
            self.grupo_componentes.setVisible(False)
        else:
            self.grupo_componentes.setVisible(True)

    def funcion_caracteristicas(self):
        index = self.combobox_componente.currentIndex()

        with open(f"archivos/{self.componente}.csv", "r") as data:
            lista_componentes = data.readlines()  # lee las lineas que haya en el documento

            caracteristicas = lista_componentes[index + 1].split(",")
            size = len(caracteristicas)
            print(size)
            for i in range(self.tabla_componentes.rowCount()):
                self.poblar_tabla(i, 1, caracteristicas[i + 1], self.tabla_componentes)
            self.tabla_componentes.resizeColumnsToContents()

    def funcion_leer_componente(self, componente):
        self.grupo_componentes.setVisible(True)
        self.combobox_componente.clear()
        self.componente = componente
        with open(f"archivos/{self.componente}.csv", "r") as data:
            self.tabla_componentes.clearContents()
            self.tabla_componentes.setColumnCount(2)
            lista_componentes = data.readlines()                    # lee las lineas que haya en el documento
            fila = lista_componentes[0].split(",")
            rowcount = len(fila) -1
            self.tabla_componentes.setRowCount(rowcount)
            r = 0
            for j in fila[1:]:
                self.poblar_tabla(r, 0, j, self.tabla_componentes)  # coloco los parametros en la tabla
                r += 1
            r = 0
            for i in lista_componentes[1:]:
                componente = i.split(",")
                self.combobox_componente.addItem(componente[0])     # Añado los componentes al combobox
            self.funcion_caracteristicas()

    def funcion_resistencias(self):
        self.grupo_componentes.setVisible(True)
        with open("archivos/resistencias.csv", "r") as data:
            lista_componentes = data.readlines()                    # lee las lineas que haya en el documento
            self.tabla_componentes.clearContents()
            self.tabla_componentes.setColumnCount(1)
            size = len(lista_componentes)
            self.tabla_componentes.setRowCount(size)
            r = 0
            for i in lista_componentes:
                self.poblar_tabla(r, 0, i.strip(), self.tabla_componentes)
                r += 1



    def funcion_verifica(self):
        try:
            flag = False
            numero = self.edit_calculadora.text()
            if numero[-1] == "(":
                self.label_calculadora.setText(self.label_calculadora.text() + numero)
            elif numero[-1] == ")":
                self.label_calculadora.setText(self.label_calculadora.text() + numero)
            else:
                for i in numero:
                    if i == ".":
                        flag = True
                        break
                if flag:
                    num = float(numero)
                else:
                    num = int(numero)
                return num
        except:
            self.edit_calculadora.setText(self.edit_calculadora.text()[0:-1])
    def funcion_calculoTrig(self):
        sender = self.sender()
        try:
            num = self.funcion_verifica()
            if sender.currentText() == "sin(x)":
                valor = np.sin(num)
                self.label_calculadora.setText(f"sin({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "cos(x)":
                valor = np.cos(num)
                self.label_calculadora.setText(f"cos({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "tan(x)":
                valor = np.tan(num)
                self.label_calculadora.setText(f"tan({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "csc(x)":
                valor = 1/(np.sin(num))
                self.label_calculadora.setText(f"csc({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "sec(x)":
                valor = 1/(np.cos(float(self.edit_calculadora.text())))
                self.label_calculadora.setText(f"sec({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "cot(x)":
                valor = 1/(np.tan(float(self.edit_calculadora.text())))
                self.label_calculadora.setText(f"cot({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arcsin(x)":
                valor = np.arcsin(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arcsin({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arccos(x)":
                valor = np.arccos(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arccos({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arctan(x)":
                valor = np.arctan(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arctan({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))

            self.combobox_funcionesTrig.setCurrentIndex(0)
        except:
            self.combobox_funcionesTrig.setCurrentIndex(0)

    def funcion_calculoHyp(self):
        sender = self.sender()
        try:
            if sender.currentText() == "sinh(x)":
                valor = np.sinh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"sinh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "cosh(x)":
                valor = np.cosh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"cosh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "tanh(x)":
                valor = np.tanh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"tanh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "csch(x)":
                valor = 1/(np.sinh(float(self.edit_calculadora.text())))
                self.label_calculadora.setText(f"csch({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "sech(x)":
                valor = 1/(np.cosh(float(self.edit_calculadora.text())))
                self.label_calculadora.setText(f"sech({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "coth(x)":
                valor = 1/(np.tanh(float(self.edit_calculadora.text())))
                self.label_calculadora.setText(f"coth({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arcsinh(x)":
                valor = np.arcsinh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arcsinh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arccosh(x)":
                valor = np.arccosh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arccosh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.currentText() == "arctanh(x)":
                valor = np.arctanh(float(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"arctanh({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))

            self.combobox_funcionesHyp.setCurrentIndex(0)
        except:
            self.combobox_funcionesHyp.setCurrentIndex(0)


    def funcion_teclado_calculadora(self):
        sender = self.sender()

        #self.combobox_funcionesTrig.currentText()
        try:
            num = self.funcion_verifica()
            if sender.text() == "x^2":
                valor = num ** 2
                self.label_calculadora.setText(f"{self.edit_calculadora.text()}^2")
                self.edit_calculadora.setText(str(valor))
            elif sender.text().isnumeric():
                if self.label_calculadora.text() == "":
                    texto_actual = self.edit_calculadora.text()
                    self.edit_calculadora.setText(texto_actual + sender.text())
                else:
                    if self.operacion == None:
                        self.edit_calculadora.clear()
                        self.label_calculadora.setText("")
                        self.edit_calculadora.setText(sender.text())
                    else:
                        texto_actual = self.edit_calculadora.text()
                        self.edit_calculadora.setText(texto_actual + sender.text())
            elif sender.text() == "|x|":
                valor = abs(num)
                self.label_calculadora.setText(f"abs({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "n!":

                valor = self.factorial(int(self.edit_calculadora.text()))
                self.label_calculadora.setText(f"factorial({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "%":
                valor = num * (1e-2)
                self.label_calculadora.setText(f"{self.edit_calculadora.text()}%")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "<--":

                self.edit_calculadora.setText(self.edit_calculadora.text()[0:-1])
            elif sender.text() == "mod":
                self.operacion = sender.text()
                self.valor = num
                self.label_calculadora.setText(f"{self.edit_calculadora.text()} mod")
                self.edit_calculadora.clear()
            elif sender.text() == "÷":
                self.operacion = sender.text()
                self.valor = num
                self.label_calculadora.setText(f"{self.edit_calculadora.text()} ÷")
                self.edit_calculadora.clear()
            elif sender.text() == "x":
                self.operacion = sender.text()
                self.valor = num
                self.label_calculadora.setText(f"{self.edit_calculadora.text()} x")
                self.edit_calculadora.clear()

            elif sender.text() == "-":
                self.operacion = sender.text()
                self.valor = num
                self.label_calculadora.setText(f"{self.edit_calculadora.text()} -")
                self.edit_calculadora.clear()
            elif sender.text() == "+":
                self.operacion = sender.text()
                self.valor = num
                self.label_calculadora.setText(f"{self.edit_calculadora.text()} +")
                self.edit_calculadora.clear()

            elif sender.text() == "=":
                if self.operacion == "x":
                    numero = self.funcion_verifica()
                    resultado = self.valor * numero

                elif self.operacion == "+":
                    numero = self.funcion_verifica()
                    resultado = self.valor + numero
                elif self.operacion == "-":
                    numero = self.funcion_verifica()
                    resultado = self.valor - numero
                elif self.operacion == "mod":
                    numero = self.funcion_verifica()
                    resultado = self.valor % numero
                elif self.operacion == "÷":
                    numero = self.funcion_verifica()
                    resultado = self.valor / numero

                else:
                    self.operacion = None

                self.edit_calculadora.setText(str(resultado))
                texto_actual = self.label_calculadora.text()
                self.label_calculadora.setText(texto_actual + " " + str(numero))

                self.operacion = None


            elif sender.text() == "+/-":
                valor = num * (-1)
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "π":
                valor = np.pi
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "e":
                valor = np.exp(1)
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "floor":
                valor = np.floor(num)
                self.label_calculadora.setText(f"floor({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "ceil":
                valor = np.ceil(num)
                self.label_calculadora.setText(f"ceil({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "√":
                valor = np.sqrt(num)
                self.label_calculadora.setText(f"sqrt({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "x^3":
                valor = num ** 3
                self.label_calculadora.setText(f"{self.edit_calculadora.text()}^3")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "C":
                self.edit_calculadora.clear()
                self.label_calculadora.setText("")
            elif sender.text() == "ln":
                valor = np.log(num)
                self.label_calculadora.setText(f"ln({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "log":
                valor = np.log10(num)
                self.label_calculadora.setText(f"log({self.edit_calculadora.text()})")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "10^x":
                valor = 10 ** num
                self.label_calculadora.setText(f"10^{self.edit_calculadora.text()}")
                self.edit_calculadora.setText(str(valor))
            elif sender.text() == "1/x":
                valor = 1 / num
                self.label_calculadora.setText(f"1/{self.edit_calculadora.text()}")
                self.edit_calculadora.setText(str(valor))
            else:
                texto_actual = self.edit_calculadora.text()
                self.edit_calculadora.setText(texto_actual + sender.text())
                self.edit_calculadora.setFocus()
            # self.edit_calculadora.setFocus()
        except:
            pass

    def factorial(self, numero):
        for i in range(1, numero):
            numero = numero * i
        return numero

    def funcion_focus(self):
        sender = self.sender()
        if sender.objectName() == "edit_conversion":
            self.flag_conversion = 0
        else:
            self.flag_conversion = 1

    def funcion_teclado(self):
        sender = self.sender()
        if sender.text() == "Clear":
            self.edit_conversion.clear()
            self.edit_conversion_1.clear()

        else:

            if self.flag_conversion == 0:
                active = self.edit_conversion
                combobox_active = self.combobox_select
                combobox_not_active = self.combobox_select_1
            elif self.flag_conversion == 1:
                active = self.edit_conversion_1
                combobox_active = self.combobox_select_1
                combobox_not_active = self.combobox_select
            if sender.text() == "<--":
                active.setText(active.text()[0:-1])
                self.convierte_unidades(active.text(), combobox_active.currentText(),
                                        combobox_not_active.currentText(), active,
                                        self.matriz_tipo, self.lista_tipo)
            else:
                texto_actual = active.text()
                active.setText(texto_actual + sender.text())

                self.convierte_unidades(active.text(), combobox_active.currentText(),
                                        combobox_not_active.currentText(), active,
                                        self.matriz_tipo, self.lista_tipo)
            active.setFocus()

    def acomodar_grid_1(self, initx, inity, w, h, seperacion_h, separacion_v, row_count, column_count):

        count = 0
        for r in range(row_count):
            for c in range(column_count):
                # if self.names[count] == "":
                #     continue
                exec(
                    f"self.crear_boton_normal(initx + (w + seperacion_h)*c, inity + (h + separacion_v)*r, w, h, '{self.botones_calculadora[count]}', self.boton_teclado_calculadora_{count}, 'white', 'black', 'boton_teclado_calculadora_{count}', 'solid')")
                count += 1

    def acomodar_grid(self, initx, inity, w, h, seperacion_h, separacion_v, row_count, column_count):
        num_elementos = row_count * column_count
        count = 0
        for r in range(row_count):
            for c in range(column_count):
                # if self.names[count] == "":
                #     continue
                exec(
                    f"self.crear_boton_normal(initx + (w + seperacion_h)*c, inity + (h + separacion_v)*r, w, h, '{self.names[count]}', self.boton_teclado_{count}, 'white', 'black', 'boton_teclado_{count}', 'solid')")
                count += 1

    def poblar_tabla(self, row, column, text, nombre_tabla):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        nombre_tabla.setItem(row, column, item)

    def funcion_ver_calendario(self):
        if self.tabla_proyecto.currentColumn() == 1 or self.tabla_proyecto.currentColumn() == 2:
            self.calendario.setVisible(True)
        else:
            self.calendario.setVisible(False)

    def funcion_calendario(self):

        if self.tabla_proyecto.currentColumn() == 1 or self.tabla_proyecto.currentColumn() == 2:
            fila = self.tabla_proyecto.currentRow()
            columna = self.tabla_proyecto.currentColumn()

            dia = str(self.calendario.selectedDate().day())
            mes = str(self.calendario.selectedDate().month())
            year = str(self.calendario.selectedDate().year())

            self.poblar_tabla(fila, columna, dia + "/" + mes + "/" + year, self.tabla_proyecto)

    def funcion_comentarios(self):
        if self.grupo_comentarios.isVisible():
            self.grupo_comentarios.setVisible(False)
        else:
            self.grupo_comentarios.setVisible(True)
            self.textedit_comentarios.setFocus()
            # crear un documento de comentarios si no existe uno:
            direccion = self.direccion_actual[: -4] + "_comentarios.csv"
            open(direccion , "a")
            self.sender_val = self.sender()
            for i in range(0, 100):
                if self.sender_val.objectName() == "boton_comentario_" + str(i):
                    with open(direccion, "r") as com:
                        comentarios_lista = com.readlines()
                        for j in comentarios_lista:
                            comentario_individual = j.split(",")
                            if comentario_individual[0] == str(i):
                                self.textedit_comentarios.setText(comentario_individual[1])
                                break
                            else:
                                self.textedit_comentarios.setText("")

                    break

    def funcion_agrega_comentario(self):
        flag = False
        for i in range(0, 100):
            if self.sender_val.objectName() == "boton_comentario_" + str(i):
                exec(f"self.coloca_icono('Comentarios', self.boton_comentario_{i})")
                if self.textedit_comentarios.toPlainText() == "":
                    pass  # Agregar mensaje diciendo que necesita agregar texto
                else:
                    direccion = self.direccion_actual[: -4] + "_comentarios.csv"
                    with open(direccion, "r") as com:
                        comentarios_lista = com.readlines()
                        for index, j in enumerate(comentarios_lista):
                            comentario_individual = j.split(",")
                            if comentario_individual[0] == str(i):  # Si ya esta presente...
                                comentario_individual[1] = self.textedit_comentarios.toPlainText()
                                comentarios_lista[index] = ",".join(
                                    comentario_individual)  # sobre escribo ese comentario
                                flag = True
                                com.close()
                                break
                    if flag:
                        with open(direccion, "w") as com:
                            com.writelines(comentarios_lista)
                    else:
                        with open(direccion, mode="+a") as com:
                            com.writelines(str(i) + "," + self.textedit_comentarios.toPlainText() + "\n")

                break
        self.funcion_comentarios()



    def funcion_estado(self):
        sender = self.sender()
        for i in range(0, 100):
            if sender.objectName() == "boton_estado_" + str(i):
                print(sender.objectName())
                if sender.text() == "En curso":
                    self.crear_botones(i, i + 1)  # Creo botones
                    exec(f"self.crear_boton_normal(0, 0, 16,16, 'Hecho' ,self.boton_estado_{i} , 'green', 'black', 'boton_estado_{i}')")
                    exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                    # exec(f"self.boton_estado_{i}.setText('Hecho')")
                    # exec(f"self.boton_estado_{i}.setStyleSheet('background-color: green; border-radius: 10px')")
                    now = datetime.now()
                    hora = str(now.hour)
                    minuto = str(now.minute)
                    segundo = str(now.second)
                    dia = str(now.day)
                    mes = str(now.month)
                    year = str(now.year)
                    self.poblar_tabla(i, 6, hora + ":" + minuto + ":" + segundo, self.tabla_proyecto)
                    self.poblar_tabla(i, 2, dia + "/" + mes + "/" + year, self.tabla_proyecto)
                    break
                elif sender.text() == "Hecho":
                    self.crear_botones(i, i + 1)  # Creo botones
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Pendiente' ,self.boton_estado_{i} , 'red', 'black', 'boton_estado_{i}')")
                    exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                    # exec(f"self.boton_estado_{i}.setText('Pendiente')")
                    # exec(f"self.boton_estado_{i}.setStyleSheet('background-color: red; border-radius: 10px')")

                    break
                elif sender.text() == "Pendiente":
                    self.crear_botones(i, i + 1)  # Creo botones
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'En curso' ,self.boton_estado_{i} , 'yellow', 'black', 'boton_estado_{i}')")
                    exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                    # exec(f"self.boton_estado_{i}.setText('En curso')")
                    # exec(f"self.boton_estado_{i}.setStyleSheet('background-color: yellow; border-radius: 10px')")
                    now = datetime.now()
                    hora = str(now.hour)
                    minuto = str(now.minute)
                    segundo = str(now.second)
                    dia = str(now.day)
                    mes = str(now.month)
                    year = str(now.year)

                    self.poblar_tabla(i, 1, dia + "/" + mes + "/" + year, self.tabla_proyecto)
                    self.poblar_tabla(i, 5, hora + ":" + minuto + ":" + segundo, self.tabla_proyecto)
                    break
        self.verificar_estado()

    def cambia_color(self, nombre_objeto):
        self.label_menu.setStyleSheet("background-color: black; border-radius: 3px")
        self.label_menu_1.setStyleSheet("background-color: black; border-radius: 3px")
        self.label_menu_2.setStyleSheet("background-color: black; border-radius: 3px")
        self.label_menu_3.setStyleSheet("background-color: black; border-radius: 3px")
        self.label_menu_4.setStyleSheet("background-color: black; border-radius: 3px")
        nombre_objeto.setStyleSheet("background-color: white; border-radius: 3px")
    def recorre_num_comentario(self, init, dir):
        flag = False
        direccion = self.direccion_actual[:-4] + "_comentarios.csv"
        try:
            with open(direccion, "r") as com:
                lista_comentarios = com.readlines()

                for i, valor in enumerate(lista_comentarios):
                    comentario = valor.split(",")
                    if dir == 1:                                                     # si se mueve hacia abajo...
                        if int(comentario[0]) >= init:
                            lista_comentarios[i] = str(int(comentario[0]) +1) + "," + comentario[1]  # Sobreescribe
                            flag = True

                    else:

                        if int(comentario[0]) >= init:  # si se mueve hacia abajo...
                            init += 1
                            lista_comentarios[i] = str(int(comentario[0]) -1) + "," + comentario[1]  # Sobreescribe
                            flag = True
            if flag:
                with open(direccion, "w") as com:
                    com.writelines(lista_comentarios)
        except:
            pass
    def remueve_comentario(self, fila):
        flag = False
        direccion = self.direccion_actual[:-4] + "_comentarios.csv"
        try:
            with open(direccion, "r") as com:
                lista_comentarios = com.readlines()
                for i, valor in enumerate(lista_comentarios):
                    comentario = valor.split(",")
                    if int(comentario[0]) == fila:
                        lista_comentarios.pop(i)
                        flag = True
                        break
            if flag:
                with open(direccion, "w") as com:
                    com.writelines(lista_comentarios)
        except:
            pass



    def cambia_num_comentario(self, num, dir):
        flag = False
        direccion = self.direccion_actual[:-4] + "_comentarios.csv"
        with open(direccion, "r") as com:
            lista_comentarios = com.readlines()
            for i, valor in enumerate(lista_comentarios):
                comentario = valor.split(",")
                if dir == 1:
                    if comentario[0] == str(num):                                       # si se mueve hacia abajo...
                        lista_comentarios[i] = str(num + 1) + "," + comentario[1]       # Sobreescribe
                        flag = True

                    elif comentario[0] == str(num +1):
                        lista_comentarios[i] = str(num) + "," + comentario[1]           # Sobreescribe
                        flag = True
                else:
                    if comentario[0] == str(num):  # si se mueve hacia abajo...
                        lista_comentarios[i] = str(num - 1) + "," + comentario[1]  # Sobreescribe
                        flag = True

                    elif comentario[0] == str(num - 1):
                        lista_comentarios[i] = str(num) + "," + comentario[1]  # Sobreescribe
                        flag = True
        if flag:
            with open(direccion, "w") as com:
                com.writelines(lista_comentarios)



    def funcion_mover_fila(self):
        sender = self.sender()
        indexes = self.tabla_proyecto.selectionModel().selectedRows()
        if indexes != []:
            for index in indexes:
                num_fila = index.row()

            if sender.objectName() == "boton_abajo":
                if num_fila != self.tabla_proyecto.rowCount() - 1:

                    var1 = self.tabla_proyecto.takeItem(num_fila, 0)
                    var2 = self.tabla_proyecto.takeItem(num_fila, 1)
                    var3 = self.tabla_proyecto.takeItem(num_fila, 2)
                    var4 = self.tabla_proyecto.takeItem(num_fila, 5)
                    var5 = self.tabla_proyecto.takeItem(num_fila, 6)

                    var6 = self.tabla_proyecto.takeItem(num_fila + 1, 0)
                    var7 = self.tabla_proyecto.takeItem(num_fila + 1, 1)
                    var8 = self.tabla_proyecto.takeItem(num_fila + 1, 2)
                    var9 = self.tabla_proyecto.takeItem(num_fila + 1, 5)
                    var10 = self.tabla_proyecto.takeItem(num_fila + 1, 6)

                    self.tabla_proyecto.setItem(num_fila + 1, 0, var1)
                    self.tabla_proyecto.setItem(num_fila + 1, 1, var2)
                    self.tabla_proyecto.setItem(num_fila + 1, 2, var3)
                    self.tabla_proyecto.setItem(num_fila + 1, 5, var4)
                    self.tabla_proyecto.setItem(num_fila + 1, 6, var5)

                    self.tabla_proyecto.setItem(num_fila, 0, var6)
                    self.tabla_proyecto.setItem(num_fila, 1, var7)
                    self.tabla_proyecto.setItem(num_fila, 2, var8)
                    self.tabla_proyecto.setItem(num_fila, 5, var9)
                    self.tabla_proyecto.setItem(num_fila, 6, var10)

                    self.cambia_num_comentario(num_fila, 1)
                    exec(f"self.e_actual = self.boton_estado_{num_fila}.text()")
                    exec(f"self.e_actual_1 = self.boton_estado_{num_fila + 1}.text()")  # guardo estados actuales
                    if self.e_actual_1 == "Pendiente":
                        color_actual_1 = "red"
                    elif self.e_actual_1 == "Hecho":
                        color_actual_1 = "green"
                    elif self.e_actual_1 == "En curso":
                        color_actual_1 = "yellow"
                    if self.e_actual == "Pendiente":
                        color_actual = "red"
                    elif self.e_actual == "Hecho":
                        color_actual = "green"
                    elif self.e_actual == "En curso":
                        color_actual = "yellow"

                    self.crear_botones(num_fila, num_fila + 2)  # Creo botones
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, self.e_actual_1 ,self.boton_estado_{num_fila} , color_actual_1, 'black', 'boton_estado_{num_fila}')")
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_fila} , 'white', 'black', 'boton_comentario_{num_fila}')")

                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, self.e_actual,self.boton_estado_{num_fila + 1} , color_actual, 'black', 'boton_estado_{num_fila + 1}')")
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_fila + 1} , 'white', 'black', 'boton_comentario_{num_fila + 1}')")

                    exec(f"self.tabla_proyecto.setCellWidget({num_fila}, 4, self.boton_estado_{num_fila})")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila} , 3, self.boton_comentario_{num_fila})")
                    exec(f"self.boton_comentario_{num_fila}.setText('')")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila + 1}, 4, self.boton_estado_{num_fila + 1})")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila + 1} , 3, self.boton_comentario_{num_fila + 1})")
                    exec(f"self.boton_comentario_{num_fila + 1}.setText('')")
                    self.tabla_proyecto.selectRow(num_fila + 1)
            elif sender.objectName() == "boton_arriba":
                if num_fila != 0:
                    var1 = self.tabla_proyecto.takeItem(num_fila, 0)
                    var2 = self.tabla_proyecto.takeItem(num_fila, 1)
                    var3 = self.tabla_proyecto.takeItem(num_fila, 2)
                    var4 = self.tabla_proyecto.takeItem(num_fila, 5)
                    var5 = self.tabla_proyecto.takeItem(num_fila, 6)
                    var6 = self.tabla_proyecto.takeItem(num_fila - 1, 0)
                    var7 = self.tabla_proyecto.takeItem(num_fila - 1, 1)
                    var8 = self.tabla_proyecto.takeItem(num_fila - 1, 2)
                    var9 = self.tabla_proyecto.takeItem(num_fila - 1, 5)
                    var10 = self.tabla_proyecto.takeItem(num_fila - 1, 6)

                    self.tabla_proyecto.setItem(num_fila - 1, 0, var1)
                    self.tabla_proyecto.setItem(num_fila - 1, 1, var2)
                    self.tabla_proyecto.setItem(num_fila - 1, 2, var3)
                    self.tabla_proyecto.setItem(num_fila - 1, 5, var4)
                    self.tabla_proyecto.setItem(num_fila - 1, 6, var5)
                    self.tabla_proyecto.setItem(num_fila, 0, var6)
                    self.tabla_proyecto.setItem(num_fila, 1, var7)
                    self.tabla_proyecto.setItem(num_fila, 2, var8)
                    self.tabla_proyecto.setItem(num_fila, 5, var9)
                    self.tabla_proyecto.setItem(num_fila, 6, var10)

                    self.cambia_num_comentario(num_fila, 2)
                    exec(f"self.e_actual = self.boton_estado_{num_fila}.text()")
                    exec(f"self.e_actual_1 = self.boton_estado_{num_fila - 1}.text()")  # guardo estados actuales
                    if self.e_actual_1 == "Pendiente":
                        color_actual_1 = "red"
                    elif self.e_actual_1 == "Hecho":
                        color_actual_1 = "green"
                    elif self.e_actual_1 == "En curso":
                        color_actual_1 = "yellow"
                    if self.e_actual == "Pendiente":
                        color_actual = "red"
                    elif self.e_actual == "Hecho":
                        color_actual = "green"
                    elif self.e_actual == "En curso":
                        color_actual = "yellow"

                    self.crear_botones(num_fila - 1, num_fila + 1)  # Creo botones
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, self.e_actual_1 ,self.boton_estado_{num_fila} , color_actual_1, 'black', 'boton_estado_{num_fila}')")
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_fila} , 'white', 'black', 'boton_comentario_{num_fila}')")

                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, self.e_actual,self.boton_estado_{num_fila - 1} , color_actual, 'black', 'boton_estado_{num_fila - 1}')")
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_fila - 1} , 'white', 'black', 'boton_comentario_{num_fila - 1}')")

                    exec(f"self.tabla_proyecto.setCellWidget({num_fila}, 4, self.boton_estado_{num_fila})")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila} , 3, self.boton_comentario_{num_fila})")
                    exec(f"self.boton_comentario_{num_fila}.setText('')")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila - 1}, 4, self.boton_estado_{num_fila - 1})")
                    exec(f"self.tabla_proyecto.setCellWidget({num_fila - 1} , 3, self.boton_comentario_{num_fila - 1})")
                    exec(f"self.boton_comentario_{num_fila - 1}.setText('')")
                    self.tabla_proyecto.selectRow(num_fila - 1)

    def agrega_fila(self):
        indexes = self.tabla_proyecto.selectionModel().selectedRows()
        if indexes == []:
            num_filas = self.tabla_proyecto.rowCount()  # Cuento las filas en la tabla
            self.tabla_proyecto.insertRow(num_filas)  # inserta una fila nueva al final
            self.crear_botones(num_filas, num_filas + 1)
            exec(
                f"self.crear_boton_normal(0, 0, 16,16, 'Pendiente',self.boton_estado_{num_filas} , 'red', 'black', 'boton_estado_{num_filas}')")
            exec(
                f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_filas} , 'white', 'black', 'boton_comentario_{num_filas}')")
            exec(f"self.tabla_proyecto.setCellWidget({num_filas}, 4, self.boton_estado_{num_filas})")
            exec(f"self.tabla_proyecto.setCellWidget({num_filas} , 3, self.boton_comentario_{num_filas})")
            exec(f"self.boton_comentario_{num_filas}.setText('')")
        else:
            for index in indexes:
                num_filas = self.tabla_proyecto.rowCount()  # Cuento las filas en la tabla
                num_fila = index.row()
                self.lista_estados = []
                for i in range(num_fila, num_filas):
                    exec(f"self.lista_estados.append(self.boton_estado_{i}.text())")
                self.tabla_proyecto.insertRow(num_fila)
                print(self.lista_estados)
                self.crear_botones(num_fila, num_filas + 1)
                exec(
                    f"self.crear_boton_normal(0, 0, 16,16, 'Pendiente',self.boton_estado_{num_fila} , 'red', 'black', 'boton_estado_{num_fila}')")
                exec(
                    f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{num_fila} , 'white', 'black', 'boton_comentario_{num_fila}')")

                exec(f"self.tabla_proyecto.setCellWidget({num_fila}, 4, self.boton_estado_{num_fila})")
                exec(f"self.tabla_proyecto.setCellWidget({num_fila} , 3, self.boton_comentario_{num_fila})")
                exec(f"self.boton_comentario_{num_fila}.setText('')")
                count = 0
                self.recorre_num_comentario(num_fila, 1)
                for i in range(num_fila + 1, num_filas + 1):

                    if self.lista_estados[count] == "Pendiente":
                        color_actual = "red"
                    elif self.lista_estados[count] == "Hecho":
                        color_actual = "green"
                    elif self.lista_estados[count] == "En curso":
                        color_actual = "yellow"

                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, self.lista_estados[{count}] ,self.boton_estado_{i} , color_actual, 'black', 'boton_estado_{i}')")
                    exec(
                        f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{i} , 'white', 'black', 'boton_comentario_{i}')")

                    exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                    exec(f"self.tabla_proyecto.setCellWidget({i} , 3, self.boton_comentario_{i})")
                    exec(f"self.boton_comentario_{i}.setText('')")
                    count += 1

                break

        self.verificar_estado()

    def remueve_fila(self):
        indexes = self.tabla_proyecto.selectionModel().selectedRows()
        if indexes == []:
            pass
        else:
            for index in indexes:
                num_fila = index.row()
                self.tabla_proyecto.removeRow(num_fila)
                break
            self.remueve_comentario(num_fila)
            self.recorre_num_comentario(num_fila, 2)
            num_filas_totales = self.tabla_proyecto.rowCount()
            for i in range(num_fila, num_filas_totales):
                exec(f"self.estado =self.boton_estado_{i + 1}.text()")
                if self.estado == "Pendiente":
                    color_fondo = 'red'
                elif self.estado == "En curso":
                    color_fondo = 'yellow'
                elif self.estado == "Hecho":
                    color_fondo = 'green'
                self.crear_botones(i, i + 1)
                exec(
                    f"self.crear_boton_normal(0, 0, 16,16, self.estado, self.boton_estado_{i} , color_fondo, 'black', 'boton_estado_{i}')")
                exec(f"self.tabla_proyecto.setCellWidget({i}, 4, self.boton_estado_{i})")
                exec(
                    f"self.crear_boton_normal(0, 0, 16,16, 'Añadir comentario',self.boton_comentario_{i} , 'white', 'black', 'boton_comentario_{i}')")
                exec(f"self.tabla_proyecto.setCellWidget({i} , 3, self.boton_comentario_{i})")
                exec(f"self.boton_comentario_{i}.setText('')")
            if self.tabla_proyecto.rowCount() > 0:
                self.verificar_estado()
            else:
                self.progressbar_1.setValue(0)

    def crear_botones(self, inicio=0, final=100):
        for i in range(inicio, final):
            exec(f"self.boton_estado_{i} = QtWidgets.QPushButton(self.grupo_proyectoactual)")
            exec(f"self.boton_comentario_{i} = QtWidgets.QPushButton(self.grupo_proyectoactual)")
            exec(f"self.conectar(self.boton_estado_{i}, self.boton_comentario_{i})")

    def conectar(self, nombre_objeto, nombre_objeto_1):
        nombre_objeto.clicked.connect(lambda: self.funcion_estado())
        nombre_objeto_1.clicked.connect(lambda: self.funcion_comentarios())

    def desconectar(self, nombre_objeto, nombre_objeto_1):
        nombre_objeto.clicked.disconnect(lambda: self.funcion_estado())
        nombre_objeto_1.clicked.disconnect(lambda: self.funcion_comentarios())

    def funcion_inicio(self):
        self.set_visible(self.grupo_contenido)
        self.cambia_color(self.label_menu)

    def funcion_proyecto_actual(self):
        self.set_visible(self.grupo_proyectoactual)
        self.cambia_color(self.label_menu_1)

    def funcion_lista_materiales(self):
        self.set_visible(self.grupo_lista_de_materiales)
        self.cambia_color(self.label_menu_2)

    def funcion_calculos(self):
        self.set_visible(self.grupo_calculos)
        self.cambia_color(self.label_menu_3)

    def borrar(self):
        self.combobox_select.clear()
        self.combobox_select_1.clear()
        self.edit_conversion.setText("")
        self.edit_conversion_1.setText("")

    def funcion_volumen(self):

        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.label_conversiones.setText("Volumen")
        self.borrar()

        self.combobox_select.addItems(conv.lista_volumen)
        self.combobox_select_1.addItems(conv.lista_volumen)
        self.matriz_tipo = conv.matriz_volumen
        self.lista_tipo = conv.lista_volumen
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_velocidad(self):
        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.label_conversiones.setText("Velocidad")
        self.borrar()
        self.combobox_select.addItems(conv.lista_velocidad)
        self.combobox_select_1.addItems(conv.lista_velocidad)
        self.matriz_tipo = conv.matriz_velocidad
        self.lista_tipo = conv.lista_velocidad
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_masa(self):
        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.label_conversiones.setText("Masa")
        self.borrar()
        self.combobox_select.addItems(conv.lista_masa)
        self.combobox_select_1.addItems(conv.lista_masa)
        self.matriz_tipo = conv.matriz_masa
        self.lista_tipo = conv.lista_masa
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_longitud(self):
        self.set_visible(self.grupo_conversiones)
        self.borrar()
        self.set_visible_teclado()
        self.label_conversiones.setText("Longitud")
        self.combobox_select.addItems(conv.lista_longitud)
        self.combobox_select_1.addItems(conv.lista_longitud)
        self.matriz_tipo = conv.matriz_longitud
        self.lista_tipo = conv.lista_longitud
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_tiempo(self):
        self.set_visible(self.grupo_conversiones)
        self.borrar()
        self.set_visible_teclado()
        self.label_conversiones.setText("Tiempo")
        self.combobox_select.addItems(conv.lista_tiempo)
        self.combobox_select_1.addItems(conv.lista_tiempo)
        self.matriz_tipo = conv.matriz_tiempo
        self.lista_tipo = conv.lista_tiempo
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_temperatura(self):
        self.set_visible(self.grupo_conversiones)
        self.borrar()
        self.set_visible_teclado()
        self.label_conversiones.setText("Temperatura")
        self.combobox_select.addItems(conv.lista_temperatura)
        self.combobox_select_1.addItems(conv.lista_temperatura)
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 1

    def funcion_angulo(self):
        self.set_visible(self.grupo_conversiones)
        self.borrar()
        self.set_visible_teclado()
        self.label_conversiones.setText("Ángulo")
        self.combobox_select.addItem(conv.lista_angulo[0])
        self.combobox_select_1.addItem(conv.lista_angulo[1])
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 2

    def funcion_energia(self):
        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.borrar()
        self.label_conversiones.setText("Energía")
        self.combobox_select.addItems(conv.lista_energia)
        self.combobox_select_1.addItems(conv.lista_energia)
        self.matriz_tipo = conv.matriz_energia
        self.lista_tipo = conv.lista_energia
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_presion(self):
        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.borrar()
        self.label_conversiones.setText("Presión")
        self.combobox_select.addItems(conv.lista_presion)
        self.combobox_select_1.addItems(conv.lista_presion)
        self.matriz_tipo = conv.matriz_presion
        self.lista_tipo = conv.lista_presion
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def funcion_fuerza(self):
        self.set_visible(self.grupo_conversiones)
        self.set_visible_teclado()
        self.borrar()
        self.label_conversiones.setText("Fuerza")
        self.combobox_select.addItems(conv.lista_fuerza)
        self.combobox_select_1.addItems(conv.lista_fuerza)
        self.matriz_tipo = conv.matriz_fuerza
        self.lista_tipo = conv.lista_fuerza
        self.cambia_color(self.label_menu_3)
        self.flag_conversion_unidades = 0

    def convierte_unidades(self, numero, inicial, final, nombre_objeto, tipo_matriz=conv.matriz_volumen,
                           tipo_lista=conv.lista_volumen):
        if self.flag_conversion_unidades == 1:

            try:
                num_conv = float(numero)
                if inicial == "Celsius" and final == "Fahrenheit":
                    resultado = 32 + 1.8 * num_conv
                    print(resultado)
                elif inicial == "Kelvin" and final == "Fahrenheit":
                    resultado = (num_conv - 273.15) * 1.8 + 32
                elif inicial == "Fahrenheit" and final == "Celsius":
                    resultado = (num_conv - 32) / 1.8
                elif inicial == "Kelvin" and final == "Celsius":
                    resultado = num_conv - 273.15
                elif inicial == "Celsius" and final == "Kelvin":
                    resultado = num_conv + 273.15
                elif inicial == "Fahrenheit" and final == "Kelvin":
                    resultado = (num_conv - 32) / 1.8 + 273.15
                elif inicial == final:
                    resultado = num_conv
                if nombre_objeto == self.edit_conversion:
                    self.edit_conversion_1.setText(str(resultado))
                else:
                    self.edit_conversion.setText(str(resultado))
            except:
                nombre_objeto.setText(nombre_objeto.text()[0:-1])
                if nombre_objeto.text() == "":
                    self.edit_conversion.setText("")
                    self.edit_conversion_1.setText("")

        elif self.flag_conversion_unidades == 2:
            try:
                num_conv = float(numero)
                grados = (num_conv * 180) / np.pi
                radianes = (num_conv * np.pi) / 180
                if nombre_objeto == self.edit_conversion:
                    self.edit_conversion_1.setText(str(grados))
                else:
                    self.edit_conversion.setText(str(radianes))
            except:
                nombre_objeto.setText(nombre_objeto.text()[0:-1])
                if nombre_objeto.text() == "":
                    self.edit_conversion.setText("")
                    self.edit_conversion_1.setText("")

        else:
            try:
                num_conv = float(numero)
                resultado = conv.conversion_unidades(num_conv, inicial, final, tipo_matriz, tipo_lista)
                if nombre_objeto == self.edit_conversion:
                    self.edit_conversion_1.setText(str(resultado))
                else:
                    self.edit_conversion.setText(str(resultado))
            except:
                nombre_objeto.setText(nombre_objeto.text()[0:-1])
                if nombre_objeto.text() == "":
                    self.edit_conversion.setText("")
                    self.edit_conversion_1.setText("")

    def convierte(self, nombre_objeto):
        numero_decimal = 0
        try:
            if nombre_objeto == self.edit_decimal:
                numero_decimal = int(nombre_objeto.text())
            elif nombre_objeto == self.edit_octal:
                numero_decimal = int(nombre_objeto.text(), 8)  # convirte el numero octal a decimal
            elif nombre_objeto == self.edit_hexadecimal:
                numero_decimal = int(nombre_objeto.text(), 16)  # convierte el numero hexadecimal a decimal
            elif nombre_objeto == self.edit_binario:
                numero_decimal = int(nombre_objeto.text(), 2)  # convirte el numero binario a decimal

            numero_binario = bin(numero_decimal)
            numero_octal = oct(numero_decimal)
            numero_hexadecimal = hex(numero_decimal)

            self.edit_decimal.setText(str(numero_decimal))
            self.edit_octal.setText(numero_octal[2:])
            self.edit_hexadecimal.setText(numero_hexadecimal[2:])
            self.edit_binario.setText(numero_binario[2:])
        except:
            nombre_objeto.setText(nombre_objeto.text()[0:-1])
            if nombre_objeto.text() == "":
                self.edit_decimal.setText("")
                self.edit_octal.setText("")
                self.edit_hexadecimal.setText("")
                self.edit_binario.setText("")

    def crear_combobox(self, x, y, w, h, texto, nombre_objeto, color, font_color):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setVisible(True)

        nombre_objeto.setFont(self.set_font(12))  # establece el tipo de fuente
        nombre_objeto.setStyleSheet("QComboBox"
                                    "{"
                                    "gridline-color: gray;"
                                    f"color: {font_color};"
                                    f"background-color : {color};"
                                    'border-radius: 15px;'
                                    "border-style: none;"
                                    "border-width: 0.5px;"
                                    "border-color: black"
                                    "}"
                                    )

    def crear_cuadro_con_contenido_2(self, initx, inity, w, h, seperacion_h, separacion_v, row_count,
                                     column_count):  # creo un nuevo cuadro con contenido (imagen de producto y boton)
        count = 0
        for r in range(row_count):
            for c in range(column_count):
                # if self.names[count] == "":
                #     continue

                exec(
                    f"self.crear_groupbox(initx + (w + seperacion_h)*c, inity + (h + separacion_v)*r,w, h,'grupo_materiales_{count}', self.grupo_materiales_{count}, 'white'  )")
                # exec(f"self.grupo_materiales_{count}.setStyleSheet('border-style:solid; border-color: black; border-width:1px')")
                exec(f"self.grupo_materiales_{count}.setVisible(True)")
                exec(
                    f"self.crear_boton_normal(0, h-30, w, 30, '{self.lista_materiales[count]}', self.boton_materiales_{count}, 'white', 'black', 'boton_materiales_{count}', 'none')")
                exec(f"self.crear_label(2, 5, w-2, h - 60, '', self.label_materiales_{count}, 'white')")
                exec(
                    f"self.label_materiales_{count}.setPixmap(QtGui.QPixmap('iconos/{self.lista_materiales[count]}' + '.png'))")

                count += 1
        # self.crear_label(0, 10, w, h - 60, "", nombre_objeto_label)
        # nombre_objeto_label.setPixmap(QtGui.QPixmap(f"imagenes/{nombre}" + ".jpg"))
        # self.crear_label(0, h - 50, w, 50, f"{nombre}\nPrecio unitario:", nombre_objeto_boton)

    def define_titulo_columna(self, texto):
        item = QtWidgets.QTableWidgetItem()
        item.setText(texto)
        item.setFont(self.set_font())
        return item

    def crear_groupbox(self, x, y, w, h, texto, nombre_objeto, color):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setVisible(False)
        nombre_objeto.setStyleSheet(f"background-color: {color}; border-style: solid; border-radius: 15px")

    def crear_lineEdit(self, x, y, w, h, texto, nombre_objeto, object_name="edit"):

        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(object_name)
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setPlaceholderText(texto)
        nombre_objeto.setStyleSheet("border-style: solid; border-width: 0.5px")

    def crear_textedit(self, x, y, w, h, texto, nombre_objeto, back_color="transparent", font_color="black"):
        nombre_objeto_name = str(nombre_objeto) + "_textEdit"
        nombre_objeto.setEnabled(True)
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setPlaceholderText(texto)
        nombre_objeto.setObjectName(nombre_objeto_name)
        nombre_objeto.setStyleSheet("border-style: solid; "
                                    "border-width: 0.5px;"
                                    f"background-color: {back_color};"
                                    f"color: {font_color}"
                                    )

    def crear_calendarwidget(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)  # establece nombre de objeto
        nombre_objeto.setFont(self.set_font(12))  # establece el tipo de fuente
        nombre_objeto.setVisible(False)
        nombre_objeto.showToday()
        nombre_objeto.setStyleSheet(
            "color: black; background-color: white; selection-background-color: rgb(127,127,127);border-style: solid")
        nombre_objeto.setStyleSheet('''
                                   QCalendarWidget QAbstractItemView:enabled 
                            {
                                font-size:12px;  
                                color: black;  
                                font: 12pt "Century Gothic";
                                background-color: white;  
                                selection-background-color: rgb(127,127,127); 
                                selection-color: white; 
                            }       
                              QCalendarWidget QMenu {
                                width: 150px;
                                left: 20px;
                                color: white;
                                font-size: 18px;
                                background-color: rgb(100, 100, 100);
                                }
                                QCalendarWidget QToolButton {
                                    height: 30px;
                                    width: 150px;
                                    color: white;
                                    font: 12pt "Century Gothic";
                                    font-size: 14px;
                                    icon-size: 15px, 15px;
                                    background-color: black;
                                }
                               
                                    '''
                                    )

    def crear_tableWidget(self, row_count, column_count, texto, x, y, w, h, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)  # establece nombre de objeto
        nombre_objeto.setColumnCount(column_count)  # Establece la cantidad de columnas
        nombre_objeto.setRowCount(row_count)  # Establece la cantidad de filas
        nombre_objeto.setFont(self.set_font(12))  # establece el tipo de fuente
        nombre_objeto.setStyleSheet("QTableWidget"
                                    "{"
                                    "gridline-color: gray;"
                                    "selection-background-color: rgb(205,92,92);"
                                    "selection-color: black;"
                                    f"color: black;"
                                    f"background-color : transparent;"
                                    'border-radius: 50px;'
                                    "border-style: none;"
                                    "border-width: 2px;"
                                    "border-color: black"
                                    "}"
                                    "QHeaderView::section"
                                    "{"
                                    "background-color : transparent;"
                                    "border-radius:14px"
                                    "}"
                                    )

    def crear_label(self, x, y, w, h, texto, nombre_objeto, color, font_color="black", border_style="none",
                    border_radius=30):
        label = texto + "_label"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setText(texto)
        nombre_objeto.setScaledContents(True)
        nombre_objeto.setObjectName(label)
        nombre_objeto.setStyleSheet("QLabel"
                                    "{"
                                    f"color: {font_color};"
                                    f"background-color : {color};"
                                    f'border-radius: {border_radius}px;'
                                    f"border-style: {border_style};"
                                    "border-width: 2px;"
                                    "border-color: black"
                                    "}"
                                    )

    def coloca_icono(self, nombre, nombre_objeto):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"iconos/{nombre.strip()}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nombre_objeto.setIcon(icon)

    def crear_progressbar(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setMouseTracking(True)

        nombre_objeto.setStyleSheet('''
                        QProgressBar{
                        border: 0.5px solid black;
                        border-radius: 2px;
                        text-align: center
                        }
                        QProgressBar::chunk {
                        background-color: rgb(205,92,92);
                        width: 5px;
                        }
                          ''')

    def crear_boton_menu(self, x, y, w, h, texto, nombre_objeto, nombre_objeto_label, color):
        boton_nombre = texto + "_boton"
        nombre_objeto.setGeometry(QtCore.QRect(x + 20, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setAutoFillBackground(True)
        nombre_objeto.setFlat(False)
        nombre_objeto.setObjectName(boton_nombre)
        nombre_objeto.setText(texto)
        self.coloca_icono(texto, nombre_objeto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setStyleSheet("QPushButton"
                                    "{"
                                    "border-radius: 10px;"
                                    f"background-color: {color};"
                                    "color: black;"
                                    "border-style: none;"
                                    "border-width: 0.5px;"
                                    "border-color: black;"
                                    "text-align: left"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : white;"
                                    "}")

        nombre_objeto.setVisible(True)
        self.crear_label(x, y, 16, h, "", nombre_objeto_label, "black")

    def crear_boton_redondo(self, x, y, r, texto, nombre_objeto, color, font_color):
        boton_nombre = texto + "_boton"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, r, r))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setAutoFillBackground(True)
        nombre_objeto.setFlat(False)
        nombre_objeto.setObjectName(boton_nombre)
        nombre_objeto.setText(texto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setStyleSheet(
            "QPushButton"
            "{"
            f"color: {font_color};"
            f"background-color : {color};"
            f'border-radius: {r / 2}px;'
            "border-style: solid;"
            "border-width: 0.5px;"
            "border-color: black"
            "}"
            "QPushButton::hover"
            "{"
            "background-color : rgb(210,105,30);"
            "color : white;"
            f"border-radius: {r / 2}px;"
            "}")
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setVisible(True)
        self.coloca_icono(texto, nombre_objeto)

    def crear_boton_normal(self, x, y, w, h, texto, nombre_objeto, color, font_color, object_name, border_style="none"):
        boton_nombre = object_name
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setAutoFillBackground(False)
        nombre_objeto.setObjectName(boton_nombre)
        nombre_objeto.setText(texto)
        nombre_objeto.setMouseTracking(True)

        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setVisible(True)
        self.coloca_icono(texto, nombre_objeto)
        nombre_objeto.setStyleSheet(
            "QPushButton"
            "{"
            f"color: {font_color};"
            f"background-color : {color};"
            f'border-radius: 10px;'
            f"border-style: {border_style};"
            "border-width: 0.5px;"
            "border-color: black"
            "}"
            "QPushButton::hover"
            "{"
            "background-color : rgb(210,105,30);"
            "color : white;"
            f"border-radius: 3px;"
            "}")

    def crear_checkBox(self, x, y, w, h, texto, nombre_objeto, color, font_color="black"):

        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setText(texto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setVisible(True)
        nombre_objeto.setStyleSheet(
            "QCheckBox"
            "{"
            f"color: {font_color};"
            f"background-color : {color};"
            f'border-radius: 10px;'
            f"border-style: none;"
            "border-width: 0.5px;"
            "border-color: black"
            "}"
        )

    def change_size(self):
        if self.grupo_menu.width() == 38:
            self.grupo_filtrar.setVisible(False)
            self.grupo_menu.resize(side_menu_width, window_height)
            self.boton_redondo_atras.move(side_menu_width - 30, 0)
            self.coloca_icono("flecha izquierda", self.boton_redondo_atras)
        else:
            self.grupo_filtrar.setVisible(True)
            self.grupo_menu.resize(38, window_height)
            self.boton_redondo_atras.move(9, 0)
            self.coloca_icono("flecha derecha", self.boton_redondo_atras)
        if self.label_acerca_de.isVisible():
            self.label_acerca_de.setVisible(False)

    def hecho(self, archivo):

        if self.edit_label_nombre.text() != "" and self.edit_label_nombre_proyecto.text() != "" and self.edit_label_direccion.text() != "":
            with open(f"archivos/{self.edit_label_nombre_proyecto.text()}_info.csv", "w") as Data:

                Data.writelines(self.edit_label_nombre.text() + "\n")
                Data.writelines(self.edit_label_nombre_proyecto.text() + "\n")
                Data.writelines(self.edit_label_direccion.text() + "\n")
                Data.writelines(self.edit_label_correo.text() + "\n")
                Data.writelines(self.textedit.toPlainText() + "\n")
            self.label_proyectoactual.setText("Proyecto actual" +": " + self.edit_label_nombre_proyecto.text())
            self.boton_menu.setEnabled(True)
            print(self.direccion_actual)
            self.funcion_guardar_tabla(self.direccion_actual)
            self.tabla_proyecto.setRowCount(0)
            self.progressbar_1.setValue(0)
            self.funcion_proyecto_actual()
        else:
            self.mensaje_error.exec_()


    def change_color(self, nombre_objeto):
        nombre_objeto.setStyleSheet("background-color: black; color: White")

    def ocultar(self):
        if self.tabla_proyecto.isVisible():
            self.tabla_proyecto.setVisible(False)
            self.coloca_icono("Triangulo abajo", self.boton_expandir)
        else:
            self.tabla_proyecto.setVisible(True)
            self.coloca_icono("Triangulo arriba", self.boton_expandir)

    def set_font(self, size=12):
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(size)
        return font

    def set_visible(self, nombre_objeto):
        self.grupo_contenido.setVisible(False)
        self.grupo_buscar.setVisible(False)
        self.grupo_nuevo_proyecto.setVisible(False)
        self.grupo_proyectoactual.setVisible(False)
        self.grupo_calculos.setVisible(False)
        self.grupo_programador.setVisible(False)
        self.grupo_conversiones.setVisible(False)
        self.grupo_calculos_1.setVisible(False)
        self.grupo_lista_de_materiales.setVisible(False)
        self.grupo_comentarios.setVisible(False)
        self.grupo_teclado.setVisible(False)
        self.grupo_calculadora.setVisible(False)
        self.grupo_componentes.setVisible(False)
        self.grupo_graficas.setVisible(False)
        nombre_objeto.setVisible(True)

    def set_visible_teclado(self):
        self.grupo_teclado.setVisible(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/Circulo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(_translate("MainWindow", " Gestor de proyectos"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # crea una instancia de la clase Qapplication
    MainWindow = QtWidgets.QMainWindow()    # crea una instancia de la clase QMainWindow
    ui = Ui_MainWindow()                    # instancia de clase Ui_MainWindow
    ui.setupUi(MainWindow)                  # Llama  al metodo setupUi, pasandole el parametro (MainWindow)
    MainWindow.show()                       # Muestra la ventana
    sys.exit(app.exec_())                   # sale de la aplicación
