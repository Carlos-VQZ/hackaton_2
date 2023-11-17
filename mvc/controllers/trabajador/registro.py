import web
import json
import firebase_config as token
import pyrebase
from datetime import datetime

render = web.template.render("mvc/views/trabajador/")

class Registro:
    def GET(self):
        try:
           return render.registro()
        except Exception as error:
            print("Error Registro: {}".format(error))
            return render.registro()
     