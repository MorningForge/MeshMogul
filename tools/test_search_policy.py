#!/usr/bin/env python3
"""Regression tests for the narrow Foundations script exception."""
import unittest
from check_site import Document


class SearchPolicyTests(unittest.TestCase):
    def test_only_exact_deferred_module_on_hub(self):
        script = '<script src="../assets/foundations-search.js" defer></script>'
        self.assertEqual(Document(script, allow_search=True).errors, [])
        self.assertTrue(Document(script).errors)

    def test_rejects_other_scripts_and_execution_paths(self):
        forbidden = [
            '<script src="https://example.com/search.js" defer></script>',
            '<script src="//example.com/search.js" defer></script>',
            '<script src="../assets/other.js" defer></script>',
            '<script src="../assets/foundations-search.js"></script>',
            '<script src="../assets/foundations-search.js" defer async></script>',
            '<script src="../assets/foundations-search.js" defer>fetch("/")</script>',
            '<script>fetch("/")</script>',
            '<script src="../assets/foundations-search.js" defer></script>' * 2,
            '<img src="../assets/favicon.png" onerror="fetch(\'/\')">',
            '<a onclick="fetch(\'/\')">Click</a>',
        ]
        for source in forbidden:
            with self.subTest(source=source):
                self.assertTrue(Document(source, allow_search=True).errors)


if __name__ == '__main__':
    unittest.main()
