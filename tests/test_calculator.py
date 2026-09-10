#!/usr/bin/env python3
import pytest
from calculator import perform_operation

def test_add():
    assert perform_operation("+", 2.0, 3.0) == "2.0 + 3.0 = 5.0"

def test_subtract():
    assert perform_operation("-", 5.0, 2.0) == "5.0 - 2.0 = 3.0"

def test_multiply():
    assert perform_operation("*", 3.0, 4.0) == "3.0 * 4.0 = 12.0"

def test_divide():
    assert perform_operation("/", 7.0, 2.0) == "7.0 / 2.0 = 3.5"

def test_divide_by_zero():
    assert perform_operation("/", 1.0, 0.0) == "Error: Division by zero"

def test_power():
    assert perform_operation("^", 2.0, 3.0) == "2.0 ^ 3.0 = 8.0"

def test_remainder():
    assert perform_operation("%", 7.0, 3.0) == "7.0 % 3.0 = 1.0"

def test_remainder_by_zero():
    assert perform_operation("%", 1.0, 0.0) == "Error: Remainder by zero"

def test_unknown():
    assert perform_operation("x", 1.0, 2.0) == "Unknown operation"
