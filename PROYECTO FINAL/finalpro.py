#PROYECTO FINAL - MARLON VILLALONA - 2019-9057 - FUNDAMENTOS DE PROGRAMACION   -----
'''----------------------------------------------'''
#IMPORTACIONES
import os
import csv
import pandas as pd
import smtplib
import yagmail
from datetime import date
import pe 

datos = []

epidemias = ['Covid-19','Lepra','Colera','Dengue','Diarrea','Ebola','Malaria','Neumonia','Sarampion','Tuberculosis','VIH/SIDA']

hospitales = ['Hospiten Santo Domingo','Hospital Regional Doctor Marcelino Vélez Santa','Day Hospital','Hospital General Plaza de la Salud',
        'Hospital Central de las Fuerzas Armadas','Hospital Pediátrico Robert Reid Cabral','Hospital Materno Infantil Santo Socorro']

provincias = ['Azua', 'Bahoruco', 'Barahona', 'Dajabón' 'Distrito Nacional','Duarte','Elías Piña','El Seibo','Espaillat','Hato Mayor','Hermanas Mirabal',
              'Independencia','La Altagracia','La Romana','La Vega','María Trinidad Sánchez','Monseñor Nouel','Monte Cristi','Monte Plata','Pedernales',
                 'Peravia', 'Puerto Plata','Samaná','San Cristóbal','San José de Ocoa','San Juan','San Pedro de Macorís','Sánchez Ramírez','Santiago',
                 'Santiago Rodríguez','Santo Domingo' ]


def clean():
    os.system('cls')

print('PROGRAMA PARA REGSITRAR CASOS')
print()


#Validar numero
def numero(mensaje):
    tmp = 0
    try:
        tmp = int(input(mensaje))
    except:
        print('No es un numero')
        tmp = numero(mensaje)
    return tmp


#Validar archivo
def crear():
    exists = os.path.isfile('final.csv')
    if not exists:
        f = open('final.csv','w')
        f.write('Nombre','Apellido','Telefono','Email','Fecha','Cedula','Hospital','Provincia','Enfermedad','Comentario')

crear()

#Funcion exportar
def exportar():
    exp = pd.read_csv('final.csv')
    html = exp.to_html()
    f = open('final.html','w')
    f.write(html)
    f.close

    html = '''
     <html> 
    <head>
     <title> LISTADO DE CASOS </title>
    </head>

    <body>

    <center> @exp </center>

    </body>




    </html>'''

#Funcion agregar
def agregar():
    clean()
    add = []
    os.system('AGREGARCASO.mp3')
    print('Agregar caso')

    add.append(input('Ingrese el nombre: '))
    add.append(input('Ingrese el apellido: '))
    Telefono = numero('Ingrese el telefono: ')
    add.append(Telefono)
    add.append(input('Ingrese su email: '))
    anio = numero('Ingrese el año de nacimiento: ')
    mes = numero('Ingrese el mes de nacimiento: ')
    while mes > 12 and mes <1:
        mes = numero('Fuera de rango, intente de nuevo: ') 
    dia = numero('Inserte el dia de nacimiento: ')
    while dia > 31 or dia < 1:
        dia = numero('Fuera de rango, intente de nuevo: ')
    fecha = date(anio,mes,dia)
    add.append(fecha)
    cedula = numero('Ingrese la cedula: ')
    add.append(cedula)
    print(hospitales)
    add.append(input('Ingrese el hospital: '))
    add.append(input('Ingrese la provinicia: '))
    print(epidemias)
    add.append(input('Ingrese la enfermedad: '))
    add.append(input('Ingrese un comentario: '))

    input('Caso agregado. Presione cualquier tecla para volver al menu.')
    return add
    

#Funcion Mostrar
def mostrar():
    i = 0
    print('Indice \t Nombre \t Apellido \t Telefono \t Email \t Fecha de Nacimiento \t Cedula \t Hospital \t Provincia \t Enfermedad \t Comentario')
    for add in datos:
        print(f'{i}\t {add[0]} \t {add[1]} \t {add[2]}\t {add[3]}\t {add[4]}\t {add[5]}\t {add[6]}\t {add[7]}\t {add[8]}\t {add[9]}')
        i += 1

