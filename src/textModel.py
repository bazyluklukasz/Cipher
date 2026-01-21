from dataclasses import dataclass, asdict


@dataclass
class TextModel:
    text: str
    rot_type: str
    status: str


    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    def __str__(self) -> str:
        return f"{self.text} {self.rot_type} {self.status}"