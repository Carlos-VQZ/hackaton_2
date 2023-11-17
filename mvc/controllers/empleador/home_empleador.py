import web

render = web.template.render("mvc/views/empleador/")

class Home_empleador:
    def GET(self):
        try:
           return render.home_empleador()
        except Exception as error:
            print("Error Home_empleador.GET: {}".format(error))
            return render.home_empleador()