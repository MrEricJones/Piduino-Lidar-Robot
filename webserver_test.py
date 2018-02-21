# -*- coding: utf-8 -*-
from time import sleep

from webserver import WebServer


class mydataclass(object):

    def __init__(self):
        self.param1=0
        self.param2=0


#MAIN LOOP
try:
    mydata=mydataclass()
    myWebServer=WebServer(mydata)
    myWebServer.start()

    cycling = True
    while cycling:
        #In the mail loop , do something, for example  increment param2
        #and do some verificationon param1
        mydata.param2 +=1
        sleep(1)
        if mydata.param1<0:
            print 'param1 is negative...'
        if mydata.param1==5:
            #parameter param1 is incremented by the user on the browser
            cycling = False

    myWebServer.stop()
    print "well done!"

except KeyboardInterrupt:
    print '^C received, shutting down server'
    myWebServer.stop()


