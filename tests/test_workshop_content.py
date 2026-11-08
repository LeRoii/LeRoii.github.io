import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LECTURE = ROOT / "workshop/electronics-foundations.md"
CHAPTER4 = ROOT / "workshop/common-interface-foundations.md"
UBUNTU_OPENCV_CONCEPTS = ROOT / "workshop/ubuntu-opencv-concepts.md"


class WorkshopContentTests(unittest.TestCase):
    def test_workshop_index_and_lecture_routes(self):
        index = (ROOT / "workshop/index.md").read_text(encoding="utf-8")
        lecture = LECTURE.read_text(encoding="utf-8")
        chapter4 = CHAPTER4.read_text(encoding="utf-8")
        concepts = UBUNTU_OPENCV_CONCEPTS.read_text(encoding="utf-8")
        self.assertIn("permalink: /workshop/", index)
        self.assertIn("/workshop/electronics-foundations/", index)
        self.assertIn("/workshop/common-interface-foundations/", index)
        self.assertIn("/workshop/ubuntu-opencv-concepts/", index)
        self.assertIn("permalink: /workshop/electronics-foundations/", lecture)
        self.assertIn("permalink: /workshop/common-interface-foundations/", chapter4)
        self.assertIn("permalink: /workshop/ubuntu-opencv-concepts/", concepts)

    def test_lecture_has_three_chapters_and_no_training_task_sections(self):
        text = LECTURE.read_text(encoding="utf-8")
        for title in [
            "# 第1章 安全和基线测试",
            "# 第2章 焊接和返修",
            "# 第3章 万用表和直流电源",
        ]:
            self.assertEqual(text.count(title), 1)
        self.assertNotRegex(text, r"(?m)^## .*实训任务")

    def test_all_five_svg_references_exist_and_are_valid(self):
        text = LECTURE.read_text(encoding="utf-8")
        references = re.findall(r"\((/assets/images/electronics/[^)]+\.svg)\)", text)
        self.assertEqual(len(references), 5)
        self.assertEqual(len(set(references)), 5)
        for reference in references:
            path = ROOT / reference.lstrip("/")
            self.assertTrue(path.is_file(), f"missing {reference}")
            ET.parse(path)

    def test_chapter4_content_and_svg_assets(self):
        text = CHAPTER4.read_text(encoding="utf-8")
        self.assertEqual(text.count("# 第4章 共同接口基础"), 1)
        for phrase in ["示波器", "单片机最小系统", "GPIO", "UART", "统一接口表", "基线测试", "分组表"]:
            self.assertIn(phrase, text)
        self.assertNotRegex(text, r"(?m)^## .*实训任务")
        references = re.findall(r"\((/assets/images/electronics/figure-4-[^)]+\.svg)\)", text)
        self.assertEqual(len(set(references)), 4)
        for reference in references:
            path = ROOT / reference.lstrip("/")
            self.assertTrue(path.is_file(), f"missing {reference}")
            ET.parse(path)

    def test_ubuntu_opencv_concepts_and_svg_assets(self):
        text = UBUNTU_OPENCV_CONCEPTS.read_text(encoding="utf-8")
        for phrase in ["Ubuntu 与 OpenCV 开发基础概念", "ISO", "UEFI", "APT", "GCC", "CMake", "pkg-config", "cv::Mat", "概念与任务书对照表"]:
            self.assertIn(phrase, text)
        references = re.findall(r"\((/assets/images/electronics/figure-uoc-[^)]+\.svg)\)", text)
        self.assertEqual(len(set(references)), 3)
        for reference in references:
            path = ROOT / reference.lstrip("/")
            self.assertTrue(path.is_file(), f"missing {reference}")
            ET.parse(path)


if __name__ == "__main__":
    unittest.main()
