from functools import reduce
from operator import add, mul


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


def test_spell_reducer() -> None:
    print("Testing spell reducer...")
    spell_powers = [23, 35, 33, 32, 32, 40]
    operations = ['add', 'multiply', 'max', 'min']
    for op in operations:
        print(f"{op.capitalize()} of {spell_powers}:",
              spell_reducer(spell_powers, op))


def main() -> None:
    test_spell_reducer()


if __name__ == "__main__":
    main()
