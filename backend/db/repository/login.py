from db.models.users import User
from sqlalchemy.orm import Session


def get_user(username: str, db: Session) -> User:
    return db.query(User).filter(User.username == username).first()