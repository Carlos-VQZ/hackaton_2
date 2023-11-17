import web

urls = (
    '/', 'mvc.controllers.public.login.Login',
    '/inicio', 'mvc.controllers.public.inicio.Inicio',
    '/trabajador/registro', 'mvc.controllers.trabajador.registro.Registro',
    '/empleador/registro_empleador', 'mvc.controllers.empleador.registro_empleador.Registro_empleador',
    '/migrante/registro_migrante', 'mvc.controllers.migrante.registro_migrante.Registro_migrante',
    '/empleador/home_empleador', 'mvc.controllers.empleador.home_empleador.Home_empleador',
    '/migrante/home_migrante', 'mvc.controllers.migrante.home_migrante.Home_migrante',

    
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()

    # '/migrante/home_migrante', 'mvc.controllers.migrante.home_migrante.Home_migrante',