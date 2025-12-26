import datetime

def confirmacion():
    input(' \n ingrese enter para continuar')
    pass

def pedir_fecha():
    while True:
        try:
            fecha_str=input('ingrese la fecha en formato  YYYY-MM-DD: ')
            fecha=llenar_fecha(fecha_str)
            return fecha
        except ValueError:
            print('fecha invalida ingrese una nueva')
            continue


def llenar_fecha(fecha_str):
    return datetime.datetime.strptime(fecha_str, '%Y-%m-%d')

def validacion_campo(texto, campo):
    if not texto or texto.strip()=='':
        print(F'{campo} no puede estar vacio, intentelo nuevamente')
        return False
    return True
