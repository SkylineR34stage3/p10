from functools import wraps
from collections.abc import Callable
import time


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


def main() -> None:
    test_spell_timer()


if __name__ == "__main__":
    main()
