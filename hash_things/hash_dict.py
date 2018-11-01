# -*- coding: utf-8 -*-

"""Hash Dictionaries."""

from typing import Dict


def hash_dict(data: Dict) -> int:
    """
    Hashes a Dictionary recursively.
    List values are converted to Tuples.
    WARNING: Hashing nested dictionaries is expensive.
    """
    cleaned_dict: Dict = {}

    def _clean_dict(data: Dict) -> Dict:
        d: Dict = {}
        for k, v in data.items():
            if isinstance(v, list):
                d[k] = tuple(v)
            elif isinstance(v, dict):
                d[k] = hash_dict(v)
            else:
                d[k] = v
        return d

    cleaned_dict = _clean_dict(data)
    return hash(tuple(sorted(cleaned_dict.items())))
