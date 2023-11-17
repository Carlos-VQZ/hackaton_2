import web

render = web.template.render("mvc/views/migrante/")

class Home_migrante:
    def GET(self):
        try:
           return render.home_migrante()
        except Exception as error:
            print("Error Home_migrante.GET: {}".format(error))
            return render.home_migrante()