"""create table scraper_runs

Revision ID: 22a881493358
Revises: 8e42086228de
Create Date: 2024-11-21 12:09:21.628014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22a881493358'
down_revision: Union[str, None] = '8e42086228de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
        CREATE TABLE invest."scraper_runs" (
            "id" BIGINT NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
            "started_at" TIMESTAMPTZ NOT NULL,
            "ended_at" TIMESTAMPTZ,
            PRIMARY KEY("id")
        );
    ''')


def downgrade() -> None:
    op.execute('''
        DROP TABLE invest."scraper_runs";
    ''')