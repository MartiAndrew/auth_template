"""create access token table

Revision ID: 562f5a4a73ed
Revises: 050d31e4dbfd
Create Date: 2025-11-10 13:26:20.230655

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
import sqlalchemy as sa
from alembic import op

revision: str = "562f5a4a73ed"
down_revision: Union[str, None] = "050d31e4dbfd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "access_token",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_access_token_user_id_user"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("token", name=op.f("pk_access_token")),
    )
    op.create_index(
        op.f("ix_access_token_created_at"),
        "access_token",
        ["created_at"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_access_token_created_at"), table_name="access_token"
    )
    op.drop_table("access_token")
