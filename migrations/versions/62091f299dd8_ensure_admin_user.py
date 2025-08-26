"""ensure_admin_user

Revision ID: 62091f299dd8
Revises: 93d1bf334089
Create Date: 2025-08-26 13:58:29.499825

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import sqlmodel
from dundie.models.user import User
from sqlmodel import Session


# revision identifiers, used by Alembic.
revision: str = '62091f299dd8'
down_revision: Union[str, None] = '93d1bf334089'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # NEW
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
