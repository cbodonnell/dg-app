from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class PlayerInfoCreate(BaseModel):
    player: str
    scores: Dict[str, int]

class RoundInfoCreate(BaseModel):
    course: str
    datetime: datetime
    isactive: bool
    players: List[PlayerInfoCreate]

class PlayerInfoResponse(PlayerInfoCreate):
    id: int

class RoundInfoResponse(RoundInfoCreate):
    id: int
    players: List[PlayerInfoResponse]

class PlayerInfoUpdate(BaseModel):
    player: Optional[str]
    scores: Optional[Dict[str, int]]

class RoundInfoUpdate(BaseModel):
    course: Optional[str]
    datetime: Optional[datetime]
    isactive: Optional[bool]
    players: Optional[List[PlayerInfoUpdate]]
