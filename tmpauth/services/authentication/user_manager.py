from typing import TYPE_CHECKING, Optional

from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import BaseUserDatabase
from loguru import logger
from tmpauth.db.models import User
from tmpauth.services.mailing.send_email_confirmed import send_email_confirmed
from tmpauth.services.mailing.send_verification_email import send_verification_email

from configuration.settings import settings
from configuration.types import UserIdType

if TYPE_CHECKING:
    from fastapi import BackgroundTasks, Request
    from fastapi_users.password import PasswordHelperProtocol


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):  # type: ignore
    """Класс менеджер для работы с пользователями."""

    reset_password_token_secret = settings.auth.reset_password_token_secret
    verification_token_secret = settings.auth.verification_token_secret

    def __init__(
        self,
        user_db: BaseUserDatabase[User, UserIdType],
        password_helper: Optional["PasswordHelperProtocol"] = None,
        background_tasks: Optional["BackgroundTasks"] = None,
    ):
        super().__init__(user_db, password_helper)
        self.background_tasks = background_tasks

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        # if self.background_tasks:
        #     self.background_tasks.add_task(
        #         FastAPICache.clear,
        #         namespace=settings.cache.namespace.users_list,
        #     )
        # else:
        #     await FastAPICache.clear(
        #         namespace=settings.cache.namespace.users_list,
        #     )
        logger.warning(f"User {user.id} has registered.")
        # await send_new_user_notification(user)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        logger.warning(
            f"User {user.id} has forgot their password. Reset token: {token}",
        )

    async def on_after_verify(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        logger.warning(f"User {user.id} has been verified")

        self.background_tasks.add_task(
            send_email_confirmed,
            user=user,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        logger.warning(
            f"Verification requested for user {user.id}. Verification token: {token}",
        )
        verification_link = request.url_for("verify_email").replace_query_params(
            token=token,
        )
        self.background_tasks.add_task(
            send_verification_email,
            user=user,
            verification_link=str(verification_link),
        )
