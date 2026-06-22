from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    res1, res2 = combined("Dragon", 10)
    print(res1, res2, sep="\n")


if __name__ == "__main__":
    main()
