import web
import json
import firebase_config as token
import pyrebase
from datetime import datetime

render = web.template.render("mvc/views/migrante/")

class Registro_migrante:
    def GET(self):
        try:
           return render.registro_migrante()
        except Exception as error:
            print("Error Registro_migrante: {}".format(error))
            return render.registro_migrante()
        
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input() #almacena los datos del formulario web
            nombre = formulario['nombre'] #almacena el email del formulario web
            apellido = formulario['apellido'] #almacena el no_control del formulario web
            telefono = formulario['telefono'] #almacena el nivel del formulario web
            correo = formulario['correo'] #almacena el password del formulario web
            fecha = formulario['dob'] #almacena el email del formulario web
            pais = formulario['country'] #almacena el email del formulario web
            description = formulario['description'] #almacena el email del formulario web
            password = formulario['contrasena'] #almacena el password del formulario web
            user = auth.create_user_with_email_and_password(correo, password) #crea el usuario en firebase
            
            data = { #crea el diccionario data
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'correo': correo,
                'fecha': fecha,
                'pais': pais,
                'description': description,
                'nivel':'migrante' 
            }    
            db.child('data').child('usuarios').child(user['localId']).set(data) #almacena el diccionario data en la base de datos
            return web.seeother('/')
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']['message']
            if (error == "EMAIL_EXISTS"):
                mensaje = "El correo ya existe"
                return render.agregar_usuario(mensaje)
            else:
                mensaje = "Error desconocido"
                return render.agregar_usuario(mensaje)