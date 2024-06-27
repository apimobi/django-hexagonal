from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DUser:
    id: str
    email: str

@dataclass(frozen=True)
class DOffer:
    id: str
    title: str
    completed: bool
    updated: datetime
    user:DUser
