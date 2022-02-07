from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.schemas.users import (
    UserInCreate,
    UserInLogin,
    UserInResponse,
    UserWithToken,
)
from app.resources import strings
from app.services import jwt
from app.services.authentication import check_phone_is_taken, check_username_is_taken

router = APIRouter()


# @router.post("/login", response_model=UserInResponse, name="权限:登录", description="")
# async def login(
#     user_login: UserInLogin = Body(..., embed=True, alias="user"),
#     users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
#     settings: AppSettings = Depends(get_app_settings),
# ) -> UserInResponse:
#     wrong_login_error = HTTPException(
#         status_code=HTTP_400_BAD_REQUEST,
#         detail=strings.INCORRECT_LOGIN_INPUT,
#     )

#     try:
#         user = await users_repo.get_user_by_phone(phone=user_login.phone)
#     except EntityDoesNotExist as existence_error:
#         raise wrong_login_error from existence_error

#     if not user.check_password(user_login.password):
#         raise wrong_login_error

#     token = jwt.create_access_token_for_user(
#         user,
#         str(settings.secret_key.get_secret_value()),
#     )
#     return UserInResponse(
#         user=UserWithToken(
#             username=user.username,
#             email=user.email,
#             phone=user.phone,
#             wechat=user.wechat,
#             bio=user.bio,
#             image=user.image,
#             token=token,
#         ),
#     )


# @router.post(
#     "/wechat",
#     status_code=HTTP_201_CREATED,
#     response_model=UserInResponse,
#     name="权限:微信注册",
# )
# async def register(
#     user_create: UserInCreate = Body(..., embed=True, alias="user"),
#     users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
#     settings: AppSettings = Depends(get_app_settings),
# ) -> UserInResponse:
#     if await check_username_is_taken(users_repo, user_create.username):
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail=strings.USERNAME_TAKEN,
#         )

#     if await check_phone_is_taken(users_repo, user_create.phone):
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail=strings.EMAIL_TAKEN,
#         )

#     user = await users_repo.create_user(**user_create.dict())

#     token = jwt.create_access_token_for_user(
#         user,
#         str(settings.secret_key.get_secret_value()),
#     )
#     return UserInResponse(
#         user=UserWithToken(
#             username=user.username,
#             phone=user.phone,
#             wechat=user.wechat,
#             bio=user.bio,
#             image=user.image,
#             token=token,
#         ),
#     )



