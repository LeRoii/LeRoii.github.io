import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SiteStructureTests(unittest.TestCase):
    def test_shared_layout_and_navigation_exist(self):
        expected = [
            ROOT / "_layouts/default.html",
            ROOT / "_includes/site-header.html",
            ROOT / "_includes/site-footer.html",
        ]
        for path in expected:
            self.assertTrue(path.is_file(), f"missing {path.relative_to(ROOT)}")

        header = (ROOT / "_includes/site-header.html").read_text(encoding="utf-8")
        for label, href in [
            ("电子创新工作室资料", "/workshop/"),
            ("过往资料", "/archive/"),
            ("关于", "/about/"),
        ]:
            self.assertIn(label, header)
            self.assertIn(href, header)

    def test_public_pages_have_stable_permalinks(self):
        pages = {
            "index.markdown": "/",
            "archive.md": "/archive/",
            "about.markdown": "/about/",
        }
        for filename, permalink in pages.items():
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertRegex(text, rf"(?m)^permalink:\s*{re.escape(permalink)}\s*$")

    def test_archive_uses_all_existing_posts(self):
        archive = (ROOT / "archive.md").read_text(encoding="utf-8")
        self.assertIn("过往资料", archive)
        self.assertIn("site.posts", archive)

    def test_site_metadata_targets_github_pages_domain(self):
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        self.assertIn('title: "LeRoii\'s MEMO"', config)
        self.assertIn('url: "https://leroii.github.io"', config)
        self.assertIn("电子创新工作室资料", config)


if __name__ == "__main__":
    unittest.main()
