from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))
    # def combined(target: str, power: int) -> tuple:
    #     return (spell1(target, power), spell2(target, power))
    # return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: (base_spell(target, power * multiplier))
    # def amplified(target: str, power: int) -> str:
    #     return base_spell(target, power * multiplier)
    # return amplified


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    res1, res2 = combined("Dragon", 10)
    print(res1, res2, sep="\n")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 10))


if __name__ == "__main__":
    main()
