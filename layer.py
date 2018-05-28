# -*- coding: utf8 -*-
from yowsup.layers                                      import YowLayerEvent
from yowsup.layers.auth                                 import YowAuthenticationProtocolLayer
from yowsup.layers.interface                            import YowInterfaceLayer                   # Reply to the message
from yowsup.layers.interface                            import ProtocolEntityCallback          # Reply to the message
from yowsup.layers.network                              import YowNetworkLayer
from yowsup.layers.protocol_iq.protocolentities         import IqProtocolEntity
from yowsup.layers.protocol_messages.protocolentities   import TextMessageProtocolEntity          # Body message
from yowsup.layers.protocol_presence.protocolentities   import AvailablePresenceProtocolEntity   # Online
from yowsup.layers.protocol_presence.protocolentities   import UnavailablePresenceProtocolEntity # Offline
from yowsup.layers.protocol_presence.protocolentities   import PresenceProtocolEntity         # Name presence
from yowsup.layers.protocol_chatstate.protocolentities  import OutgoingChatstateProtocolEntity   # is writing, writing pause
from yowsup.common.tools                                import Jid  # is writing, writing pause
import sys
from server import YoServer

reload(sys)
sys.setdefaultencoding('utf-8')

class MDALayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self, messageProtocolEntity):
        origin = messageProtocolEntity.getFrom(False)
        body = messageProtocolEntity.getBody()
        id = messageProtocolEntity.getId()
        self.getProp("messages")[id] = { 'origin': origin, 'body': body }

    def sendMessage(self, to, msg):
        print("sendMessage",to,msg)
        messageEntity = TextMessageProtocolEntity(msg, to=to)
        self.toLower(messageEntity)

    def onEvent(self, e):
        if e.name == 'sendMessage':
            self.sendMessage(e.args['to'],e.args['msg'])
