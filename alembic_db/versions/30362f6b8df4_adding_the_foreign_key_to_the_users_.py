"""Adding the foreign key to the users table

Revision ID: 30362f6b8df4
Revises: 0c9606749cf4
Create Date: 2024-09-02 15:24:53.113764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30362f6b8df4'
down_revision: Union[str, None] = '0c9606749cf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
