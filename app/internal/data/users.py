"""User data and database CRUD operations."""

from argon2 import PasswordHasher
from psycopg import AsyncConnection
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    SecretStr,
    model_serializer,
)


class UserCreate(BaseModel):
    """User input model with validation.

    Validation:
        - Name: 1-256 characters
        - Email: 1-256 characters
        - Password: 8-256 characters
    """

    name: str = Field(min_length=1, max_length=256)
    email: EmailStr = Field(max_length=256)
    password: SecretStr = Field(min_length=8, max_length=256)

    @model_serializer
    def serialize_with_password_hash(self) -> dict[str, str]:
        """Serialize the model to a dictionary.

        Override the default serialization to hash the password.
        """
        return {
            "name": self.name,
            "email": self.email,
            "password_hash": PasswordHasher().hash(self.password.get_secret_value()),
        }


async def insert_user(conn: AsyncConnection, user: UserCreate) -> None:
    """Insert a user into the database.

    Args:
        conn: The database connection.
        user: The user to insert.
    """
    query = """
    INSERT INTO users (name, email, password_hash)
        VALUES (%(name)s, %(email)s, %(password_hash)s)
        RETURNING id, created_at
    """

    await conn.execute(query, params=user.model_dump(), prepare=True)
