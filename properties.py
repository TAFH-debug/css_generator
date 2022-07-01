# TODO


class PropType:
    _value: str

    def __init__(self, value: str):
        self._value = value

    def __str__(self) -> str:
        return self._value


def get_type(name: str) -> PropType:
    return PropType(name)
