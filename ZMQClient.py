#################
# ZMQ Client provided by original equipment manufacturer
# Three different classes are established based on the communication protocol 
# with the API, Command, Data, and events.
# The command client wraps part of the request with common sending requirements. 
##################

import zmq

#Event client
from threading import Thread

class ZMQCommandClient(object):
    """description of class"""
    def __init__(self,address, port):
        self.address = address
        self.port  = port
        self.context =  zmq.Context.instance()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.REQ_RELAXED,1)
        self.socket.setsockopt(zmq.RCVTIMEO,1000) #ms
        self.socket.connect('tcp://%s:%d' % (address , port))
        self.requestSlot = None
        self.resultSlot = None

    def sendCommand(self,command, params):

        request = {"jsonrpc": "2.0", "id" : 1, "method" : command, "params" : params}

        if self.requestSlot :
             self.requestSlot(request)

        self.socket.send_json(request, zmq.NOBLOCK)

        #  Get the reply.
        result = self.socket.recv_json()

        if self.resultSlot :
             self.resultSlot(result)

        if 'error' in result.keys() :
            raise Exception(result['error']['message'])

        return result['result']

class ZMQDataClient(object):
    """description of class"""
    def __init__(self,address, port):
        self.address = address
        self.port  = port

        self.dataSlot = None

        self.context =  zmq.Context.instance()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

        self.socket.connect('tcp://%s:%d' % (address , port))

    def receiveData(self):
        return self.socket.recv(zmq.NOBLOCK)

class ZMQEventClient(object):
    """description of class"""
    def __init__(self,address, port):
        self.address = address
        self.port  = port

        self.eventSlot = None

        self.context =  zmq.Context.instance()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

        self.socket.connect('tcp://%s:%d' % (address , port))

        self.threadEvent = Thread(target = self.pollEvents, daemon = True)
        self.threadEvent.start()


    def pollEvents(self):
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)
        while True:
            socks = dict(self.poller.poll())
            if self.socket in socks :
                event = self.socket.recv_json()
                if self.eventSlot :
                    self.eventSlot(event)