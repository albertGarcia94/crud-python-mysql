from flask import Flask,jsonify,request
import controlador

app=Flask(__name__)
#Lista del request

#CRUD PROFESORES
@app.route('/profesores',methods=['GET','POST','PUT','DELETE'])
def profesores():
    request_list = request.get_json()
    if request.method=='GET':
        return jsonify(controlador.get_profesores())
    if request.method=='POST':
        nombre = request_list["nombre"]
        apellido = request_list["apellido"]
        return jsonify(controlador.post_profesores(nombre,apellido))
    if request.method=='PUT':
        id_profesor = request_list["id_profesor"]
        nombre = request_list["nombre"]
        apellido = request_list["apellido"]
        return jsonify(controlador.put_profesores(id_profesor,nombre,apellido))
    if request.method=='DELETE':
        id_profesor= request_list["id_profesor"]
        return jsonify(controlador.delete_profesores(id_profesor))
        #Busqueda profesor por id
@app.route('/profesores/<int:id>')
def profesor_id(id):
   return jsonify(controlador.get_id_profesor(id))

if __name__ == '__main__':
    app.run(port=5000,debug=True)