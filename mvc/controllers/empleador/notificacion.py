import web

render = web.template.render("mvc/views/empleador/")

class Notificacion:
    def GET(self):
        try:
           return render.notificacion()
        except Exception as error:
            print("Error Notificacion.GET: {}".format(error))
            return render.notificacion()