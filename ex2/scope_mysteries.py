from collections.abc import Callable, Iterator
from random import choice


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


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item: f"{enchantment_type} {item}"


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


def enchantment_generator(types: list[str], items: list[str]) -> Iterator[str]:
    while True:
        enchantment = choice(types)
        item = choice(items)
        enchantment_applier = enchantment_factory(enchantment)
        yield enchantment_applier(item)


def test_enchantment_factory(item_count: int) -> None:
    print("\nTesting Enchantment Factory")
    enchantment_types = ['Radiant', 'Windy', 'Shocking']
    items_to_enchant = ['Armor', 'Wand', 'Shield', 'Staff']

    gen = enchantment_generator(enchantment_types, items_to_enchant)
    for _ in range(item_count):
        print(next(gen))


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}
    return {
        "store": lambda key, value: memory.update({key: value}),
        "recall": lambda key: memory.get(key, "Memory not found")
    }
    # def store(key: str, value: str) -> None:
    #     memory[key] = value
    # def recall(key: str) -> str:
    #     return memory.get(key, "Memory not found")
    # return {"store": store, "recall": recall}


def test_memory_vault() -> None:
    print("\nTesting memory vault...")
    vault = memory_vault()

    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


def main() -> None:
    test_mage_counter()

    test_spell_accumulator(100)

    test_enchantment_factory(5)

    test_memory_vault()


if __name__ == "__main__":
    main()
