import pandas as pd

from clase import *
from fuzzywuzzy import fuzz

# Ejercicio 1:
# Completar el método is_hot_in_pehuajo con el siguiente objetivo:
# Consultar la información de clima y devolver True si la temperatura actual
# supera los 28 grados celsius o False caso contrario. Esto implica incluso
# devolver False ante cualquier excepción http.

def consultar_temperatura():

    try:
        
        geo = GeoAPI()

        rta, data = geo.is_hot_in_pehuajo()

        if rta:
            
            print(f"La temperatura actual es: {data['temp']}, y habrá una máxima prevista de: {data['temp_min']}, con una mínima prevista de: {data['temp_max']}")
            print("Que sea doble!")
            
        else:
            
            print(f"La temperatura actual es: {data['temp']}, y habrá una máxima prevista de: {data['temp_min']}, con una mínima prevista de: {data['temp_max']}")
            print("Nunca viene mal un buen helado!")
            
    except Exception as e:
        print(e)
        return False
            
# Ejercicio 2.1:
# Dadas las variables: product_name y quantity, complete la función
# is_product_available con el siguiente objetivo:
# Buscar en un pandas DataFrame y devolver True si existe stock, False caso
# contrario.

# Ejercicio 2.2:
# Si miramos el diagrama de flujo al momento de la decisión de stock, encontramos un
# potencial loop infinito, ya que el usuario podría continuar ingresando productos
# inválidos o sin stock. Reformule la función para solucionar este problema. 

# Solución Propuesta
# Se listan al comienzo los productos con su stock disponible
# Si el usuario ingresa un producto no reconocido, la función retorna "Producto no reconocido"
# Si el usuario ingresa un stock superior al actual, la función retorna "Stock no disponible"
        
def is_product_available():

    _PRODUCT_DF = pd.DataFrame({
    "product_name": ["chocolate", "granizado", "limon", "dulce de leche"],
    "quantity": [3, 10, 0, 5]
    })
        
    try:
        
        print("Estos son nuestros productos y su stock actual")  

        for index, row in _PRODUCT_DF.iterrows():
            
            print(f"{row['product_name']}, Stock: {row['quantity']}")
            
        while True:
            
            product_name = input("Ingrese su pedido: ")
            
            if product_name.lower() in _PRODUCT_DF.values:
                    
                stock_producto = _PRODUCT_DF.loc[_PRODUCT_DF["product_name"] == product_name.lower(), "quantity"].values[0]
                
                if stock_producto != 0:
                                    
                    while True:
                        
                        pedido = input("Ingrese la cantidad requerida: ")
                        
                        if pedido.isdigit():
                            
                            if int(pedido) <= stock_producto:
                                                
                                return True
                                
                            else:
                                
                                print("No hay suficiente stock")
                        else:
                            
                            print("Cantidad invalida")
                else:
                    
                    print("Nos hemos quedado sin stock del producto ingresado. Disculpas.")
                
            else:
                
                print("Producto no reconocido")
            
    except Exception as e:
        print(e)
        return False


# Ejercicio 3:
# Completar la función validate_discount_code con el siguiente objetivo:
# Dada la lista de códigos de descuento vigentes y un código de descuento
# mencionado por el cliente, devuelve True si la diferencia entre el código
# mencionado y los códigos vigentes es menor a tres caracteres, en al menos
# uno de los casos.
# Por diferencia se entiende: caracteres que están presentes en el código brindado, pero
# no en el código evaluado de la lista o viceversa 

def validate_discount_code():

    _AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

    try:
        
        while True:
        
            codigo = input("¿Cuenta con algun código de descuento? ")
            
            if codigo.lower() == "si" or codigo.lower() == "sí":
                
                while True:
                    
                    cod_dscto = input("Ingrese su código de descuento: ")
                
                    for codigo in _AVAILABLE_DISCOUNT_CODES:
                        
                        similitud = fuzz.ratio(cod_dscto.lower(), codigo.lower())
                        
                        if similitud > 82:
                            
                            return True, True
                    
                    print('Código erroneo. Intente nuevamente')    
                
            elif codigo.lower() == "no":
                
                return True, False      
    
    except Exception as e:
        print(e)
        return False