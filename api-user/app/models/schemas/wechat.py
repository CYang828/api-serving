from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class WechatCallbackInfo(RWSchema):
    token: str
    signature: str
    timestamp: str
    nonce: str


class WechatCallbackResponse(RWSchema):
    pass


class UserInResponse(RWSchema): 
    pass