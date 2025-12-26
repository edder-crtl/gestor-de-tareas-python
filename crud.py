from clases import Tarea, EstadoTarea, ImportanciaTarea
import datetime
from funciones import pedir_fecha,validacion_campo, confirmacion





def crear_tarea(lista):
    while True:
        operacion='El Titulo'
        titulo=input('ingrese el titulo nuevo: ')
        if validacion_campo(titulo,operacion ):
            break
        continue

    while True:
        operacion='La descripcion'
        descripcion=input('ingrese la descripcion de la tarea: ')
        if validacion_campo(descripcion, operacion):
            break
        continue
    
    fecha_creacion=datetime.datetime.now()
    estado=EstadoTarea.PENDIENTE
    fecha_entrega=pedir_fecha()

    while True:
        try:
            importancia=int(input('''ingrese la importancion de su tarea: 
        1.BAJA
        2.MEDIA
        3.ALTA
        : '''))
            if verificar_importancia(importancia):
                break
        except ValueError:
            print('tipo de dato erroneo, asegurese de ingresar un numero')
            confirmacion()


    Nueva = Tarea (
        titulo=titulo,
        descripcion=descripcion,
        fecha_creacion=fecha_creacion,
        fecha_entrega=fecha_entrega,
        estado=estado,
        importancia=importancia
    )
    lista.append(Nueva)


def verificar_importancia(a):
    try:
        importancia=ImportanciaTarea(a)
        return importancia
    except ValueError:
        return None


def mostrar_tareas(lista):
    if not lista or lista==[]:
        print('sin tareas existentes')
        return
    for i, tarea in enumerate(lista, start=1):
        print(f'\n {i}. Titulo de la tarea: {tarea.titulo}')
        print(f'Descripcion de la tarea: {tarea.descripcion}')
        print(f'Fecha de creacion de la tarea: {tarea.fecha_creacion}')
        print(f'Fecha de entrega: {tarea.fecha_entrega}')
        print(f'Estado de la tarea:{tarea.estado.name}')
        print(f'Importancia de la tarea:{tarea.importancia.name}')


def obtener_tarea(lista, opcion):
    indice=opcion-1
    tarea_sel=lista[indice]
    return tarea_sel

####parte de modicar tarea

def modificar_tarea_ux(lista):
    print('0.salir del menu')
    while True:
        try:
            opcion=int(input('ingrese la tarea que desea modificar: '))
            return opcion
        except ValueError:
            print('error en tipo de dato')


def verificar_indice(lista, opcion):
    ### las listas del usuario empiezan en 1, nosotros en 0, por eso se usa -1
    indice=opcion-1
    if indice >= len(lista) or indice <=-1:
        return False
    else:
        return True


def mostrar_tarea(tarea_sel):
    print(f'1. Titulo de la tarea:{tarea_sel.titulo}')
    print(f'2. Descripcion de la tarea: {tarea_sel.descripcion}')
    print(f' [Inmodificable] Fecha de creacion de la tarea: {tarea_sel.fecha_creacion}')
    print(f'3. Fecha de entrega: {tarea_sel.fecha_entrega}')
    print(f'4. Estado de la tarea:{tarea_sel.estado.name}')
    print(f'5. Importancia de la tarea:{tarea_sel.importancia.name}')


def pedir_opcion_submenu(tipo_tarea):
    print('6. salir del menu')
    while True:
        try:
            opcion_modificada=int(input(f'ingrese la opcion a {tipo_tarea}, debe ser un NUMERO:'))
            return opcion_modificada
        except ValueError:
            print('tipo de dato invalido, ingrese un NUMERO')
            continue

def verificar_opcion_submenu(opcion):
    if not 1<= opcion <=6 :
        print('opcion invalida, selecion uno valido')
        return False
    else:
        return True

def sel_modificacion(opcion):
    if opcion==1:
        campo='El titulo'
        while True:
            modificacion=input('ingrese el nuevo titulo: ')
            if validacion_campo(modificacion, campo):
                return modificacion
            else:
                continue
    elif opcion==2:
        campo='La descripcion'
        while True:
            modificacion= input('ingrese la nueva descripcion: ')
            if validacion_campo(modificacion, campo):
                return modificacion
            else:
                continue
    elif opcion==3:
        modificacion= pedir_fecha()
        return modificacion
    elif opcion==4:
        modificacion= input('ingrese el nuevo estado:')
        return modificacion
    elif opcion==5:
        modificacion= input('ingrese la nueva importancia:')
        return modificacion
    elif opcion==6:
        print('salir del menu')
        return None



def modificar_tarea_sel(tarea, modificacion, opcion):
    if opcion==1:
        tarea.titulo=modificacion
        return True
    elif opcion==2:
        tarea.descripcion= modificacion
        return True
    elif opcion==3:
        tarea.fecha_creacion= modificacion
        return True
    elif opcion==4:
        tarea.estado= modificacion
        return True
    elif opcion==5:
        tarea.importancia= modificacion
        return True


def pregunta_continuacion():
    continuacion=input('¿desea continuar modificando? (s/n):').upper()
    if continuacion != 'S':
        print('modificaciones realizadas con exito, feliz dia')
        return False
    else:
        print('continuara modifcando la misma tarea')
        return True


###borrar

def borrar_seleccion(lista):
    while True:
        try:
            opcion=int(input('selecione la tarea a eliminar:'))-1 ###usuario=1 sistema=0
            if opcion >= len(lista) or opcion <=-1:
                print('numero de usuario inexistente, intentelo nuevamente')
                continue
            return opcion
        except ValueError:
            print('tipo de dato erroneo, ingrese uno correcto')
            continue

def confirmacion_borrar():
    while True:
        try:
            confirmacion=input('esta seguro de eliminar la tarea (s/n)').upper()
            if confirmacion=='S':
                return True
            input('cancelado con exito, ingrese enter para continuar')
            return False
        except ValueError:
            print('INGRESE UNA LETRA')


def borrar_tarea(lista, tarea):
    lista.pop(tarea)