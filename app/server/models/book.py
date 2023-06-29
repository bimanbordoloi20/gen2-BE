from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class BookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "The Notebook",
                "author": "Nicholas Sparks"
            }
        }