import web

urls = (
    '/', 'mvc.controllers.public.login.Login',
    
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()