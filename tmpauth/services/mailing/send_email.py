from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib

from configuration.settings import settings


async def send_email(
    recipient: str,
    subject: str,
    plain_content: str,
    html_content: str = "",
):
    """
    Отправка почты получателю.

    :param recipient: Получатель
    :param subject: Тема письма
    :param plain_content: Текст письма в формате plain
    :param html_content: Текст письма в формате html
    """
    message = MIMEMultipart("alternative")
    message["From"] = settings.mail.admin_email
    message["To"] = recipient
    message["Subject"] = subject

    plain_text_message = MIMEText(
        plain_content,
        "plain",
        "utf-8",
    )
    message.attach(plain_text_message)

    if html_content:
        html_message = MIMEText(
            html_content,
            "html",
            "utf-8",
        )
        message.attach(html_message)

    await aiosmtplib.send(
        message,
        hostname=settings.mail.host,
        port=settings.mail.port,
    )
