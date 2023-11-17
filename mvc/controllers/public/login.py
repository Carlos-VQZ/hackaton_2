import web
import json
import firebase_config as token
import pyrebase
from datetime import datetime

render = web.template.render("mvc/views/public/")

class Login:
    def GET(self):
        try:
            return render.login()
        except Exception as error:     
            print("Error Login.GET: {}".format(error))
            return render.login() 
        
    def POST(self):
        try:
            
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input() 
            email = formulario['email']
            password = formulario['password']
            user = auth.sign_in_with_email_and_password(email, password) 
            tokens = user["idToken"]
            local_id = user['localId']
            web.setcookie('localid', local_id)
            web.setcookie('tokenUser', tokens) 

            busqueda = db.child("data").child("usuarios").child(user['localId']).get()

            if busqueda.val() and busqueda.val().get('nivel') == 'empleador':
                return web.seeother("/empleador/home_empleador")
            elif busqueda.val() and busqueda.val().get('nivel') == "migrante":
                # Si el usuario es un migrante, redirige a la página de inicio de migrante
                return web.seeother("/migrante/home_migrante")
            else:
                # Si el nivel no coincide con ninguno, el usuario no está autorizado o es inactivo.
                mensaje = "Acceso no autorizado o usuario inactivo"
                return render.login(mensaje)
                    
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            mensaje = error['message']
            
            if mensaje == "EMAIL_NOT_FOUND":
                mensaje = "Correo no encontrado"
            elif mensaje == "INVALID_PASSWORD":
                mensaje = "Contraseña incorrecta"
            
            return render.login(mensaje)


