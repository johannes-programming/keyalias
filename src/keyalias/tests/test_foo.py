import unittest
from typing import Any, Self

import setdoc

from keyalias import keyalias

__all__ = ["TestFoo"]


class TestFoo(unittest.TestCase):
    def test_foo(self: Self):
        @keyalias(bar=6)
        class Foo:
            @setdoc.basic
            def __init__(self: Self) -> None:
                self.data = list(range(10))  # Example list with 10 elements

            @setdoc.basic
            def __getitem__(self: Self, index: Any) -> Any:
                return self.data[index]

            @setdoc.basic
            def __setitem__(self: Self, index: Any, value: Any) -> None:
                self.data[index] = value

            @setdoc.basic
            def __delitem__(self: Self, index: Any) -> None:
                del self.data[index]

        # Create an instance of Foo
        my_instance: Foo
        my_instance = Foo()

        # Use the alias property to access index 6
        # Get the value at index 6
        self.assertEqual(
            my_instance.bar, # type: ignore[attr-defined]
            6,
        ) 

        # Set the value at index 6
        my_instance.bar = 42 # type: ignore[attr-defined]

        # Check the updated value at index 6
        self.assertEqual(
            my_instance.bar, # type: ignore[attr-defined]
            42,
        )  
        
        # Delete the value at index 6
        del my_instance.bar  # type: ignore[attr-defined]

        # Check the updated value at index 6
        self.assertEqual(
            my_instance.bar, # type: ignore[attr-defined]
            7,
        )  


if __name__ == "__main__":
    unittest.main()
