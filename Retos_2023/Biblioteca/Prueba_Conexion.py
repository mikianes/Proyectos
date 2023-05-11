import pymysql

def conexion():
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='biblioteca')
        correcta = "Conexión correcta"
        return correcta
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        incorrecta = "Ocurrió un error al conectar: ", e
        return incorrecta
    

def main():
   conexion()
   
if __name__ == "__main__":
    main()  