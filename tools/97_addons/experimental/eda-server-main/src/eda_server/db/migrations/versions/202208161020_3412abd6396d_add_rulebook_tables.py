#  Copyright 2022 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Add rulebook related tables.

Revision ID: 3412abd6396d
Revises: 09d9de4b4624
Create Date: 2022-08-16 10:20:48.125149+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "3412abd6396d"
down_revision = "09d9de4b4624"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ruleset",
        sa.Column(
            "id", sa.Integer(), sa.Identity(always=True), nullable=False
        ),
        sa.Column("rule_set_file_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["rule_set_file_id"],
            ["rule_set_file.id"],
            name=op.f("fk_ruleset_rule_set_file_id"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ruleset")),
    )
    op.create_table(
        "rule",
        sa.Column(
            "id", sa.Integer(), sa.Identity(always=True), nullable=False
        ),
        sa.Column("ruleset_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column(
            "action",
            postgresql.JSONB(none_as_null=True, astext_type=sa.Text()),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["ruleset_id"],
            ["ruleset.id"],
            name=op.f("fk_rule_ruleset_id"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rule")),
    )


def downgrade() -> None:
    op.drop_table("rule")
    op.drop_table("ruleset")
