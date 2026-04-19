from typing import Any, Callable


def spell(target: str, power: int) -> str:
    return f"{target} lanched a spell of a power: {power}"


def heal(target: str, power: int) -> str:
    return f"{target} healed with a power of {power}"


def attack(target: str, power: int) -> str:
    return f"{target} attacked with a power of {power}"


def fireball(target: str, power: int) -> str:
    return f"{target} recieved a fireball power: {power}"


def spell_combiner(spell: Callable, spell2: Callable) -> Callable:
    def combined(spell: Callable, spell2: Callable) -> Any:
        return (spell(), spell2())

    def call_func() -> Any:
        return combined(spell, spell2)

    return call_func


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(base_spell: Callable, multiplier: int) -> Any:
        try:
            power = int(base_spell().split(": ", 1)[1])
            return f"Original: {power}, Amplified: {power * multiplier}"
        except Exception as e:
            return e

    def call_func() -> Any:
        return amplifier(base_spell, multiplier)

    return call_func


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def is_valid(condition: Callable, spell: Callable) -> Any:
        if not condition():
            return "Spell fizzled"
        return spell()

    return is_valid


def spell_sequence(spells: list[Callable]) -> Callable:
    def call_func() -> Any:
        for spell in spells:
            print(spell())

    return call_func


def testing_spell_combiner() -> None:
    print("Testing spell combiner")
    combined = spell_combiner(
            lambda: heal("Dragon", 8),
            lambda: attack("Goblin", 12))
    print("Combined: ", combined())


def testing_power_amplifier() -> None:
    print("Testing power amplifier...")
    re = power_amplifier(
            lambda: fireball("Dragon", 10),
            3
            )
    print(re())


def testing_spell_sequence() -> None:
    print("Testing spell sequence...")
    sequence = spell_sequence([
        lambda i=i: spell(f"target {i}", i) for i in range(5)
        ])
    sequence()


def main() -> None:
    testing_spell_combiner()
    print()
    testing_power_amplifier()
    print()
    testing_spell_sequence()


if __name__ == "__main__":
    main()
