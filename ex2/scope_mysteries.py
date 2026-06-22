from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def test_mage_counter() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    for i in range(1, 3):
        print(f"counter_a call {i}: {counter_a()}")
    for i in range(1, 2):
        print(f"counter_b call {i}: {counter_b()}")


def main() -> None:
    test_mage_counter()


if __name__ == "__main__":
    main()
