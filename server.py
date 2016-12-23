from pyfirmata import Arduino
import tornado.ioloop
import tornado.web
import tornado
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")

    def post(self):
        #new_value = int(self.get_argument("input1"))
        #print("The new value is {}".format(new_value))
        self.redirect("/")

class UpdateHandler(tornado.web.RequestHandler):
    def get(self):
        args = { k: self.get_argument(k) for k in self.request.arguments }
        print(args)
        if args["switch1"] == "on":
            board.digital[13].write(1)
        elif args["switch1"] == "off":
            board.digital[13].write(0)
        else:
            pass

def make_app():
    settings = {'debug': False,
                "static_path": os.path.join(os.path.dirname(__file__), "static")}

    handlers = [(r"/", MainHandler),
                (r"/_update", UpdateHandler)]

    return tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    board = Arduino('/dev/ttyS0')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
