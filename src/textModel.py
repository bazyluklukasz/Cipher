from dataclasses import dataclass, asdict


@dataclass
class TextModel:
    text: str
    rot_type: str
    status: str


    def to_dict(self) -> dict:
        return asdict(self)