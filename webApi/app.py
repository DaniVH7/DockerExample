import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):

        return 'Hello papi'

if __name__ == "__main__":
    app.run()