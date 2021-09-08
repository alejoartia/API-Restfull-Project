import json


class Response:

    def __init__(self, status=True, data=[], msg='ok', code=200):
        self.status = status
        self.msg = msg
        self.data = data
        self.code = code

    def send(self):
        return json.dumps(
            {
                "status":self.status,
                "msg": self.msg,
                "data": {self.data},
                "code": self.code
            }
            )