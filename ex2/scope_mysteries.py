from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> Callable:
    initial_value = initial_power
    base = initial_power

    def add(value: int) -> str:
        nonlocal initial_value
        nonlocal base
        base = base
        initial_value += value
        return f"Base {base}, add {value}: {initial_value}"

    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment = enchantment_type

    def apply(item_name: str) -> str:
        nonlocal enchantment
        enchantment = enchantment
        return f"{enchantment_type} {item_name}"

    return apply


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Callable] = {}

    def store(
            key: str,
            value: Callable
            ) -> dict[str, Callable]:
        nonlocal vault
        vault = vault
        vault.update({key: value})
        return vault

    def recall(key: str) -> Callable | str:
        if key not in vault:
            return "Memory not found"
        return vault[key]

    return {
            'store': store,
            'recall': recall
            }


def testing_mage_counter() -> None:
    print("Testing mage conuter...")
    counter = mage_counter()
    for _ in range(5):
        print("curr_count =", counter())


def testing_spell_accumulator() -> None:
    accumulator = spell_accumulator(100)
    start = 20
    for _ in range(2):
        re = (accumulator(start))
        print(re)
        start += 10


def testing_enchantment_factory() -> None:
    print("Testing enchantment type...")
    factory = enchantment_factory("Flaming")
    factory2 = enchantment_factory("Frozen")
    re = factory("Sword")
    re2 = factory2("Shield")
    print(re)
    print(re2)


def testing_memory_vault() -> None:
    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']('secret', 42)
    print("Recall 'secret':", vault['recall']('secret'))
    print("Recall 'unkown':", vault['recall']('unkown'))


def main() -> None:
    testing_mage_counter()
    print()
    testing_spell_accumulator()
    print()
    testing_enchantment_factory()
    print()
    testing_memory_vault()


if __name__ == "__main__":
    main()
