from db import get_db

db = get_db()
cursor = db.cursor()

# _____________PROFESORES______________
# ______________________________________
def get_profesores():
    query="SELECT * FROM t_profesor"
    cursor.execute(query)
    return cursor.fetchall()
def post_profesores(nombre,apellido):
    
    query="INSERT INTO t_profesor(nombre,apellido) VALUES (%s,%s)"
    cursor.execute(query,[nombre,apellido])
    db.commit()
    return 'Guardo Exitoso'

def put_profesores(id_profesor,nombre,apellido):
    query_existe_usuario ="SELECT * FROM t_profesor WHERE id_profesor = %s"
    cursor.execute(query_existe_usuario, [id_profesor])
    existeProfesor = cursor.fetchone()
    if existeProfesor == None:
        return'Profesor no Existe'

    query="UPDATE t_profesor SET nombre = %s, apellido = %s WHERE (id_profesor = %s)"
    cursor.execute(query,[nombre,apellido,id_profesor])
    db.commit()
    return 'Actualizado Exitoso'

def delete_profesores(id_profesor):
    query="DELETE FROM t_profesor WHERE id_profesor=%s"
    cursor.execute(query,[id_profesor])
    db.commit()
    return 'Borrado Exitoso'

def get_id_profesor(id):
    query= "SELECT * FROM t_profesor WHERE id_profesor = %s"
    cursor.execute(query,[id])
    return cursor.fetchone()
