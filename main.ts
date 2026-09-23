function explorar_derecha () {
    girar_derecha()
    cambiar_direccion_derecha()
    basic.pause(100)
    resultado = medir_distancia()
    girar_izquierda()
    cambiar_direccion_izquierda()
    return resultado
}
function girar_izquierda () {
    cuteBot.motors(-55, 55)
    basic.pause(TIEMPO_GIRO)
    cuteBot.stopcar()
    basic.pause(100)
}
function cambiar_direccion_derecha () {
    direccion = direccion + 1
    if (direccion > 3) {
        direccion = 0
    }
}
function avanzar_celda () {
    cuteBot.motors(VELOCIDAD, VELOCIDAD)
    basic.pause(TIEMPO_CELDA)
    cuteBot.stopcar()
    basic.pause(100)
}
function detener () {
    cuteBot.stopcar()
}
function iniciar () {
    x = 0
    y = 0
    direccion = 0
    pasos = 0
    visitados_x[0] = 0
    visitados_y[0] = 0
    basic.showString("GO")
    basic.pause(500)
    buscar_salida()
}
function mover_posicion () {
    if (direccion == 0) {
        y = y + 1
    } else if (direccion == 1) {
        x = x + 1
    } else if (direccion == 2) {
        y = y - 1
    } else {
        x = x - 1
    }
}
function cambiar_direccion_izquierda () {
    direccion = direccion - 1
    if (direccion < 0) {
        direccion = 3
    }
}
function ya_visitado (px: number, py: number) {
    while (i < visitados_x.length) {
        if (visitados_x[i] == px && visitados_y[i] == py) {
            return true
        }
        i = i + 1
    }
    return false
}
function guardar_posicion () {
    visitados_x.push(x)
    visitados_y.push(y)
}
function buscar_salida () {
    pasos = pasos + 1
    if (pasos >= MAX_PASOS) {
        detener()
        basic.showString("FIN")
        return
    }
    frente = medir_distancia()
    if (frente > 40) {
        detener()
        basic.showIcon(IconNames.Happy)
        basic.pause(2000)
        return
    }
    derecha = explorar_derecha()
    if (derecha > DISTANCIA_SEGURA) {
        girar_derecha()
        cambiar_direccion_derecha()
        mover_posicion()
        if (!(ya_visitado(x, y))) {
            guardar_posicion()
            avanzar_celda()
            return
        }
        girar_izquierda()
        cambiar_direccion_izquierda()
    }
    if (frente > DISTANCIA_SEGURA) {
        mover_posicion()
        if (!(ya_visitado(x, y))) {
            guardar_posicion()
            avanzar_celda()
            return
        }
    }
    izquierda = explorar_izquierda()
    if (izquierda > DISTANCIA_SEGURA) {
        girar_izquierda()
        cambiar_direccion_izquierda()
        mover_posicion()
        if (!(ya_visitado(x, y))) {
            guardar_posicion()
            avanzar_celda()
            return
        }
        girar_derecha()
        cambiar_direccion_derecha()
    }
    girar_180()
    direccion = direccion + 2
    if (direccion > 3) {
        direccion = direccion - 4
    }
    mover_posicion()
    avanzar_celda()
}
function explorar_izquierda () {
    girar_izquierda()
    cambiar_direccion_izquierda()
    basic.pause(100)
    resultado2 = medir_distancia()
    girar_derecha()
    cambiar_direccion_derecha()
    return resultado2
}
function medir_distancia () {
    return cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
}
function girar_derecha () {
    cuteBot.motors(55, -55)
    basic.pause(TIEMPO_GIRO)
    cuteBot.stopcar()
    basic.pause(100)
}
function girar_180 () {
    cuteBot.motors(55, -55)
    basic.pause(TIEMPO_GIRO * 2)
    cuteBot.stopcar()
    basic.pause(100)
}
let resultado2 = 0
let izquierda = 0
let derecha = 0
let frente = 0
let i = 0
let pasos = 0
let y = 0
let x = 0
let direccion = 0
let resultado = 0
let visitados_y: number[] = []
let visitados_x: number[] = []
let MAX_PASOS = 0
let TIEMPO_GIRO = 0
let TIEMPO_CELDA = 0
let DISTANCIA_SEGURA = 0
let VELOCIDAD = 0
VELOCIDAD = 50
DISTANCIA_SEGURA = 15
TIEMPO_CELDA = 700
TIEMPO_GIRO = 450
MAX_PASOS = 150
visitados_x = [0]
visitados_y = [0]
iniciar()
basic.forever(function () {
    buscar_salida()
    basic.pause(100)
})
