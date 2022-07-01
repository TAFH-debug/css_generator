#!/usr/bin python3.10
from properties import get_type, PropType
import sys


class CssProperty:
    property_type: PropType
    value: str

    def __init__(self, name: str, value: str):
        self.property_type = get_type(name)
        self.value = value

    def __str__(self):
        return self.code()

    def code(self) -> str:
        return str(self.property_type) + ": " + self.value + ";"


class Style:
    selector: str
    properties: list[CssProperty]

    def __init__(self, selector: str):
        self.selector = selector
        self.properties = []

    def set_property(self, prop: str, value: str):
        self.properties.append(CssProperty(prop, value))

    def code(self) -> str:
        data = ""
        data += self.selector + " {\n"
        for i in self.properties:
            data += "    " + i.code() + "\n"
        data += "}"
        return data


class Stylesheet:
    path: str
    _styles: list[Style]

    def __init__(self, path):
        self.path = path
        self._styles = []

    def add_style(self, style: Style):
        self._styles.append(style)

    def create(self):
        data = ""
        for i in self._styles:
            data += i.code() + "\n\n"
        with open(self.path, "w") as file:
            file.write(data)


def main():
    # TODO: CLI

    # Example code
    st = Stylesheet("./a.css")
    for i in range(0, 10):
        style = Style(".a" + str(i))
        style.set_property("background-color", "#ff" + str(i))
        st.add_style(style)
    st.create()


if __name__ == '__main__':
    main()

