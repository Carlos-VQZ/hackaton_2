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
            email = formulario.email 
            password = formulario.password
            user = auth.sign_in_with_email_and_password(email, password) 
            tokens = user["idToken"]
            local_id = user['localId']
            web.setcookie('localid', local_id)
            web.setcookie('tokenUser', tokens) 

            # Aquí se puede agregar la lógica para redirigir según el tipo de usuario (empleador o migrante)
            if  vce(local_id):
                return web.seeother("/empleador/dashboard")
            elif vcm(local_id):
                return web.seeother("/migrante/dashboard")
            else:
                # Si no es ni empleador ni migrante, redirecciona a una página por defecto o muestra un mensaje de error
                return render.error_page("No tiene acceso como empleador ni como migrante.")
         
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            mensaje = error['message']
            
            if mensaje == "EMAIL_NOT_FOUND":
                mensaje = "Correo no encontrado"
            elif mensaje == "INVALID_PASSWORD":
                mensaje = "Contraseña incorrecta"
            
            return render.login()


