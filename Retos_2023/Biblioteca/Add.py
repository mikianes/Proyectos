import pymysql



def insertar_autor(autor):
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='biblioteca')
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO autor(nombre) VALUES (%s);"
                #Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, (autor))
            conexion.commit()
        finally:
            conexion.close()
            correcta = "Inserción correcta"
            return correcta
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        incorrecta = "Ocurrió un error al conectar: ", e
        return incorrecta
        

def insertar_libro():
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='biblioteca')
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
                #Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, ("Volver al futuro 1", 1985))
                cursor.execute(consulta, ("Ready Player One", 2018))
                cursor.execute(consulta, ("It", 2017))
                cursor.execute(consulta, ("Pulp Fiction", 1994))
            conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)