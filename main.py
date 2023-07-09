from ejecicios import *

# El cliente Heladerías Frozen SRL nos solicita la construcción de un bot para la toma de
# pedidos. Usted forma parte del equipo asignado a este proyecto y tiene como
# responsabilidad el desarrollo de funciones auxiliares que le darán al bot la capacidad
# de desenvolverse en la conversación.

def bot_pedidos():
    
    try:
        
        print("¡Bienvenido a Heladerías Frozen!")
        
        consultar_temperatura()
        
        print("¿Le tomo su pedido?")  
                      
        is_product_available()
                
        result, codigo = validate_discount_code()
            
        if result:
            
            if codigo:
                
                print("Descuento aplicado, disfrute su pedido!")
                
            else:
                
                print("Disfrute su pedido!")
                 
    except Exception as e:
        print(e)
        return False
   
    
bot_pedidos()




