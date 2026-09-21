from pathlib import Path
import unittest


class HelloWorldPageTests(unittest.TestCase):
    def test_page_has_hello_world_heading(self):
        page = Path(__file__).parents[1] / "index.html"

        self.assertTrue(page.is_file())
        self.assertIn("<h1>Hello, World!</h1>", page.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
