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


if __name__ == '__main__':
    card1 = create_jungle_delver()
    card2 = create_hydras_growth()
    print(card1)
    print()
    print(card2)
