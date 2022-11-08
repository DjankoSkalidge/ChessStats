from pydantic import BaseModel
from typing import Optional


class Move(BaseModel):
    notation: str
    annotations: Optional[dict]


class Turn(BaseModel):
    movenumber: int
    whitemove: Move
    blackmove: Optional[Move]


class Game(BaseModel):
    turns: list[Turn]


class Entry(BaseModel):
    annotations: dict
    game: Game


class File(BaseModel):
    entries: list[Entry]
