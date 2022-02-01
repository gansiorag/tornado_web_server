import tornado.ioloop
from app import make_app


if __name__ == "__main__":
    app = make_app()
    address = 'localhost'
    port = 4556
    print(f' -- Start tornado server on adress {address}:{port} --')
    app.listen(address=address, port=port)
    tornado.ioloop.IOLoop.current().start()