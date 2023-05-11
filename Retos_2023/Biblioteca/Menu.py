import Prueba_Conexion, Add

def main():
    
    print("Prueba de Conexión")
    resultado = Prueba_Conexion.conexion()
    print(resultado)
    print("------")
    print("prueba de insert")
    resultado = Add.insertar_autor("Maria")
    if resultado != "None":
        print(resultado)
    
    
if __name__ == "__main__":
    main()  