#Funcion modificar
def modificar():
    if len(datos) ==0:
        input('No existe caso, presione enter para voler al menu')
    else:
        mostrar()
        os.system('MODIFICAR.mp3')
        opt = numero('Inserte fila que desea modificar')
        while opt > len(datos):
            opt = numero('Error, intentelo de nuevo: ')
        print(datos[opt])
        print('Opciones a modificar\n')
        print('1. Nombre')
        print('2. Apellido')
        print('3. Telefono')
        print('4. Email')
        print('5. Fecha de Nacimiento')
        print('6. Cedula')
        print('7. Hospital')
        print('8. Provincia')
        print('9. Enfermedad')
        print('10. Comentario')

        choose = numero('Ingrese la opcion deseada: ')
        while choose > 11 or choose < 1:
            choose = numero('Error, intente de nuevo: ')
        if choose ==1:
            nombre = input('Ingrese el nuevo nombre: ')
            datos[opt][0] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==2:
            nombre = input('Ingrese el nuevo apellido: ')
            datos[opt][1] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==3:
            nombre = input('Ingrese el nuevo telefono: ')
            datos[opt][2] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==4:
            nombre = input('Ingrese el nuevo email: ')
            datos[opt][3] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==5:
            anio = numero('Ingrese el  nuevo año de nacimiento: ')
            mes = numero('Ingrese el nuevo mes de nacimiento: ')
            while mes >12 or mes <1:
                mes = numero('Fuera de rango, pruebe otra vez')
            dia = numero('Ingrese nuevo dia de nacimiento: ')
            while dia > 31 or dia <1:
                dia = numero('Error, intente de nuevo: ')
            nombre = date(anio,mes,dia)
            datos[opt][4] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==6:
            nombre = input('Ingrese la nueva cedula: ')
            datos[opt][5] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==7:
            print(hospitales)
            print('\n')
            nombre = input('Ingrese el nuevo hospital: ')
            datos[opt][6] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==8:
            nombre = input('Ingrese la nueva provinicia: ')
            datos[opt][7] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==9:
            print(epidemias)
            print('\n')
            nombre = input('Ingrese la nueva enfermedad: ')
            datos[opt][8] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        elif choose ==10:
            nombre = input('Ingrese el nuevo comentario: ')
            datos[opt][9] = nombre
            input('Opcion cambiada exitosamente, presione cualquier tecla para continuar.')
        
#Funcion eliminar
def eliminar():
    if len(datos) == 0:
        input('No existen casos, presione enter para volver.')
    else:
        mostrar()
        os.system('ELIMINAR.mp3')
        opt = numero('Ingrese fila que desea eliminar')
        while opt > len(datos):
            opt = numero('Error, ingrese la opcion nuevamente: ')
        del datos[opt]


