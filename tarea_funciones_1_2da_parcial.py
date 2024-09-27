import streamlit as st

menu_opciones = ['Inicio','Suma de dos numeros','Area de un triangulo','Calculadora de descuento','Suma de una lista de numeros','Funciones con valores predeterminados','Numeros pares e impares','Multiplicacion con args','Informacion de una persona con kwargs','Calculadora flexible']

seleccionar_opcion = st.sidebar.selectbox('Opciones',menu_opciones)


def saludar():
    nombre = st.text_input('Ingresa tu nombre')
    if nombre:
        st.text(f'Hola {nombre} pasala bien')
    
def sumar()->float:
    a = st.number_input('Ingrese el primer numero')
    b = st.number_input('Ingrese el segundo numero')
    suma = a + b
    st.write(f'El resultado es: {suma}')

def calcular_area_triangulo()->float:
    base = st.number_input('Ingrese el valor de la base del triangulo')
    altura = st.number_input('Ingrese el valor de la altura del triangulo')
    if base <= 0:
        st.error('El valor no puede ser 0 o menor')
    elif altura <= 0:
        st.error('El valor no puede ser 0 o menor')
    else:
        area = (1/2) * base * altura
        st.write(f'El area del triangulo es: {area} metros cuadrados')


def calcular_precio_final()->float:
    precio = st.number_input('Ingrese el precio del producto')
    pedir_descuento = st.number_input('Ingrese el descuento del producto', min_value= 10.0, max_value= 100.0 )
    pedir_impuesto = st.number_input('Ingrese el impuesto del producto',min_value= 16.0, max_value= 100.0)
    descuento = precio * (pedir_descuento / 100)
    impuesto = precio * (pedir_impuesto / 100)
    precio_final = (precio - descuento) + impuesto
    st.write(f'El precio final es: {precio_final}')

def sumar_lista(n:list)->float:
    suma = 0
    for i in n:
        suma += i
    
    st.write(f'La lista de numeros es: {n}')
    st.write(f'La suma de la lista de numeros es: {suma}')

def producto():
    nombre_producto = st.text_input('Ingrese el nombre del producto')
    cantidad = st.number_input('Ingrese la cantidad de producto',min_value=1)
    precio_u = st.number_input('Ingrese el precio del producto por unidad', min_value= 1)
    precio_t = cantidad * precio_u
    st.write(f'El precio total de {cantidad}  {nombre_producto} es: {precio_t} pesos')

def numeros_pares_e_impares():
    pares = []
    impares = []
    numeros = [1,2,3,4,5]
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    st.write(f'La lista de numeros es: {numeros}')
    st.write(f'Los numeros pares son {pares}')
    st.write(f'Los numeros impares son {impares}')

def  multiplicar_todos(*n):
    resultado = 1
    for num in n:
        resultado *= num

    st.write(f'El resultado de la multiplicacion es: {resultado}')

def informacion_personal(**informacion):
    for clave, valor in informacion.items():
        st.write(f'{clave} : {valor}')

def menu_calculadora():
    st.text('Menu')
    st.text('Opciones')
    st.text('1. Suma')
    st.text('2. Resta')
    st.text('3. Multiplicacion')
    st.text('4. Division')
    st.text('5. Salir')


def calculadora_flexible():
    menu_calculadora()
    while True:
       opcion = st.number_input('Ingrese el numero de la operacion', min_value= 1, max_value= 5)
       
       match opcion:
        case 1:
            num1 = st.number_input('Ingrese el primer numero',key= 'num1_suma')
            num2 = st.number_input('Ingrese el segundo numero',key= 'num2_suma')
            st.write(f'El resultado de la suma es: {num1 + num2}')
        case 2: 
            num1 = st.number_input('Ingrese el primer numero',key= 'num1_resta')
            num2 = st.number_input('Ingrese el segundo numero',key= 'num2_resta')
            st.write(f'El resultado de la resta es: {num1 - num2}')
        case 3:
            num1 = st.number_input('Ingrese el primer numero', key='num1_multi')
            num2 = st.number_input('Ingrese el segundo numero', key='num2_multi')
            st.write(f'El resultado de la multiplicacion es: {num1 * num2}')
        case 4: 
            num1 = st.number_input('Ingrese el primer numero', key='num1_divi')
            num2 = st.number_input('Ingrese el segundo numero', key='num2_divi')
            if num2 == 0:
                st.text('Error, el segundo numero no puede ser 0')
            else:
                res = round(num1 / num2,2)
                st.write(f'El resultado de la divison es: {res}')
        case 5:
            st.text('Gracias por usar la calculadora')
            break

match seleccionar_opcion:
    case 'Inicio':
        st.title('Se Bienvenid@ a mi pagina')
        st.subheader('Disfruta de sus funciones')
        saludar()
    case 'Suma de dos numeros':
        st.title('Funcion para sumar dos numeros')
        sumar()
    case 'Area de un triangulo':
        st.title('Area de un Triangulo')
        calcular_area_triangulo()
    case 'Calculadora de descuento':
        st.title('Calculadora de descuento')
        calcular_precio_final()
    case 'Suma de una lista de numeros':
        st.title('Suma de una lista de numeros')
        sumar_lista(([1,2,3,4,5]))
    case 'Funciones con valores predeterminados':
        st.title('Funciones con valores predeterminados')
        producto()
    case 'Numeros pares e impares':
        st.title('Numeros pares e impares')
        numeros_pares_e_impares()
    case 'Multiplicacion con args':
        st.title('Multiplicacion con args')
        multiplicar_todos(1,2,3,4,5)
    case 'Informacion de una persona con kwargs':
        st.title('Informacion de una persona con kwargs')
        informacion_personal(nombre = ['Juan','Rene','Daniel'], edad = [18,24,25],direccion = ['Juan Jose Rios','Albarrada','Centro'])
    case 'Calculadora flexible':
        st.title('Calculadora flexible')
        calculadora_flexible()




            


    
       
       

      























