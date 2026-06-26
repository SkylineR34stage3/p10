from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


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


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


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


def test_memoized_fibonacci() -> None:
    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0), memoized_fibonacci.cache_info())
    print("Fib(1):", memoized_fibonacci(1), memoized_fibonacci.cache_info())
    print("Fib(10):", memoized_fibonacci(10), memoized_fibonacci.cache_info())
    print("Fib(15):", memoized_fibonacci(15), memoized_fibonacci.cache_info())


def test_spell_dispatcher() -> None:
    print("\nTesting spell dispatcher...")

    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("Skibidi"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))


def main() -> None:
    test_spell_reducer()

    test_partial_enchanter()

    test_memoized_fibonacci()

    test_spell_dispatcher()


if __name__ == "__main__":
    main()
