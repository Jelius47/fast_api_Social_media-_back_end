"""Creating users  table

Revision ID: 0c9606749cf4
Revises: b233aacef588
Create Date: 2024-09-02 14:58:10.363004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c9606749cf4'
down_revision: Union[str, None] = 'b233aacef588'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False),
                    sa.UniqueConstraint("email") ,# This is to ensure that duplicate emails are allowed
                    sa.PrimaryKeyConstraint("id")
                    )


def downgrade() -> None:
    pass
