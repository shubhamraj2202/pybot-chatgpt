"""
Useful Miscellaneous Utilities which can be reused at multiple places in a Python Code
"""

from __future__ import annotations

import os
import re
from typing import Any, Callable, Dict, Iterator, List


def find_all_in_dict(data: dict[str, Any], search_key: str) -> List[Any]:
    """
    Function to Find/Search any Key in a Nested Dictionary.
    Args:
        data_dict (Dict[str, Any]):  Data Dict in which search will be performed
        search_key (str): Key to search
    Returns:
        List: List of Found Values matching with the Keys
    """
    result: list = []
    if search_key in data:
        result.append(data[search_key])
    for key in data.keys():
        val = data[key]
        if isinstance(val, Dict):
            result.extend(find_all_in_dict(val, search_key))
        elif isinstance(val, List):
            result.extend(find_all_in_list(val, search_key))
    return result


def find_all_in_list(data: List[Any], search_key: str) -> List[Any]:
    """
    Function to Find/Search any Key in a Nested List.
    Args:
        data_list (List[Any]):  Data List in which search will be performed
        search_key (str): Key to search
    Returns:
    """
    result: list = []
    for val in data:
        if isinstance(val, Dict):
            result.extend(find_all_in_dict(val, search_key))
        elif isinstance(val, List):
            result.extend(find_all_in_list(val, search_key))
    return result


def dict_with(data: dict[str, Any], keys: List[Any]) -> dict[str, Any]:
    """
    Function to Create a Dict with the given keys.
    Args:
        data (Dict[str, Any]):  Data Dict
        keys (List[str]): Keys to Include
    Returns:
        Dict: Dict to given keys
    """
    result: dict = {}
    if not keys:
        return result
    for key in data.keys():
        if key in keys:
            result[key] = data[key]
    return result


def deeep_flatten(array: List[Any]) -> Iterator[Any]:
    """Flattens arbitrarily-nested list `array` into single-dimensional."""
    while array:
        if isinstance(array[0], List):
            array = array[0] + array[1:]
        else:
            yield array.pop(0)


def rec_flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten Any List"""
    if not nested_list:
        return nested_list
    if isinstance(nested_list[0], list):
        return rec_flatten_list(*nested_list[:1]) + rec_flatten_list(nested_list[1:])
    return nested_list[:1] + rec_flatten_list(nested_list[1:])


def has_common(list1: List[Any], list2: List[Any]) -> bool:
    """
    Function to check if list1 and list2 have common elements
    Args:
        list1 (List[Any]): List 1
        list2 (List[Any]): List 2
    Returns: bool: True if list1 and list2 have common elements
    """
    for elem in list1:
        if elem in list2:
            return True
    return False


def matched_parenthesis(string: str) -> bool:
    """
    Function to check if string has matching parenthesis
    Args:
        string (str): String to check
    Returns: bool: True if string has matching parenthesis
    """
    return string.count("(") == string.count(")")


def remove_parenthesis(string: str) -> str:
    """
    Function to remove parenthesis from string
    Args:
        string (str): String to remove parenthesis from
    Returns:
        str: String without parenthesis
    """
    return string.replace("(", "").replace(")", "")


def multi_split(string: str, pattern: str) -> List[str]:
    """
    Function to split a string into multiple substrings based on regex pattern
    Args:
        string (str): String to split
        pattern (str): Pattern to split on
    Returns:
        List[str]: List of substrings
    """
    return re.split(pattern, string)


def predicate_splitter(string: str, pattern="AND|OR") -> List[str]:
    """
    Function to split a string into multiple substrings based on regex pattern
    Args:
        string (str): String to split
        pattern (str): Pattern to split on
    Returns:
        List[str]: List of substrings
    """
    return multi_split(string, pattern)


def get_files(path, suffix: tuple[str] | None = None) -> List[str]:
    """
    Function to get all files in a directory
    Args:
        path (str): Path to directory
        suffix (Optional[Tuple[str]], optional): Suffix to filter files. Defaults to None.
    Returns:
        List[str]: List of files
    """
    fullpaths = []
    for root, _, files in os.walk(path):
        for _file in files:
            if suffix and _file.endswith(suffix):
                fullpaths.append(os.path.join(root, _file))
    return fullpaths


def _map(func: Callable, data: List[Any]) -> List[Any]:
    """Wrapper over python's map fucntion"""
    return [*map(func, data)]


def _filter(func: Callable, data: List[Any]) -> List[Any]:
    """Wrapper over python map fucntion"""
    return [*filter(func, data)]
