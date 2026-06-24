from functools import reduce, partial
from operator import add, mul
from collections.abc import Callable


class InvalidOperation(Exception):
    def __init__(self, op: str):
        super().__init__(f"Invalid operator used: '{op}'")


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": add,
        "multiply": mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b
    }
    if operation not in ops:
        raise InvalidOperation(operation)
    if not spells:
        return 0
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "skibidi": partial(base_enchantment, 50, "Skibidi"),
    }


def test_spell_reducer() -> None:
    print("Testing spell reducer...")
    spell_powers = [23, 35, 33, 32, 32, 40]
    operations = ['add', 'multiply', 'max', 'min']
    for op in operations:
        print(f"{op.capitalize()} of {spell_powers}:",
              spell_reducer(spell_powers, op))


def test_partial_enchanter() -> None:
    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(
        lambda s, e, x: f"{e} enchantment (power {s}) applied to {x}"
    )

    print(enchantments["fire"]("Sword"))
    print(enchantments["ice"]("Sword"))
    print(enchantments["skibidi"]("Tung Tung Sahur"))


def main() -> None:
    test_spell_reducer()

    test_partial_enchanter()


if __name__ == "__main__":
    main()
