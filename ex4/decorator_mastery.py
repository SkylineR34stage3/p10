from functools import wraps
from collections.abc import Callable
import time
from random import choice


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def test_spell_timer() -> None:
    print("Testing spell timer...")

    @spell_timer
    def slow_fireball(target: str, power: int) -> str:
        time.sleep(0.228)
        return f"Fireball hits {target} for {power} damage"

    result = slow_fireball("Dragon", 50)
    print("Result:", result)


def test_power_validator() -> None:
    print("\nTesting power validator")

    @power_validator(10)
    def cast(power: int, target: str) -> str:
        return f"Hit {target} with {power} power"

    print(cast(15, "Dragon"))
    print(cast(5, "Dragon"))


def test_retry_spell() -> None:
    print("\nTesting retry spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        if choice([True, False, False]):
            return "Waaaaaagh spelled !"
        raise RuntimeError("Spell misfired!")

    print(unstable_spell())


def main() -> None:
    test_spell_timer()

    test_power_validator()

    test_retry_spell()


if __name__ == "__main__":
    main()
