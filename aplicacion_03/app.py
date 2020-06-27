import web

urls = (
    '/', 'application.controllers.formulario.Formulario',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()