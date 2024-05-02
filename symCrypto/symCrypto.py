from typing import TypeVar, Callable, Set
from abc import ABC, abstractmethod

X = TypeVar('X')
Y = TypeVar('Y')
K = TypeVar('K')

class SymCryptoSystem():
    def __init__(self, X: Set[X], Y: Set[Y], K: Set[K], encrypt: Callable[[K, X], Y], decrypt: Callable[[K, Y], X]) -> None:
        self.X = X
        self.Y = Y
        self.K = K
        self.encrypt = encrypt
        self.decrypt = decrypt


