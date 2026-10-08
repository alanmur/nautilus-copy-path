from pathlib import Path
import json
import tempfile
import unittest
from extension.copy_path import (
    format_single_path,
    format_multiple_paths,
    get_git_relative_path,
)


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_format_single_absolute(self):
        target = self.tmp_path / "sample.txt"
        target.touch()
        res = format_single_path(str(target), "absolute")
        self.assertEqual(res, str(target.resolve()))

    def test_format_single_tilde(self):
        home = Path.home()
        target = home / "test_file_copy.txt"
        res = format_single_path(str(target), "tilde")
        self.assertTrue(res.startswith("~"))

    def test_format_single_shell_spaces(self):
        target = self.tmp_path / "my folder with spaces" / "file name.txt"
        target.parent.mkdir()
        target.touch()
        res = format_single_path(str(target), "shell")
        self.assertTrue("'" in res or "\\" in res)

    def test_format_single_basename(self):
        target = self.tmp_path / "document.pdf"
        target.touch()
        self.assertEqual(format_single_path(str(target), "basename"), "document.pdf")

    def test_format_single_uri(self):
        target = self.tmp_path / "data.csv"
        target.touch()
        res = format_single_path(str(target), "uri")
        self.assertTrue(res.startswith("file://"))
        self.assertIn("data.csv", res)

    def test_format_single_markdown(self):
        target = self.tmp_path / "notes.md"
        target.touch()
        res = format_single_path(str(target), "markdown")
        self.assertTrue(res.startswith("[notes.md](file://"))

    def test_format_multiple_newline(self):
        f1 = self.tmp_path / "a.txt"
        f2 = self.tmp_path / "b.txt"
        f1.touch()
        f2.touch()
        res = format_multiple_paths([str(f1), str(f2)], "absolute")
        lines = res.splitlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], str(f1.resolve()))
        self.assertEqual(lines[1], str(f2.resolve()))

    def test_format_multiple_shell_spaced(self):
        f1 = self.tmp_path / "file one.txt"
        f2 = self.tmp_path / "file two.txt"
        f1.touch()
        f2.touch()
        res = format_multiple_paths([str(f1), str(f2)], "shell_spaced")
        self.assertIn(" ", res)
        self.assertTrue("'" in res or "\\" in res)

    def test_format_multiple_json(self):
        f1 = self.tmp_path / "item1.txt"
        f2 = self.tmp_path / "item2.txt"
        f1.touch()
        f2.touch()
        res = format_multiple_paths([str(f1), str(f2)], "json")
        data = json.loads(res)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], str(f1.resolve()))
        self.assertEqual(data[1], str(f2.resolve()))

    def test_git_relative_in_repo(self):
        repo_file = Path(__file__).resolve()
        rel = get_git_relative_path(str(repo_file))
        self.assertIsNotNone(rel)
        self.assertIn("test_formatter.py", rel)


if __name__ == "__main__":
    unittest.main()
