"""/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
 * - Host: mysql-5707.dinaserver.com
 * - Port: 3306
 * - User: mouredev_read
 * - Password: mouredev_pass
 * - Database: moure_test
 * 
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 */"""
 
 
import pymysql

def conexion():
    try:
        conexion = pymysql.connect(host='mysql-5707.dinaserver.com',
                                port=3306,
                                user='mouredev_read',
                                password='mouredev_pass',
                                db='moure_test')
        correcta = "Conexión correcta"
        return correcta
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        incorrecta = "Ocurrió un error al conectar: ", e
        return incorrecta
 
def select():
    try:
        conexion = pymysql.connect(host='mysql-5707.dinaserver.com',
                                port=3306,
                                user='mouredev_read',
                                password='mouredev_pass',
                                db='moure_test')
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM `challenges`;"
                #Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta)
            print(cursor.fetchall())
        finally:
            conexion.close()
            correcta = "Consulta correcta"
            return correcta
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        incorrecta = "Ocurrió un error al conectar: ", e
        return incorrecta   

def main():
   print(conexion())
   print(select())
   
if __name__ == "__main__":
    main()  