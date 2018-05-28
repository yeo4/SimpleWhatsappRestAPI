#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, request, post,Bottle,get
from yowsup.layers import YowLayerEvent
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


class YoServer:
    def __init__(self, stack,messages):
        self.stack = stack
        self._app = Bottle()
        self._route()
        self.messages = messages

    def SendMessage(self):
        if self.Password(request.get_header('password')):
            to = request.forms.get("to")
            message = request.forms.get("message")
            try:
                self.stack.broadcastEvent(YowLayerEvent("sendMessage", to=to, msg=message))
            except:
                return "message Error"
            return "message send"
        else:
            return "Accsses dined"

    def ReciveMessage(self):
        if self.Password(request.get_header('password')):
            rec = dict((k, self.messages.pop(k)) for k in self.messages.keys())
            return rec
        else:
            return "Accsses dined"

    def Password(self,password):
        return (password == '0x347c2a6e4e34fb1497bd6606354c3c56b63c3694a88cf16d0dd5416592fb12e2691512248786a6da6983e04b1a711a421e84674b49a042c2f2f197d628f4f24d8dc7beafa54c3f3ccd5828181c22ef53L')

    def _route(self):
        self._app.post('/SendMessage', callback=self.SendMessage)
        self._app.get('/ReciveMessage', callback=self.ReciveMessage)


    def StartServer(self):
        self._app.run(host='localhost',port='8081')
