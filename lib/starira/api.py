import json
import msgpack
import websocket


class StariraWebSocketDealer():
    def __init__(self, url="ws://t-vertx-home-3.ww.revuestarlight-relive.com:443"):
        self.connected = False
        self.url = url
        self.ws = None
        self.connect()
        pass

    # will run only on init. please don't call it or you'll receive an exception
    def connect(self):
        if self.connected:
            raise Exception("Connection already enstablished")

        headers = {
            'Upgrade': 'websocket',
            'Connection': 'Upgrade',
            'Sec-WebSocket-Key': 'anAuY28uYXRlYW0ud2Vic29ja2V0',
            'Sec-WebSocket-Version': '13'
        }

        self.ws = websocket.create_connection(self.url, headers=headers)
        self.connected = True # connected now
        pass

    # disconnects the websocket
    def disconnect(self):
        if not self.connected:
            raise Exception("Trying to close a closed/null socket")

        try:
            self.ws.shutdown()
        except:
            pass
        self.ws = None

        self.connected = False # not connected anymore
        pass

    # sends data to server. it can be bytes (msgpack-ed) or just a dict (will be encoded automatically)
    def send(self, data):
        if not self.connected:
            raise Exception("Trying to send data on closed/null socket")

        if type(data) is dict:
            data = self.packData("pack", data)
        elif not type(data) is bytes:
            raise Exception("Invalid data type found on body")

        try:
            self.ws.send(data)
            response = self.ws.recv()
            #print(response)
            return self.packData('unpack', response)
        except TypeError as e:
            print(e,"| empty")
            return "<empty>"
        except BrokenPipeError:
            print("broken pipe")
            self.disconnect()
            self.connect()
            return self.send(data)

    def packData(self, mode, obj):
        if mode == 'pack':
            return msgpack.packb(obj)
        elif mode == 'unpack':
            return msgpack.unpackb(obj, raw=False)
