import web
import app
import json
import firebase_config as token
import pyrebase
from datetime import datetime

render = web.template.render("mvc/views/public/")

class Login: #clase Index
    def GET (self): 
        try:  
            mensaje = None 
            return render.login(mensaje)
        except Exception as error: # error
            mensaje = None
            print("Error Login.GET: {}".format(error))
            return render.login(mensaje) 
        
    def POST(self): 
        try: 
            mensaje = None
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input() 
            email = formulario.email 
            password= formulario.password
            user = auth.sign_in_with_email_and_password(email, password) 
            tokens = user["idToken"]
            local_id =  (user ['localId'])
            web.setcookie('localid', local_id)
            web.setcookie('tokenUser', tokens)
            busqueda =  db.child("data").child("usuarios").child(user['localId']).get()
            if busqueda.val()['nivel'] == 'administrador' and busqueda.val()['status'] == "activo":
                actividad = "Ingreso al sistema"
                registro = {
                    "actividad": actividad,
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                db.child("data").child("usuarios").child(user['localId']).child("logs").push(registro)
                return web.seeother("/admin/lista-pozos")
            elif busqueda.val()['nivel'] == "operador" and busqueda.val()['status'] == "activo":
                actividad = "Ingreso al sistema"
                registro = {
                    "actividad": actividad,
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                db.child("data").child("usuarios").child(user['localId']).child("logs").push(registro)
                return web.seeother("/operador/lista-pozos")
            elif busqueda.val()['nivel'] == "informatica":
                actividad = "Ingreso al sistema"
                registro = {
                    "actividad": actividad,
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                db.child("data").child("usuarios").child(user['localId']).child("logs").push(registro)
                return web.seeother("/informatica/agregar-usuario")
            else:
                mensaje = "Usuario inactivo"
                return render.login(mensaje)
                    
        except Exception as error: # Error en formato JSON
            formato = json.loads(error.args[1])
            error = formato['error']
            mensaje = error['message']
            if mensaje == "EMAIL_NOT_FOUND":
                mensaje = "Correo no encontrado"
                return render.login(mensaje) 
            elif mensaje == "INVALID_PASSWORD":
                mensaje = "Contraseña incorrecta"
                return render.login(mensaje)