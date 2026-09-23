def explorar_derecha():
    global resultado
    girar_derecha()
    cambiar_direccion_derecha()
    basic.pause(100)
    resultado = medir_distancia()
    girar_izquierda()
    cambiar_direccion_izquierda()
    return resultado
def girar_izquierda():
    cuteBot.motors(-55, 55)
    basic.pause(TIEMPO_GIRO)
    cuteBot.stopcar()
    basic.pause(100)
def cambiar_direccion_derecha():
    global direccion
    direccion = direccion + 1
    if direccion > 3:
        direccion = 0
def avanzar_celda():
    cuteBot.motors(VELOCIDAD, VELOCIDAD)
    basic.pause(TIEMPO_CELDA)
    cuteBot.stopcar()
    basic.pause(100)
def detener():
    cuteBot.stopcar()
def iniciar():
    global x, y, direccion, pasos
    x = 0
    y = 0
    direccion = 0
    pasos = 0
    visitados_x[0] = 0
    visitados_y[0] = 0
    basic.show_string("GO")
    basic.pause(500)
    buscar_salida()
def mover_posicion():
    global y, x
    if direccion == 0:
        y = y + 1
    elif direccion == 1:
        x = x + 1
    elif direccion == 2:
        y = y - 1
    else:
        x = x - 1
def cambiar_direccion_izquierda():
    global direccion
    direccion = direccion - 1
    if direccion < 0:
        direccion = 3
def ya_visitado(px: number, py: number):
    global i
    while i < len(visitados_x):
        if visitados_x[i] == px and visitados_y[i] == py:
            return True
        i = i + 1
    return False
def guardar_posicion():
    visitados_x.append(x)
    visitados_y.append(y)
def buscar_salida():
    global pasos, frente, derecha, izquierda, direccion
    pasos = pasos + 1
    if pasos >= MAX_PASOS:
        detener()
        basic.show_string("FIN")
        return
    frente = medir_distancia()
    if frente > 40:
        detener()
        basic.show_icon(IconNames.HAPPY)
        basic.pause(2000)
        return
    derecha = explorar_derecha()
    if derecha > DISTANCIA_SEGURA:
        girar_derecha()
        cambiar_direccion_derecha()
        mover_posicion()
        if not (ya_visitado(x, y)):
            guardar_posicion()
            avanzar_celda()
            return
        girar_izquierda()
        cambiar_direccion_izquierda()
    if frente > DISTANCIA_SEGURA:
        mover_posicion()
        if not (ya_visitado(x, y)):
            guardar_posicion()
            avanzar_celda()
            return
    izquierda = explorar_izquierda()
    if izquierda > DISTANCIA_SEGURA:
        girar_izquierda()
        cambiar_direccion_izquierda()
        mover_posicion()
        if not (ya_visitado(x, y)):
            guardar_posicion()
            avanzar_celda()
            return
        girar_derecha()
        cambiar_direccion_derecha()
    girar_180()
    direccion = direccion + 2
    if direccion > 3:
        direccion = direccion - 4
    mover_posicion()
    avanzar_celda()
def explorar_izquierda():
    global resultado2
    girar_izquierda()
    cambiar_direccion_izquierda()
    basic.pause(100)
    resultado2 = medir_distancia()
    girar_derecha()
    cambiar_direccion_derecha()
    return resultado2
def medir_distancia():
    return cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
def girar_derecha():
    cuteBot.motors(55, -55)
    basic.pause(TIEMPO_GIRO)
    cuteBot.stopcar()
    basic.pause(100)
def girar_180():
    cuteBot.motors(55, -55)
    basic.pause(TIEMPO_GIRO * 2)
    cuteBot.stopcar()
    basic.pause(100)
resultado2 = 0
izquierda = 0
derecha = 0
frente = 0
i = 0
pasos = 0
y = 0
x = 0
direccion = 0
resultado = 0
visitados_y: List[number] = []
visitados_x: List[number] = []
MAX_PASOS = 0
TIEMPO_GIRO = 0
TIEMPO_CELDA = 0
DISTANCIA_SEGURA = 0
VELOCIDAD = 0
VELOCIDAD = 50
DISTANCIA_SEGURA = 15
TIEMPO_CELDA = 700
TIEMPO_GIRO = 450
MAX_PASOS = 150
visitados_x = [0]
visitados_y = [0]
iniciar()

def on_forever():
    buscar_salida()
    basic.pause(100)
basic.forever(on_forever)
