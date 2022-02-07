from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository


async def check_username_is_taken(repo: UsersRepository, username: str) -> bool:
    try:
        await repo.get_user_by_username(username=username)
    except EntityDoesNotExist:
        return False

    return True


async def check_email_is_taken(repo: UsersRepository, email: str) -> bool:
    try:
        await repo.get_user_by_email(email=email)
    except EntityDoesNotExist:
        return False

    return True



async def check_phone_is_taken(repo: UsersRepository, phone: str) -> bool:
    try:
        await repo.get_user_by_phone(phone=phone)
    except EntityDoesNotExist:
        return False

    return True

