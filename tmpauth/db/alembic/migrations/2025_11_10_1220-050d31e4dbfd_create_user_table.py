"""create_user_table

Revision ID: 050d31e4dbfd
Revises: 
Create Date: 2025-11-10 12:20:11.830450

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "050d31e4dbfd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "user",
        sa.Column(
            "nickname", sa.String(length=25), nullable=True, comment="Никнейм"
        ),
        sa.Column(
            "avatar",
            sa.String(length=250),
            nullable=True,
            comment="Ссылка на аватар",
        ),
        sa.Column(
            "about", sa.String(length=150), nullable=True, comment="О себе"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата создания",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
        sa.UniqueConstraint("nickname", name=op.f("uq_user_nickname")),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
