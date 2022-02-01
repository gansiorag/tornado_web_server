'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 01/02/2022//
Ending 2022//
    
'''

import tornado.web

class StartPage(tornado.web.RequestHandler):
    def get(self):
        # output rith on pages
        # if not self.get_secure_cookie("mycookie"):
        #     self.set_secure_cookie("mycookie", "myvalue")
        #     self.write("Your cookie was not set yet!")
        # else:
        #     self.write("Your cookie was set!") 
        return self.render('index.html') # output throu on pages