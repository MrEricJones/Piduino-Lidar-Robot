# -*- coding: utf-8 -*-
import threading
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class WebServer(threading.Thread):

    def __init__(self,data):
        threading.Thread.__init__(self)
        #Nte:this is a generic approach, valid whatever it is the passed data
        MyHandler.data=data

        self.server = HTTPServer(('', 80), MyHandler)

    def run(self):
        print 'started httpserver...'
        self.server.serve_forever()

    def stop(self):
        self.server.socket.close()
        print 'stopped httpserver...'


class MyHandler(BaseHTTPRequestHandler):
    #This class is specifi for teh data to be managed. It is the part to be implemented

    def do_GET(self):
        try:

            #IMP: create a local variable = data.variable
            #to be able to write it
            self.param1=self.data.param1
            print (self.path)

            #here manage teh commands
            if self.path.startswith("/param1_incr"):
                self.param1 = self.param1+1

            if self.path.startswith("/param1_decr"):
                self.param1 = self.param1-1

            #add here other possible commands

            #here return the page with updated information
            f = open(curdir + sep + '/index.html')
            self.send_response(200)
            self.send_header('Content-type',	'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            self.wfile.write('param1: '+str(self.param1))
            self.wfile.write('\n param2: '+str(self.data.param2))

            self.wfile.write('\n \n www.solenerotech1.wordpress.com')
            f.close()

            #write the param
            self.data.param1=self.param1
            return
        except:
            pass