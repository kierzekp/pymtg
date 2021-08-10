from typing import List, Set, Iterable

from card_types import CardType
from utils import StringableEnum


class Color(StringableEnum):
    """Enumeration of mana colors in Magic the Gathering."""
    ANY = -1
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4


class CardRarity(StringableEnum):
    """Enumeration of possible card rarities in Magic the Gathering."""
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MYTHIC_RARE = 3
    BONUS = 4


class ManaPoint:
    """A class abstracting a single mana point as drawn on a card."""
    def __init__(self, colors: List[Color]):
        self.colors = colors


class Card:
    """A class abstracting a physical, static Magic the Gathering card. All the costs, abilities and effects are
    represented exactly as on the card, and do not take into account any effects that affect it during game. """
    def __init__(self,
                 name: str, mana_cost: List[ManaPoint], types: List[CardType], rarity: CardRarity,
                 base_attack: int = 0, base_defence: int = 0):
        self.name = name
        self.types = types
        self.rarity = rarity
        self.mana_cost = mana_cost
        self.converted_mana_cost = len(mana_cost)
        self.colors = list(get_colors_from_mana_cost(mana_cost))
        self.base_attack = base_attack
        self.base_defence = base_defence

    def __str__(self):
        return f"""{self.name} / {self.types}
{self.rarity}
Converted mana cost: {self.converted_mana_cost}
Colors: {self.colors}
"""


class Ability:
    """A class abstracting a non-static ability a card has."""
    def __init__(self, name: str, description: str, mana_cost: List[ManaPoint], tapping: bool):
        self.name = name
        self.description = description
        self.mana_cost = mana_cost
        self.tapping = tapping


def get_colors_from_mana_cost(mana_cost: Iterable[ManaPoint]) -> Set[Color]:
    """A function which converts an iterable collection of ManaPoint objects into a set of unique colors an enitity
    has. If the passed collection is empty, the returned value is a set with a single Color.ANY value."""
    unique_colors = {Color.ANY}
    for point in mana_cost:
        if point.colors and len(point.colors) == 1:
            unique_colors.add(point.colors[0])
    if len(unique_colors) > 1:
        unique_colors.discard(Color.ANY)
    return unique_colors
