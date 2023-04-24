# -*- coding: utf-8 -*-

from pydantic import BaseModel


# step: 0-init; 1-ai_name; 2-ai_role; 3-ai_goal; 6-input_command;
from pydantic.fields import Optional


class KKRequest(BaseModel):
    uid: str
    step: int = 0
    content: str = None
    extras: Optional[object]


class KKResponse(BaseModel):
    code: int = 0
    msg: str = ""
    data: object = None

    def __init__(self, code: int, msg: str, data: object, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = code
        self.msg = msg
        self.data = data

    def success(self):
        return self.code == 0


def response(code: int, msg: str, data: object) -> KKResponse:
    return KKResponse(code, msg, data)


def success_response(data: object) -> KKResponse:
    return KKResponse(0, "OK", data)
