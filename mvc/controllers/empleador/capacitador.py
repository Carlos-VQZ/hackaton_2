import web

render = web.template.render("mvc/views/empleador/")

class Capacitador:
    def GET(self):
        try:
           return render.capacitador()
        except Exception as error:
            print("Error Capacitador.GET: {}".format(error))
            return render.capacitador()