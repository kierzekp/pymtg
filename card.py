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


class KeywordAbility(Enum):
    DEATHTOUCH = 2
    DEFENDER = 3
    DOUBLE_STRIKE = 4
    ENCHANT = 5
    EQUIP = 6
    FIRST_STRIKE = 7
    FLASH = 8
    FLYING = 9
    HASTE = 10
    HEXPROOF = 11
    INDESTRUCTIBLE = 12
    INTIMIDATE = 13
    LANDWALK = 14
    LIFELINK = 15
    PROTECTION = 16
    REACH = 17
    SHROUD = 18
    TRAMPLE = 19
    VIGILANCE = 20
    WARD = 21
    BANDING = 22
    RAMPAGE = 23
    CUMULATIVE_UPKEEP = 24
    FLANKING = 25
    PHASING = 26
    BUYBACK = 27
    SHADOW = 28
    CYCLING = 29
    ECHO = 30
    HORSEMANSHIP = 31
    FADING = 32
    KICKER = 33
    FLASHBACK = 34
    MADNESS = 35
    FEAR = 36
    MORPH = 37
    AMPLIFY = 38
    PROVOKE = 39
    STORM = 40
    AFFINITY = 41


class ManaPoint:
    def __init__(self, colors: List[Color]):
        self.colors = colors


class Card:
    def __init__(self, name: str, mana_cost: List[ManaPoint], types: List[CardType], rarity: CardRarity):
        self.name = name
        self.types = types
        self.rarity = rarity
        self.mana_cost = mana_cost
        self.colors = list(get_colors_from_mana_cost(mana_cost))


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
    return unique_colors
