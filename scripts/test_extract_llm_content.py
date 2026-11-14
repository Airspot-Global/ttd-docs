"""Tests for extract_llm_content.py. usage: python3 -I scripts/test_extract_llm_content.py"""
import os
import re
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract_llm_content.py")
URL = "https://open.thetradedesk.com/advertiser/docsApp/Test"

FLAT = """<html><body><article id="llm-content" class="llm-only">
<h2>Flat</h2>
<p>Intro with <code>code</code>.</p>
<table>
<thead><tr><th>Name</th><th>Value</th></tr></thead>
<tbody>
<tr><td>a|b</td><td>One <strong>two</strong></td></tr>
<tr><td>c</td><td><ul><li>x</li><li>y</li></ul></td></tr>
</tbody>
</table>
<p>After.</p>
</article></body></html>
"""

# Output of the extractor before the nested-table fix, captured on the fixture above.
FLAT_GOLDEN = """## Flat

Intro with `code`.

| Name | Value |
| --- | --- |
| a\\|b | One **two** |
| c | - x - y |

After.
"""

NESTED = """<article id="llm-content">
<table>
<thead><tr><th>Topic</th><th>What you need to know and do</th></tr></thead>
<tbody><tr><td>Change summary</td><td><p>We renamed the following names.</p>
<table>
<thead><tr><th>Type</th><th>Old</th><th>New</th></tr></thead>
<tbody>
<tr><td>Query</td><td>myReportsReportTemplates</td><td>reportingTemplates</td></tr>
<tr><td>Note</td><td>a|b</td><td>-</td></tr>
</tbody>
</table>
</td></tr>
<tr><td>Action required</td><td>Plan a migration.</td></tr>
</tbody>
</table>
</article>
"""

UNBALANCED = '<article id="llm-content"><table><tr><td>x</td></tr></table></table></article>'
STRAY_CELL = '<article id="llm-content"><p>x</p></td></article>'
UNCLOSED = '<article id="llm-content"><table><tr><td>x</td></tr></article>'
NO_ARTICLE = "<html><body><p>app shell</p></body></html>"


def run(html):
    with tempfile.NamedTemporaryFile("w", suffix=".page", delete=False, encoding="utf-8") as f:
        f.write(html)
    try:
        return subprocess.run([sys.executable, "-I", SCRIPT, f.name, URL], capture_output=True, text=True)
    finally:
        os.unlink(f.name)


class ExtractTest(unittest.TestCase):
    def test_flat_table_unchanged(self):
        r = run(FLAT)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, FLAT_GOLDEN)

    def test_nested_table_kept_in_outer_cell(self):
        r = run(NESTED)
        self.assertEqual(r.returncode, 0, r.stderr)
        out = r.stdout
        self.assertIn("| Topic | What you need to know and do |", out)
        self.assertIn("We renamed the following names.", out)
        self.assertIn("Query · myReportsReportTemplates · reportingTemplates", out)
        self.assertIn("| Action required | Plan a migration. |", out)
        self.assertEqual(out.count("a\\|b"), 1)
        self.assertNotIn("a\\\\|b", out)
        table = [ln for ln in out.splitlines() if ln.startswith("|")]
        self.assertEqual(len(table), 4)
        self.assertTrue(all(len(re.split(r"(?<!\\)\|", ln)) == 4 for ln in table))

    def test_extra_table_close_exits_3(self):
        self.assertEqual(run(UNBALANCED).returncode, 3)

    def test_cell_close_without_table_exits_3(self):
        self.assertEqual(run(STRAY_CELL).returncode, 3)

    def test_unclosed_table_exits_3(self):
        r = run(UNCLOSED)
        self.assertEqual(r.returncode, 3)
        self.assertEqual(r.stdout, "")

    def test_no_article_exits_2(self):
        self.assertEqual(run(NO_ARTICLE).returncode, 2)


if __name__ == "__main__":
    unittest.main()
