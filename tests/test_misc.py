""" PyTest for py_helper misc.py"""
from __future__ import annotations

from typing import Any, Dict, List

from pyhelper.misc import find_all_in_dict, find_all_in_list


def test_find_all_in_dict(sample_nested_dict: Dict[str, Any]):
    """Test func find_all_in_dict"""
    assert find_all_in_dict(sample_nested_dict, "k")[0] == [1, 2, 3]


def test_find_all_in_list(sample_nested_list: List[Any]):
    """Test func find_all_in_list"""
    assert find_all_in_list(sample_nested_list, "d")[0] == 1
