import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__", debug=True)

if __name__ == "__main__":
    app = make_app()
    address = 'localhost'
    port = 4556
    print(f' -- Start tornado server on adress {address}:{port} --')
    app.listen(address=address, port=port)
    tornado.ioloop.IOLoop.current().start()