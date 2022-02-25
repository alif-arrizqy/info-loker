import random
import string
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from schemas.users import UserCreate

from db.repository.users import create_new_user
from db.repository.login import get_user


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_owner(db:Session):
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    user_schema = UserCreate(username=email, email=email, password=password)
    user = create_new_user(user=user_schema, db=db)
    return user


def user_authentication_headers(client: TestClient, username: str, password: str):
    data = {"username": username, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_username(client: TestClient, username: str, db: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = "random-passW0rd"
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    user = get_user(username=username, db=db)
    if not user:
        user_in_create = UserCreate(username=username, email=email, password=password)
        user = create_new_user(user=user_in_create, db=db)
    return user_authentication_headers(client=client, username=username, password=password)