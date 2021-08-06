from collections.abc import Iterable
from enum import Enum
from typing import List, Set


class CardType(Enum):
    PERMANENT_LAND = 0
    PERMANENT_CREATURE = 1
    PERMANENT_ARTIFACT = 2
    PERMANENT_ENCHANTMENT = 3
    PERMANENT_PLANESWALKER = 4
    SPELL_INSTANT = 10
    SPELL_SORCERY = 11


class Color(Enum):
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4


class CardRarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MYTHIC_RARE = 3


class ManaPoint:
    def __init__(self, colors: List[Color]):
        self.colors = colors


class Card:
    def __init__(self, mana_cost: Set[ManaPoint], types: List[CardType], rarity: CardRarity):
        self.types = types
        self.rarity = rarity
        self.mana_cost = mana_cost
        self.colors = list(get_colors_from_mana_cost(mana_cost))


def get_colors_from_mana_cost(mana_cost: Iterable[ManaPoint]) -> Set[Color]:
    unique_colors = set()
    for point in mana_cost:
        if point.colors and len(point.colors) == 1:
            unique_colors.add(point.colors[0])
    return unique_colors