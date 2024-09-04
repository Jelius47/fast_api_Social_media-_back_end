"""adding content column in a post table

Revision ID: b233aacef588
Revises: 42da8cec2e57
Create Date: 2024-09-02 14:47:58.402390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b233aacef588'
down_revision: Union[str, None] = '42da8cec2e57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # Here we will be added the logics for creating the new column,but I have created them in a 42da8cec2e57 revision
    pass


def downgrade() -> None:
    pass
