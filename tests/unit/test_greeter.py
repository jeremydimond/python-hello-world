from typing import Optional

import pytest

from src.helloworld.greeter import say_hello


@pytest.mark.parametrize(
    argnames=['name', 'expected_result'],
    argvalues=[
        ('Bob', 'Hello, Bob!'),
        (None, 'Hello!'),
    ]
)
def test_say_hello(name: Optional[str], expected_result: str):
    assert say_hello(name=name) == expected_result
