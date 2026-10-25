import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VerifySiteCommandTests(unittest.TestCase):
    def test_verify_site_command_reports_success(self):
        script = ROOT / "scripts/verify_site.py"
        self.assertTrue(script.is_file(), "missing scripts/verify_site.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("site verification: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
