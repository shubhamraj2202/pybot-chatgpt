""" Cnftest for py-helper """
from __future__ import annotations

from typing import Dict, List

import pytest


@pytest.fixture(scope="session")
def sample_nested_dict() -> Dict:
    """Return Sample Nested Dict"""
    return {
        "a": {
            "b": {"c": {"d": {"e": {"f": {"g": {"h": {"i": "j", "k": [1, 2, 3]}}}}}}},
            "l": [4, 5, 6],
        },
    }


@pytest.fixture(scope="session")
def sample_nested_list() -> List:
    """Returns Sample nested List"""
    return ["a", ["b", ["c", {"d": 1}]], "e", ["f"], [["g"]]]
