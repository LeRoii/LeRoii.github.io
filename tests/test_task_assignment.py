import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_INDEX = ROOT / "tasks/index.md"
TASK_PAGE = ROOT / "tasks/ubuntu-opencv-week1.md"


class TaskAssignmentTests(unittest.TestCase):
    def test_navigation_links_to_task_assignment_section(self):
        header = (ROOT / "_includes/site-header.html").read_text(encoding="utf-8")
        self.assertIn("任务分配", header)
        self.assertIn("/tasks/", header)
        self.assertRegex(header, r"page\.section\s*==\s*'tasks'")

    def test_task_section_has_stable_routes_and_entry(self):
        self.assertTrue(TASK_INDEX.is_file())
        self.assertTrue(TASK_PAGE.is_file())
        index = TASK_INDEX.read_text(encoding="utf-8")
        page = TASK_PAGE.read_text(encoding="utf-8")
        self.assertRegex(index, r"(?m)^permalink:\s*/tasks/\s*$")
        self.assertRegex(page, r"(?m)^permalink:\s*/tasks/ubuntu-opencv-week1/\s*$")
        self.assertIn("/tasks/ubuntu-opencv-week1/", index)
        self.assertRegex(index, r"(?m)^section:\s*tasks\s*$")
        self.assertRegex(page, r"(?m)^section:\s*tasks\s*$")

    def test_published_task_removes_teacher_confirmation_but_keeps_safety(self):
        text = TASK_PAGE.read_text(encoding="utf-8")
        for removed in ["教师确认栏", "教师签字", "安装前教师确认表"]:
            self.assertNotIn(removed, text)
        for retained in ["安全红线", "备份", "目标硬盘", "SHA-256", "OpenCV 工程重建"]:
            self.assertIn(retained, text)
        self.assertNotIn("[!CAUTION]", text)

    def test_article_layout_links_tasks_breadcrumb_to_section(self):
        layout = (ROOT / "_layouts/article.html").read_text(encoding="utf-8")
        self.assertRegex(layout, r"page\.section\s*==\s*'tasks'")
        self.assertIn("/tasks/", layout)


if __name__ == "__main__":
    unittest.main()
