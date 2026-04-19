import functools
import time
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

    def validate(min_power: int) -> Any:
        pass

    return validate


def retry_spell(max_attemps: int) -> Callable:
    ...


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        return ""


@spell_timer
def main() -> None:
    pass


if __name__ == "__main__":
    main()
