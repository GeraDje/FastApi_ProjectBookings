"""Add bookings,hotels, rooms and users tables

Revision ID: 85b8808c1473
Revises: 022453b2eaca
Create Date: 2023-11-25 21:06:17.408277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85b8808c1473'
down_revision: Union[str, None] = '022453b2eaca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
