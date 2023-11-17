import web

render = web.template.render("/")

class Salir:
    def GET(self):
        try:
           return render.salir()
        except Exception as error:
            print("Error Salir.GET: {}".format(error))
            return render.salir()