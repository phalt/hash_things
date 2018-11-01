#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `hash_things` package."""

import pytest

from hash_things import hash_dict


@pytest.mark.parametrize(
    'input_dict', [
        {'foo': 'bar'},
        {'foo': {'bar': 'two'}},  # Dict of dicts is supported
        {'foo': ['bar', 'two']},  # Lists should be supported
        {'foo': ('bar', 'foo')},  # Tuples should be supported
    ],
)
def test_hash_dict(input_dict):
    # Various inputs should hash properly
    result = hash_dict(input_dict)
    assert isinstance(result, int)
