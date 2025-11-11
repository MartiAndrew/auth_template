from textwrap import dedent

from tmpauth.db.models import User
from tmpauth.jinja_templates import templates
from tmpauth.services.mailing.send_email import send_email


async def send_email_confirmed(
    user: User,
):
    """Send email confirmed email."""
    recipient = user.email
    subject = "Email confirmed"

    plain_content = dedent(
        f"""\
        Dear {recipient},

        Your email has been confirmed.

        Your site admin,
        © 2025.
        """,
    )

    template = templates.get_template("mailing/email-verify/email-verified.html")
    context = {
        "user": user,
    }
    html_content = template.render(context)
    await send_email(
        recipient=recipient,
        subject=subject,
        plain_content=plain_content,
        html_content=html_content,
    )
