"""maps includes multiple maps
"""
import itertools
from abc import ABC


class Map(ABC):
    pass


class TypedMap(Map):
    """
    """
    def __init__(self, key_type=None, value_type=None):
        self._Tk = key_type
        self._Tv = value_type
        self._m = {}


class BidirectMap(Map):
    """Bidirectional Map

    Attributes
        _Tk(type): type of key
        _Tv(type): type of value
        _k(dict): dict of key-value
        _v(dict): dict of value-key
    """
    def __init__(self, key_type=None, value_type=None):
        self._Tk = key_type
        self._Tv = value_type
        self._k = {}
        self._v = {}
        self._l = 0

    def __getitem__(self, key):
        if self._k is None:
            raise KeyError("Empty collection.")

        if isinstance(key, self._Tk):
            return self._k[key]

        if not isinstance(key, self._Tv):
            raise TypeError(
                f"{type(key)} is neither {self._Tk} nor {self._Tv}")

        return self._v[key]

    def __setitem__(self, key, value):
        if self._Tk is None:
            self._Tk = type(key)
            self._Tv = type(value)
            self._set_item(key, value)

        if isinstance(key, self._Tk):
            if not isinstance(value, self._Tv):
                raise TypeError(f"{type(value)} expected to be {self._Tv}")
            self._set_item(key, value)
            return

        if not isinstance(key, self._Tv):
            raise TypeError(
                f"{type(key)} is neither {self._Tk} nor {self._Tv}")

        if not isinstance(value, self._Tk):
            raise TypeError(f"{type(value)} expected to be {self._Tk}")

        self._set_item(value, key)

    def __str__(self):
        s = ""
        for k, v in self._k.items():
            s += f"{k}: {v}\n"
        return s

    def __iter__(self):
        return sekf, _k

    def __len__(self):
        return self._l

    def _set_item(self, key, value):
        self._k[key] = value
        self._v[value] = key
        self._l += 1


if __name__ == "__main__":
    bm = BidirectMap()

    bm["1"] = 1

    bm[2] = "2"

    print(bm)
