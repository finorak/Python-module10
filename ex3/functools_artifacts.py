from functools import lru_cache, partial, reduce, singledispatch
import operator
from typing import Any, Callable


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} hit {target} with a power of {power}"


def spell_reducer(
        spells: list[int],
        operation: str) -> int:
    if not spells:
        return 0
    if operation not in ("add", "multiply", "max", "min"):
        raise ValueError("Operation not recognized")
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return max(spells)
    return min(spells)


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable]:
    first_value = partial(
            base_enchantment,
            50,
            "fireball",
            "dragon"
            )
    second_value = partial(
            base_enchantment,
            50,
            "fireball"
            )
    third_value = partial(
            base_enchantment,
            50,
            )
    return {
            "1": first_value,
            "2": second_value,
            "3": third_value
            }


@lru_cache
def memorized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Uknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"{value} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return spell

    @dispatch.register
    def _(spells: list) -> str:
        return f"{len(spells)} spells"

    return dispatch


def testing_spell_reducer() -> None:
    print(("Testing spell reducer..."))
    spells = [40, 30, 20, 10]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))


def testing_partial_enchanter() -> None:
    print("Testing partial enchanter...")
    value = partial_enchanter(enchantment)
    print(value['1']())
    print(value['2']("Mouse"))
    print(value['3']("Icecream", "Bird"))


def testing_memorized_fibonacci() -> None:
    print("Testing memorized fibonacci...")
    print("Fib(0):", memorized_fibonacci(0))
    print("Fib(1):", memorized_fibonacci(1))
    print("Fib(10):", memorized_fibonacci(10))
    print("Fib(15):", memorized_fibonacci(15))


def testing_spell_dispatcher() -> None:
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Damage spell:", dispatcher(42))
    print("Enchantment:", dispatcher("fireball"))
    print("Multi-cast:", dispatcher(["fireball", "firebolt", "test"]))
    print(dispatcher({"t": 6}))


def main() -> None:
    try:
        testing_spell_reducer()
    except Exception as e:
        print(e)
    print()
    testing_memorized_fibonacci()
    print()
    testing_spell_dispatcher()
    print()
    testing_partial_enchanter()


if __name__ == "__main__":
    main()
