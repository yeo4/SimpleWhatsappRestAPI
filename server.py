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
            return "Unauthorized access"

    def ReciveMessage(self):
        if self.Password(request.get_header('password')):
            rec = dict((k, self.messages.pop(k)) for k in self.messages.keys())
            return rec
        else:
            return "Accsses dined"

    def Password(self,password):
        return (password == 'PASSWORD')

    def _route(self):
        self._app.post('/SendMessage', callback=self.SendMessage)
        self._app.get('/ReciveMessage', callback=self.ReciveMessage)


    def StartServer(self):
        self._app.run(host='localhost',port='8081')
