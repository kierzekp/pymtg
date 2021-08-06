from typing import List, Set, Iterable
from utils import StringableEnum


class CardType(StringableEnum):
    PERMANENT_LAND = 0
    PERMANENT_CREATURE = 1
    PERMANENT_ARTIFACT = 2
    PERMANENT_ENCHANTMENT = 3
    PERMANENT_PLANESWALKER = 4
    SPELL_INSTANT = 10
    SPELL_SORCERY = 11


class Color(StringableEnum):
    ANY = -1
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4


class CardRarity(StringableEnum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MYTHIC_RARE = 3


class ManaPoint:
    def __init__(self, colors: List[Color]):
        self.colors = colors


class Card:
    def __init__(self, name: str, mana_cost: List[ManaPoint], types: List[CardType], rarity: CardRarity):
        self.name = name
        self.types = types
        self.rarity = rarity
        self.mana_cost = mana_cost
        self.converted_mana_cost = len(mana_cost)
        self.colors = list(get_colors_from_mana_cost(mana_cost))

    def __str__(self):
        return f"""{self.name} / {self.types}
{self.rarity}
Converted mana cost: {self.converted_mana_cost}
Colors: {self.colors}
"""


class Ability:
    def __init__(self, name: str, mana_cost: List[ManaPoint], tapping: bool):
        self.name = name
        self.mana_cost = mana_cost
        self.tapping = tapping


def get_colors_from_mana_cost(mana_cost: Iterable[ManaPoint]) -> Set[Color]:
    unique_colors = set()
    for point in mana_cost:
        if point.colors and len(point.colors) == 1:
            unique_colors.add(point.colors[0])
    unique_colors.discard(Color.ANY)
    return unique_colors
