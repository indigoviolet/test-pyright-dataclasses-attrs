from dataclasses import dataclass, field

import attrs

@dataclass
class Parent:
    foo: int = field(default=2)


@attrs.define
class Child(Parent):
    bar: str

if __name__ == '__main__':
    c = Child('c')
    print(repr(c))