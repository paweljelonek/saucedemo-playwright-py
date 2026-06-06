from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


STANDARD_USER = User(username="standard_user", password="secret_sauce")
LOCKED_OUT_USER = User(username="locked_out_user", password="secret_sauce")
PROBLEM_USER = User(username="problem_user", password="secret_sauce")
PERFORMANCE_GLITCH_USER = User(username="performance_glitch_user", password="secret_sauce")
ERROR_USER = User(username="error_user", password="secret_sauce")
INVALID_CREDENTIALS_USER = User(username="standard_user", password="wrong_password")
