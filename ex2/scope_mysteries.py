from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power
    return accumulate


def test_mage_counter() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    for i in range(1, 3):
        print(f"counter_a call {i}: {counter_a()}")
    for i in range(1, 2):
        print(f"counter_b call {i}: {counter_b()}")


def test_spell_accumulator(base: int) -> None:
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(base)
    print(f"Base {base}, add 20: {accumulator(20)}")
    print(f"Base {base}, add 30: {accumulator(30)}")


def main() -> None:
    test_mage_counter()

    test_spell_accumulator(100)


if __name__ == "__main__":
    main()
