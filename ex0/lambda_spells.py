def get_test_artifacts() -> list[dict]:
    return [
        {'name': 'Light Prism', 'power': 106, 'type': 'armor'},
        {'name': 'Wind Cloak', 'power': 94, 'type': 'focus'},
        {'name': 'Lightning Rod', 'power': 116, 'type': 'accessory'},
        {'name': 'Light Prism', 'power': 98, 'type': 'armor'}
    ]


def get_test_mages() -> list[dict]:
    return [
        {'name': 'Ash', 'power': 86, 'element': 'lightning'},
        {'name': 'Storm', 'power': 62, 'element': 'shadow'},
        {'name': 'Luna', 'power': 76, 'element': 'light'},
        {'name': 'Rowan', 'power': 70, 'element': 'water'},
        {'name': 'Alex', 'power': 78, 'element': 'earth'}
    ]


def get_test_spells() -> list[str]:
    return ['fireball', 'meteor', 'freeze', 'shield']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: " ".join(["*", s, "*"]), spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": round(sum(m["power"] for m in mages) / len(mages), 2)
    }


def main() -> None:
    print("Testing artifacts sorter...")
    print(artifact_sorter(get_test_artifacts()))

    print("\nTesting power filter...")
    print(power_filter(get_test_mages(), 70))

    print("\nTesting spell transformer...")
    print(spell_transformer(get_test_spells()))

    print("\nTesting mage stats...")
    print(mage_stats(get_test_mages()))


if __name__ == "__main__":
    main()