#Menu del programa
def menu():
    os.system('MENU.mp3')
    print('1. Casos')

    print('    a. Agregar')
    print('    b. Editar')
    print('    c. Eliminar\n')



    print('2. Estadisticas\n')

    print('    a. Listado de casos por hospitales')
    print('    b. Listado de casos por epidemia')
    print('    c. Listado de casos por Provincia')
    print('    d. Listado de casos por mes de cumpleaños')
    print('    e. Exportar caso a HTML\n')

    print('3. Notificacion\n')

    print('4. Configuracion\n')

    print('5. Salir\n')

    option = input('Ingrese la opcion deseada: ')
    
    if option == '1':
        option_casos = input('Cual opcion desea elegir: ')

        if option_casos == 'a' or option_casos == 'A':
            clean()
            datos.append(agregar())
            df = pd.DataFrame(datos, columns=['Nombre','Apellido','Telefono','Email','Fecha','Cedula','Hospital','Provincia','Enfermedad','Comentario'])
            df.to_csv('final.csv')



        elif option_casos == 'b' or option_casos == 'B':
            clean()
            modificar()
            df = pd.DataFrame(datos, columns=['Nombre','Apellido','Telefono','Email','Fecha','Cedula','Hospital','Provincia','Enfermedad','Comentario'])
            df.to_csv('final.csv')
            

        elif option_casos == 'c' or option_casos == 'C':
            clean()
            eliminar()
            df = pd.DataFrame(datos, columns=['Nombre','Apellido','Telefono','Email','Fecha','Cedula','Hospital','Provincia','Enfermedad','Comentario'])
            df.to_csv('final.csv')

            
        else:
            input('Debe ser una opcion valida. Intente de nuevo')
            menu()

    if option == '2':
        clean()
        mostrar()
        
        
        print('a. Lista de casos por Hospitales. \n')
        print('b. Lista de casos por Epidemia. \n')
        print('c. Lista de casos por Provincia. \n')
        print('d. Lista de pacientes por mes de cumpleaños . \n')
        print('e. Exportar caso a HTML. \n')

        opt = input('Eliga la opcion deseada: ')

        if opt == 'a' or opt == 'A':
            clean()
            i = 0
            print('\t Hospitales ')
            for add in datos:
                print(f'{add[6]}\t')
                i += 1

                print('Casos registrados por hospitales \n')

                input('Presione ENTER para volver')
        
        

        elif opt == 'b' or opt == 'B':
            clean()
            i = 0 
            print('\t Epidemias ')
            for add in datos:
                print(f'{add[8]}\t')
                i += 1

                print('Casos por epidemias \n')

                input('Presione ENTER para volver al menu')
        

        elif opt == 'c' or opt == 'C':
            clean()
            i = 0 
            print('\t Provincias ')
            for add in datos:
                print(f'{add[7]}\t')
                i += 1

                print('Casos por provincia \n')

                input('Presione ENTER para volver al menu')


        elif opt == 'd' or opt == 'D':
            clean()
            i = 0
            print('\t Mes de nacimiento ')
            for add in datos:
                print(f'{add[5]}\t')
                i += 1

                print('Casos por mes de nacimiento \n')

                input('Presione ENTER para volver al menu')

        elif opt == 'e' or opt == 'E':
            exportar()
            os.system('CASOEXPORTADO.mp3')

            input('Caso exportado, presione ENTER para volver al menu')
            


        else:
            input('Debe ser una opcion valida, intente de nuevo.')
            menu()

    #Envio de correo
    if option == '3':
        clean()
        os.system('CORREO.mp3')
        correodeusuario = input('Ingrese el correo: ')

        #Validacion del correo
        if "@gmail" in correodeusuario or "@hotmail" in correodeusuario or "@live" in correodeusuario or "@yahoo" in correodeusuario or "outlook" in correodeusuario:


            correo = yagmail.SMTP('iamvillalona2017@gmail.com',open('contra.txt').read())

            correo.send(to = correodeusuario, subject='Listado de casos reportados',contents='final.csv')

            input('Enviado correctamente! ... Presione cualquier tecla para volver el MENU.')
            menu()

        else:
	        input("No es válido, presione ENTER para volver al menu")
        menu()


    if option == '4':
        clean()
        os.system('LISTADO.mp3')

        #Listas de Epidemias, Provinicias y Hospitales
        print('a. Epidemias')
        print('b. Provincias')
        print('c. Hospitales')

        opcion = input('Ingrese la opcion deseada: ')

        if opcion == 'a':
            print('1. Agregar')
            print('2. Modificar')
            print('3. Eliminar')
            
            opc = input('Que desea? ')

            if opc == '1':
                opcagregar = input('Ingrese la epidemia que desee agregar: ')

                epidemias.append(opcagregar)

                input('Epidemia agregada correctamente, presione ENTER para volver a menu.')
                menu()

            elif opc == '2':
                print(epidemias)
                print('')

                mod = input('Cual desesa modificar: ')

                mod2 = input('Ingrese dato a cambiar: ')

                completo = mod - 1

                epidemias[completo] = mod2
            
                input('Se modifico correctamente, presione ENTER para volver al menu.')
                menu()

            elif opc == '3':
                print(epidemias)
                print('')

                delete = input('Cual desea eliminar: ')

                elim = delete - 1

                del epidemias[elim]

                input('Eliminado correctamente, presione ENTER para volver al menu')
                menu()

        if opcion == 'b':
            print('1. Agregar')
            print('2. Modificar')
            print('3. Eliminar')
            
            opc = input('Que desea? ')

            if opc == '1':
                opcagregar = input('Ingrese la epidemia que desee agregar: ')

                provincias.append(opcagregar)

                input('Epidemia agregada correctamente, presione ENTER para volver a menu.')
                menu()

            elif opc == '2':
                print(provincias)
                print('')

                mod = input('Cual desesa modificar: ')

                mod2 = input('Ingrese dato a cambiar: ')

                completo = mod - 1

                provincias[completo] = mod2
            
                input('Se modifico correctamente, presione ENTER para volver al menu.')
                menu()

            elif opc == '3':
                print(provincias)
                print('')

                delete = input('Cual desea eliminar: ')

                elim = delete - 1

                del provincias[elim]

                input('Eliminado correctamente, presione ENTER para volver al menu')
                menu()


        if opcion == 'c':
            print('1. Agregar')
            print('2. Modificar')
            print('3. Eliminar')
            
            opc = input('Que desea? ')

            if opc == '1':
                opcagregar = input('Ingrese la epidemia que desee agregar: ')

                hospitales.append(opcagregar)

                input('Epidemia agregada correctamente, presione ENTER para volver a menu.')
                menu()

            elif opc == '2':
                print(hospitales)
                print('')

                mod = input('Cual desesa modificar: ')

                mod2 = input('Ingrese dato a cambiar: ')

                completo = mod - 1

                hospitales[completo] = mod2
            
                input('Se modifico correctamente, presione ENTER para volver al menu.')
                menu()

            elif opc == '3':
                print(hospitales)
                print('')

                delete = input('Cual desea eliminar: ')

                elim = delete - 1

                del hospitales[elim]

                input('Eliminado correctamente, presione ENTER para volver al menu')
                menu()

    if option == '5':
        os.system('SALIR.mp3')
        input('Gracias por utilizar el programa. Presione cualquier letra para salir.')

    else:
        print('Debe ser una opcion valida. Intente de nuevo')
        menu()    


#Guarda datos registrados por el Usuario en el CSV
dtmp = pd.read_csv('final.csv')
tmp = dtmp.values.tolist()
for lin in tmp:
    t = []
    t.append(lin[1])
    t.append(lin[2])
    t.append(lin[3])
    t.append(lin[4])
    t.append(lin[5])
    t.append(lin[6])
    t.append(lin[7])
    t.append(lin[8])
    t.append(lin[9])
    t.append(lin[10])
    datos.append(t)

menu()    


#PROYECTO FINAL - MARLON VILLALONA - 2019-9057 - FUNDAMENTOS DE PROGRAMACION   ------

