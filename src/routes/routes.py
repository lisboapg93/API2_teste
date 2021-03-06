from urllib import response
from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
from werkzeug.utils import secure_filename
from api import app


UPLOAD_FOLDER = '/receives'
ALLOWED_EXTENSIONS = {'word', 'pdf'}


CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



users_data = {
}

#rota inicial
api = Api(app, 
    doc='/')


#rota read
@app.route("/users")
def list_users():
    return response_users()


#rota criar
@app.route("/users", methods=["POST"])
def create_users():
    body = request.json
    
    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1
    
    users_data[new_id] = {
        "id": new_id,
        "name": body["name"],
        "email": body["email"],
        "phone": body["phone"],
        "address": body["address"],
        "job": body["job"],
        "file": body["file"]
    }

    response = api.payload
    return response_users()

#rota update
@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")
    
    if user_id in users_data:
        users_data[user_id]["name"] = name
        
    return response_users()
        
#rota delete
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_data.get(user_id)
    
    if user:
        del users_data[user_id]
    
    return response_users()

def response_users():
    return {"users": list(users_data.values())}
 
#rota post arquivo
	
@app.route('/users', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(app.config['UPLOAD_FOLDER'], f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)

