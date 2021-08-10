from card import Card, ManaPoint, Color, CardType, CardRarity


def create_jungle_delver():
    return Card("Jungle Delver", [ManaPoint([Color.GREEN])], [CardType.PERMANENT_CREATURE], CardRarity.COMMON)


def create_hydras_growth():
    return Card(
        "Hydra's Growth",
        [ManaPoint([Color.GREEN]), ManaPoint([Color.ANY]), ManaPoint([Color.ANY])],
        [CardType.PERMANENT_ENCHANTMENT],
        CardRarity.UNCOMMON
    )


def create_broodmate_dragon():
    return Card(
        "Broodmate Dragon",
        [ManaPoint([Color.GREEN]), ManaPoint([Color.RED]), ManaPoint([Color.BLACK]),
         ManaPoint([Color.ANY]), ManaPoint([Color.ANY]), ManaPoint([Color.ANY])],
        [CardType.PERMANENT_CREATURE],
        CardRarity.RARE
    )


def create_black_lotus():
    return Card(
        "Black Lotus",
        [],
        [CardType.PERMANENT_ENCHANTMENT],
        CardRarity.BONUS
    )


if __name__ == '__main__':
    card1 = create_jungle_delver()
    card2 = create_hydras_growth()
    card3 = create_broodmate_dragon()
    card4 = create_black_lotus()
    print(card1)
    print()
    print(card2)
    print()
    print(card3)
    print()
    print(card4)
