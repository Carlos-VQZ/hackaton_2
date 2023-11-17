import web

render = web.template.render("mvc/views/empleador/")

class Inicio:
    def GET(self):
        try:
           return render.inicio()
        except Exception as error:
            print("Error Inicio.GET: {}".format(error))
            return render.inicio()