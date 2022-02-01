from tracemalloc import start


'''
 This module make learning frame work tornado.
 This is realization router tornado
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 01/02/2022//
Ending 2022//
    
'''
    
import tornado.ioloop
import tornado.web
import os
from app.Pages_py.startPge import StartPage



def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}
    return tornado.web.Application([
        (r"/", StartPage),
    ], debug=True, **settings)
    
