from __future__ import annotations
from collections.abc import Iterable, Iterator

"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

class CadenaIterator(Iterator):
    def __init__(self, cadena: str, reverse: bool = False) -> None:
        self._cadena = cadena
        self._reverse = reverse
        self._position = len(cadena) - 1 if reverse else 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self._reverse and self._position < 0) or (not self._reverse and self._position >= len(self._cadena)):
            raise StopIteration()
        value = self._cadena[self._position]
        self._position += -1 if self._reverse else 1
        return value


class Cadena(Iterable):
    def __init__(self, cadena: str = "") -> None:
        self._cadena = cadena

    def __iter__(self) -> CadenaIterator:
        return CadenaIterator(self._cadena)

    def get_reverse_iterator(self) -> CadenaIterator:
        return CadenaIterator(self._cadena, True)


# Ejemplo de uso
cadena = Cadena("Hola Mundo")

print("Recorrido directo:")
print(''.join(cadena))

print("\nRecorrido inverso:")
print(''.join(cadena.get_reverse_iterator()))
