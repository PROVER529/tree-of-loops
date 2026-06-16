import unittest

from string_utils import normalize_title

class NormalizeTitleTest(unittest.TestCase):
def test_trims_outer_whitespace(self) -> None:
self.assertEqual(normalize_title("  hello world  "), "Hello World")

```
def test_collapses_repeated_spaces(self) -> None:
    self.assertEqual(normalize_title("hello   world"), "Hello World")

def test_collapses_tabs_and_newlines(self) -> None:
    self.assertEqual(normalize_title("tree\t of\n loops"), "Tree Of Loops")

def test_handles_mixed_whitespace(self) -> None:
    self.assertEqual(
        normalize_title("  branch   search\tengineering  "),
        "Branch Search Engineering",
    )
```

if **name** == "**main**":
unittest.main()
