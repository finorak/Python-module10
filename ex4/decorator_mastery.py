import functools
import time
import inspect
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def get_time(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f}s")
        return result

    return get_time


def power_validator(min_power: int) -> Callable:

    def get_param_index(args: Any) -> int | None:
        for index, arg in enumerate(args):
            if arg == 'power':
                return index
        return None

    def wrapper(func: Callable) -> Any:
        @functools.wraps(func)
        def validator(
                *args: Any,
                **kwargs: Any
                ) -> Any:
            sig = inspect.signature(func)
            index = get_param_index(sig.parameters.keys())
            if index is None:
                return "Power not in paramater"
            power = args[index]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return validator
    return wrapper


def retry_spell(max_attemps: int) -> Callable:

    def wrapper(func: Callable) -> Any:
        @functools.wraps(func)
        def repeater(*args: Any, **kwargs: Any) -> Any:
            res: Any = None
            for i in range(max_attemps):
                res = func(*args, **kwargs)
                if res and res is not None:
                    return res
                print("Spell failed, retrying... "
                      f"(attempt {i + 1}/{max_attemps})")
            if not res:
                print(f"Spell casting failed after {max_attemps} attempts")
                return None
            print("Waaaaaagh spelled !!")
        return repeater
    return wrapper


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        new_name = name.replace(" ", "")
        if not new_name:
            return True
        return new_name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Succesfully cast {spell_name} with {power} power"


def fireball(power: int) -> str:
    return f"fireball lunched with a power of {power}"


def thunder(power: int) -> str:
    return f"thunder lunched with a power of {power}"


def testing_spell_timer() -> None:
    print("Testing spell timer...")
    spells: list[Callable] = [spell_timer(fireball), spell_timer(thunder)]
    for spell in spells:
        spell(5)


def testing_spell_repeater() -> None:
    print("Testing retrying spell...")

    @retry_spell(3)
    def call_spell(n: int) -> bool:
        if n < 4:
            print("Waaaaaagh spelled!")
            return True
        return False

    call_spell(6)
    call_spell(2)


def testing_power_validator() -> None:
    print("Testing power validator...")

    @power_validator(5)
    def simulation(power: int) -> Any:
        return "Succesfully casted spell"

    re = simulation(2)
    print(re)
    re_fail = simulation(6)
    print(re_fail)


def testing_mage_guild() -> None:
    print("Testing MageGuild...")
    mage: MageGuild = MageGuild()
    print(mage.validate_mage_name("Lightning"))
    print(mage.validate_mage_name("4"))
    valid_casting = mage.cast_spell("Lightning", 15)
    invalid_casting = mage.cast_spell("Lightning", 7)
    print(valid_casting)
    print(invalid_casting)


def main() -> None:
    testing_spell_timer()
    print()
    testing_spell_repeater()
    print()
    testing_power_validator()
    print()
    testing_mage_guild()


if __name__ == "__main__":
    main()
