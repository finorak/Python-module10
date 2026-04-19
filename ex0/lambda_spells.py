from typing import Any, Union


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts: list[dict] = []
    try:
        sorted_artifacts = sorted(artifacts, key=lambda x: -x['power'])
        return sorted_artifacts
    except Exception as e:
        print(e)
    return []


def power_filter(mages: list[dict[str, Any]], min_power: int) -> list[dict]:
    power_filtered: filter[dict[str, Any]]
    try:
        power_filtered = filter(lambda x: x['power'] >= min_power, mages)
        return list(power_filtered)
    except Exception as e:
        print(e)
    return []


def spell_transformer(spels: list[str]) -> list[str]:
    transformed: list[str] = []
    try:
        transformed = list(map(lambda x: f"* {x} *", spels))
        return transformed
    except Exception as e:
        print(e)
    return []


def mage_stats(mages: list[dict]) -> dict:
    def ge_avg(lst: list[int]) -> float:
        counter = 0
        for el in (lst):
            counter += el
        return counter / len(lst)

    try:
        mage_power: list[int] = list(map(lambda x: x['power'], mages))
        return {
                'max_power': max(mage_power),
                'min_power': min(mage_power),
                'avg_power': ge_avg(mage_power)
                }
    except Exception as e:
        print(e)
    return {}


def testing_articact_sort(artifacts: list[dict[str, Union[str, int]]]) -> None:
    print("Testing artifacts sorter...")
    new_artifacts = artifact_sorter(artifacts)
    if not new_artifacts:
        return None
    for index, el in enumerate(new_artifacts):
        end = " -> " if index < len(new_artifacts) - 1 else "\n"
        print(f"{el['name']} ({el['power']})", end=end)


def testing_power_filter(mages: list[dict[str, Any]], min_power: int) -> None:
    print("Testing power filter...")
    new_power = power_filter(mages, min_power)
    if not new_power:
        return None
    for index, el in enumerate(new_power):
        end = "" if index < len(new_power) - 1 else "\n"
        print(f"* {el['name']} * ", end=end)


def testing_spell_transformer(spells: list[str]) -> None:
    print("Testing spell transformer...")
    transformed: list[str] = spell_transformer(spells)
    if not transformed:
        return None
    for spell in transformed:
        print(spell)


def testing_mage_stats(mages: list[dict[str, Any]]) -> None:
    print("Testing mage stats...")
    stats = mage_stats(mages)
    if not stats:
        return None
    print(stats)


def main(artifacts: list[dict[str, Any]],
         mages: list[dict[str, Any]],
         spells: list[str]) -> None:
    testing_articact_sort(artifacts)
    print()
    testing_power_filter(mages, 80)
    print()
    testing_spell_transformer(spells)
    print()
    testing_mage_stats(mages)


if __name__ == "__main__":
    artifacts = [
            {'name': 'Light Prism', 'power': 117, 'type': 'accessory'},
            {'name': 'Earth Shield', 'power': 102, 'type': 'armor'},
            {'name': 'Lightning Rod', 'power': 95, 'type': 'relic'},
            {'name': 'Ice Wand', 'power': 63, 'type': 'armor'},
            ]
    mages = [
            {'name': 'Kai', 'power': 86, 'element': 'wind'},
            {'name': 'Sage', 'power': 79, 'element': 'fire'},
            {'name': 'Morgan', 'power': 62, 'element': 'earth'},
            {'name': 'Phoenix', 'power': 65, 'element': 'earth'},
            {'name': 'Jordan', 'power': 82, 'element': 'lightning'}
            ]
    spells = ['blizzard', 'darkness', 'shield', 'meteor']
    main(artifacts, mages, spells)
