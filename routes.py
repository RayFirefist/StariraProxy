import json
from main import server

import lib.starira.api as api
import lib.starira.packets as packets

stariraApi = api.StariraWebSocketDealer()

print("Hello")


@server.route("/ping")
def ping():
    data = stariraApi.send({"type": 1005, "data": {"hash": "DEQBCjt2kw/Ln4FUEyhxlZt4GwnbzE6jiusUtk4X7IFkTBfZAAh6UDIpnf0XOkt2", "cookie": "7e14d92a-8002-4278-bd03-22f280c64ff2"}})
    print(data)
    data = stariraApi.send({"type": packets.PK_AUTH_CREATE_HASH})
    print(data)
    return "pong"

@server.route("/ping2")
def ping2():
    data = stariraApi.send({"type": packets.PK_DRESS_LIST})
    print(data)
    return "pong"
