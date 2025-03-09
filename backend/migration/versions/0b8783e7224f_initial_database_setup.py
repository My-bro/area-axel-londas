"""Initial database setup

Revision ID: 0b8783e7224f
Revises: 
Create Date: 2024-10-27 17:47:46.216719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0b8783e7224f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('is_activated', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('actions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('service_id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('output_fields', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('route', sa.String(), nullable=False),
    sa.Column('provider', sa.String(), nullable=True),
    sa.Column('polling_interval', sa.Integer(), nullable=False),
    sa.Column('webhook', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discord_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('github_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('sub', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sub')
    )
    op.create_table('google_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('sub', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sub')
    )
    op.create_table('reactions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('service_id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('route', sa.String(), nullable=False),
    sa.Column('provider', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spotify_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('twitch_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actions_inputs_fields',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('action_id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('regex', sa.String(), nullable=False),
    sa.Column('example', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['action_id'], ['actions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applets',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('tags', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('action_id', sa.UUID(), nullable=False),
    sa.Column('action_inputs', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('action_state', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('action_webhook_armed', sa.Boolean(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['action_id'], ['actions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reactions_inputs_fields',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('reaction_id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('regex', sa.String(), nullable=False),
    sa.Column('example', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['reaction_id'], ['reactions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applets_reactions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('applet_id', sa.UUID(), nullable=False),
    sa.Column('reaction_id', sa.UUID(), nullable=False),
    sa.Column('reaction_inputs', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['applet_id'], ['applets.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['reaction_id'], ['reactions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applets_reactions')
    op.drop_table('reactions_inputs_fields')
    op.drop_table('applets')
    op.drop_table('actions_inputs_fields')
    op.drop_table('twitch_credentials')
    op.drop_table('spotify_credentials')
    op.drop_table('reactions')
    op.drop_table('google_credentials')
    op.drop_table('github_credentials')
    op.drop_table('discord_credentials')
    op.drop_table('actions')
    op.drop_table('users')
    op.drop_table('services')
    # ### end Alembic commands ###
