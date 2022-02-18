from enum import Enum


class StringableEnum(Enum):
    def __str__(self):
        return self.name.replace("_", " ").title()
