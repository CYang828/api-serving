from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from app.api.dependencies.database import get_repository
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.schemas.wechat import (
    WechatCallbackInfo,
    WechatCallbackResponse,
    UserInResponse
)
from app.resources import strings
from app.services import jwt
from app.services.authentication import check_phone_is_taken, check_username_is_taken

router = APIRouter()


@router.post(
    "/callback",
    status_code=HTTP_201_CREATED,
    response_model=UserInResponse,
    name="微信:扫描二维码回调函数",
    description="""
    扫描公司服务号二维码。
    1. 如果是未关注用户，完成关注后，跳转到输入用户信息页面，完成注册流程；
    2. 如果是已关注用户，登录系统。
    """,
    response_description="""
    1. 如果是未关注用户，完成关注后,返回用户唯一ID，并跳转到用户填写信息页面。
    2. 如果是已关注用户，登录系统。
    """
)
async def callback(
    wechat_callback_info: WechatCallbackInfo = Body(..., embed=True, alias="user"),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
    settings: AppSettings = Depends(get_app_settings),
) -> WechatCallbackResponse:
    # 检查回调身份是否合法
    try:
        check_signature(wechat_callback_info.token, wechat_callback_info.signature,
                        wechat_callback_info.timestamp, wechat_callback_info.nonce)
    except InvalidSignatureException:
        pass
    
    user = await users_repo.create_user(**user_create.dict())

    token = jwt.create_access_token_for_user(
        user,
        str(settings.secret_key.get_secret_value()),
    )
    return WechatCallbackResponse(
        user=UserWithToken(
            username=user.username,
            phone=user.phone,
            wechat=user.wechat,
            bio=user.bio,
            image=user.image,
            token=token,
        ),
    )
