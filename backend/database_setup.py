from dotenv import load_dotenv
load_dotenv()
from database_orm import Base
from database_orm import User, Role
from database_orm import GoogleCredentials
from database_orm import GithubCredentials
from database_orm import DiscordCredentials
from database_orm import SpotifyCredentials
from database_orm import TwitchCredentials
from database_orm import Service, Applet, AppletReaction, Action, Reaction, ActionInputField, ReactionInputField
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routes.auth_routes import get_password_hash
import os
import sys

required_env_vars = ["DATABASE_URL"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    print(f"Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

path = os.getenv("DATABASE_URL")

engine = create_engine(path, echo=True)

Base.metadata.create_all(engine)

db = sessionmaker(bind=engine)()

users = db.query(User).all()

if not users:
    admin = User(
        name="admin",
        surname=None,
        email="admin",
        password=get_password_hash("admin"),
        gender=None,
        birthdate=None,
        role=Role.admin,
        is_activated=True
    )
    db.add(admin)
    db.commit()

db.close()
