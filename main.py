from funciones import confirmacion
from guardado_datos import cargar_tareas, guardar_tareas
from crud import crear_tarea, mostrar_tareas,modificar_tarea_ux, verificar_indice, obtener_tarea, mostrar_tarea,verificar_opcion_submenu, pedir_opcion_submenu, sel_modificacion, modificar_tarea_sel, pregunta_continuacion,borrar_seleccion,borrar_tarea, confirmacion_borrar





def main():
    Tareas=cargar_tareas()
    while True:
        try:
            opcion=int(input('''bienvenido a su gestor de tareas, que desea hacer el dia de hoy
    1. Crear una tarea
    2. revisar tareas 
    3. modificar tareas
    4. eliminar tarea
    0. salir
    ingrese su opcion: '''))
        except ValueError:
            print('debe ingresar un NUMERO')
            confirmacion()
            continue


        if opcion==0:
            print('gracias por usar nuestro sistema, tenga un buen dia')
            break

        elif opcion==1:
            crear_tarea(Tareas)
            guardar_tareas(Tareas)
            confirmacion()
            continue 

        elif opcion==2:
            mostrar_tareas(Tareas)
            confirmacion()
            continue

        elif opcion==3:
            tipo_tarea='modificar'
            while True:
                mostrar_tareas(Tareas)
                opcion_tarea=modificar_tarea_ux(Tareas)
                if opcion_tarea==0:
                    break
                es_valido=verificar_indice(Tareas, opcion_tarea) ### Validamos la opcion
                if es_valido: ### Si es valido, encontrara la tarea y dentrara al bucle del submenu, si no regrasa al inicio
                    tarea_a_modificar=obtener_tarea(Tareas, opcion_tarea)
                    while True:
                        mostrar_tarea(tarea_a_modificar)
                        opcion_submenu=pedir_opcion_submenu(tipo_tarea)
                        es_valido_submenu=verificar_opcion_submenu(opcion_submenu) ###Verificamos opcion de submenu
                        if es_valido_submenu:
                            modificacion=sel_modificacion(opcion_submenu)
                            modificar_tarea_sel(tarea_a_modificar, modificacion, opcion_submenu)
                            guardar_tareas(Tareas) ###guardamos cambios antes de seguir
                            if pregunta_continuacion(): ###en caso de ser true, continua en el submenu, en caso contrario saldra al menu
                                continue
                            break
                        continue###en caso de false, se reinicial el while submenu
                else:
                    print('ERROR, tarea inexistente')
                    continue




        elif opcion==4:
            while True:
                mostrar_tareas(Tareas)
                opcion=borrar_seleccion(Tareas)
                tarea_a_borrar=obtener_tarea(Tareas, opcion)
                mostrar_tarea(tarea_a_borrar)
                if confirmacion_borrar():
                    borrar_tarea(Tareas, opcion)
                    print('eliminado con exito, feliz dia')
                    confirmacion()
                    guardar_tareas(Tareas)
                    break
                break


        else:
            print('opcion invalida, por favor ingrese una opcion valida')
            confirmacion()
            continue


if __name__=="__main__":
    main()

