from yowsup.stacks                             import YowStackBuilder
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.stacks                             import YowStack
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from yowsup                                    import env
from layer                                     import MDALayer
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_presence           import YowPresenceProtocolLayer
from yowsup.env                                import YowsupEnv
from server                                    import YoServer
import threading, time

CREDENTIALS = ("", "") # replace with your phone and password

if __name__== "__main__":

    messages = dict()

    stackBuilder = YowStackBuilder()
    stack = stackBuilder\
            .pushDefaultLayers(True)\
            .push(MDALayer)\
            .build()
    YoServer = YoServer(stack,messages)

    stack.setCredentials(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    stack.setProp("messages", messages)

    def Bot():
        try:
            print("\nWhatsBot started. Phone number: %s" % CREDENTIALS[0])
            stack.loop(timeout = 0.5, discrete = 0.5)
        except AuthError as e:
            print("Auth Error: %s" % e.message)
    def Server():
            YoServer.StartServer()
    try:
        WaThread = threading.Thread( target=Bot )
        WaThread.daemon = True
        WaThread.start()

        AppThread = threading.Thread( target=Server )
        AppThread.daemon = False
        AppThread.start()
    except KeyboardInterrupt:
        print("\nBot down now :)")
