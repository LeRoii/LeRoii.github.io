import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VisualStyleTests(unittest.TestCase):
    def test_specialized_layouts_exist(self):
        for name in ["home.html", "archive.html", "article.html", "post.html"]:
            path = ROOT / "_layouts" / name
            self.assertTrue(path.is_file(), f"missing _layouts/{name}")

    def test_legacy_posts_are_wrapped_in_article_layout(self):
        post = (ROOT / "_layouts/post.html").read_text(encoding="utf-8")
        self.assertIn("layout: article", post)
        self.assertIn("{{ content }}", post)

    def test_home_has_selected_information_hierarchy(self):
        home = (ROOT / "_layouts/home.html").read_text(encoding="utf-8")
        for phrase in [
            "FEATURED",
            "电子创新工作室资料",
            "电子设计基础训练自学讲义（第1-3章）",
            "阅读讲义",
            "安全和基线测试",
            "焊接和返修",
            "万用表和直流电源",
        ]:
            self.assertIn(phrase, home)

    def test_styles_define_palette_reading_width_and_rounded_button(self):
        css = (ROOT / "assets/css/style.scss").read_text(encoding="utf-8")
        for variable in ["--paper", "--ink", "--blue", "--accent"]:
            self.assertIn(variable, css)
        self.assertRegex(css, r"\.button-primary\s*\{[^}]*border-radius:\s*(10|11|12)px", re.S)
        self.assertRegex(css, r"\.article-body\s*\{[^}]*max-width:\s*(760|780|800|820)px", re.S)

    def test_mobile_and_wide_content_rules_exist(self):
        css = (ROOT / "assets/css/style.scss").read_text(encoding="utf-8")
        self.assertRegex(css, r"@media\s*\(max-width:\s*720px\)")
        self.assertIn("overflow-x: auto", css)
        self.assertIn("overflow-wrap: anywhere", css)


if __name__ == "__main__":
    unittest.main()
