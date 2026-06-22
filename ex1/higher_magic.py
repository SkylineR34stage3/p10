from collections.abc import Callable
from random import randint


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def condition(target: str, power: int) -> bool:
    resistance = randint(0, 50 + len(target) * 3)
    return power > resistance


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


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda t, p: spell(t, p) if condition(t, p) else "Spell fizzled"
    # def guarded(target: str, power: int) -> str:
    #     if condition(target, power):
    #         return spell(target, power)
    #     return "Spell fizzled"
    # return guarded


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    res1, res2 = combined("Dragon", 10)
    print(res1, res2, sep="\n")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")
    spell = conditional_caster(condition, fireball)
    for _ in range(5):
        print(spell("Dragon", 34))


if __name__ == "__main__":
    main()
