Este código crea una aplicación web interactiva utilizando Streamlit, donde se presenta un menú lateral que permite elegir entre diferentes funciones, como la suma de dos números, el cálculo del área de un triángulo, una calculadora flexible, y más.

Menú de opciones:
menu_opciones = ['Inicio', 'Suma de dos numeros', ...]
seleccionar_opcion = st.sidebar.selectbox('Opciones', menu_opciones)

Aquí se define un menú con diferentes opciones, que se mostrará en la barra lateral (sidebar). El usuario puede seleccionar una opción y esa elección se guardará en la variable seleccionar_opcion.

Funciones:

Saludar:
def saludar():
    nombre = st.text_input('Ingresa tu nombre')
    if nombre:
        st.text(f'Hola {nombre}, pasala bien')
        
Esta función pide al usuario su nombre y lo saluda si se ha ingresado un valor.

Sumar dos números:
def sumar()->float:
    a = st.number_input('Ingrese el primer numero')
    b = st.number_input('Ingrese el segundo numero')
    suma = a + b
    st.write(f'El resultado es: {suma}')
    
Se ingresan dos números y se muestra su suma.

Área de un triángulo:
def calcular_area_triangulo()->float:
    base = st.number_input('Ingrese el valor de la base del triangulo')
    altura = st.number_input('Ingrese el valor de la altura del triangulo')
    if base <= 0 or altura <= 0:
        st.error('El valor no puede ser 0 o menor')
    else:
        area = (1/2) * base * altura
        st.write(f'El area del triangulo es: {area} metros cuadrados')
        
Calcula el área de un triángulo con base y altura dadas, validando que los valores sean mayores que cero.

Calculadora de descuento:
def calcular_precio_final()->float:
    precio = st.number_input('Ingrese el precio del producto')
    pedir_descuento = st.number_input('Ingrese el descuento del producto', min_value= 10.0, max_value= 100.0 )
    pedir_impuesto = st.number_input('Ingrese el impuesto',min_value= 16.0, max_value= 100.0)
    descuento = precio * (pedir_descuento / 100)
    impuesto = precio * (pedir_impuesto / 100)
    precio_final = (precio - descuento) + impuesto
    st.write(f'El precio final es: {precio_final}')
    
Calcula el precio final de un producto aplicando un descuento y sumando un impuesto.

Suma de una lista de números:
def sumar_lista(n:list)->float:
    suma = sum(n)
    st.write(f'La lista de numeros es: {n}')
    st.write(f'La suma de la lista es: {suma}')
    
Muestra una lista de números y calcula su suma.

Multiplicación con *args:
def multiplicar_todos(*n):
    resultado = 1
    for num in n:
        resultado *= num
    st.write(f'El resultado de la multiplicacion es: {resultado}')
    
Multiplica una lista de números utilizando el operador *args para recibir un número variable de argumentos.

Información personal con **kwargs:
def informacion_personal(**informacion):
    for clave, valor in informacion.items():
        st.write(f'{clave} : {valor}')

Usa **kwargs para recibir información personal (nombre, edad, etc.) como pares clave-valor y mostrarla.

Calculadora flexible con match:
def calculadora_flexible():
    while True:
        opcion = st.number_input('Ingrese el numero de la operacion', min_value= 1, max_value= 5)
        match opcion:
            case 1: # Suma
            case 2: # Resta
            case 3: # Multiplicación
            case 4: # División
            case 5: # Salir
            
Proporciona una calculadora con varias operaciones usando match para manejar las opciones seleccionadas.

Ejecución según la opción seleccionada:
match seleccionar_opcion:
    case 'Inicio':
        st.title('Se Bienvenid@ a mi pagina')
        saludar()
    case 'Suma de dos numeros':
        sumar()
    ...
Dependiendo de la opción que el usuario seleccione en la barra lateral, se ejecutará una función específica.
