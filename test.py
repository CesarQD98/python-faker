import json

example = {"id": "123", "name": "lince", "rol": "admin", "online": False}

myobject = json.dumps(example)

print(myobject)
