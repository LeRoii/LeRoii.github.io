#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
errors = []


def require_file(relative):
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"missing file: {relative}")
    return path


required_files = [
    "_config.yml",
    "index.markdown",
    "archive.md",
    "about.markdown",
    "workshop/index.md",
    "workshop/electronics-foundations.md",
    "_layouts/default.html",
    "_layouts/home.html",
    "_layouts/archive.html",
    "_layouts/article.html",
    "_layouts/post.html",
    "_includes/site-header.html",
    "_includes/site-footer.html",
    "assets/css/style.scss",
]
for filename in required_files:
    require_file(filename)

routes = {
    "index.markdown": "/",
    "archive.md": "/archive/",
    "about.markdown": "/about/",
    "workshop/index.md": "/workshop/",
    "workshop/electronics-foundations.md": "/workshop/electronics-foundations/",
}
for filename, route in routes.items():
    path = ROOT / filename
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        if not re.search(rf"(?m)^permalink:\s*{re.escape(route)}\s*$", text):
            errors.append(f"wrong or missing permalink in {filename}: {route}")

posts = sorted((ROOT / "_posts").glob("*"))
if len(posts) != 23:
    errors.append(f"historical post count changed: expected 23, got {len(posts)}")

lecture = require_file("workshop/electronics-foundations.md")
if lecture.is_file():
    lecture_text = lecture.read_text(encoding="utf-8")
    for heading in [
        "# 第1章 安全和基线测试",
        "# 第2章 焊接和返修",
        "# 第3章 万用表和直流电源",
    ]:
        if lecture_text.count(heading) != 1:
            errors.append(f"lecture heading count is not 1: {heading}")
    if re.search(r"(?m)^## .*实训任务", lecture_text):
        errors.append("lecture still contains training-task section")
    svg_refs = re.findall(r"\((/assets/images/electronics/[^)]+\.svg)\)", lecture_text)
    if len(svg_refs) != 5 or len(set(svg_refs)) != 5:
        errors.append(f"expected 5 unique SVG references, got {len(svg_refs)}")
    for reference in svg_refs:
        path = ROOT / reference.lstrip("/")
        if not path.is_file():
            errors.append(f"missing SVG reference target: {reference}")
            continue
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"invalid SVG XML {reference}: {exc}")

header = require_file("_includes/site-header.html")
if header.is_file():
    header_text = header.read_text(encoding="utf-8")
    for label, route in [
        ("电子创新工作室资料", "/workshop/"),
        ("过往资料", "/archive/"),
        ("关于", "/about/"),
    ]:
        if label not in header_text or route not in header_text:
            errors.append(f"navigation entry missing: {label} -> {route}")

css = require_file("assets/css/style.scss")
if css.is_file():
    css_text = css.read_text(encoding="utf-8")
    checks = {
        "rounded primary button": r"\.button-primary\s*\{[^}]*border-radius:\s*12px",
        "mobile breakpoint": r"@media\s*\(max-width:\s*720px\)",
        "wide-content scroll": r"overflow-x:\s*auto",
        "long-title wrapping": r"overflow-wrap:\s*anywhere",
    }
    for name, pattern in checks.items():
        if not re.search(pattern, css_text, flags=re.S):
            errors.append(f"missing CSS rule: {name}")

if errors:
    print("site verification: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("site verification: PASS")
print(f"historical posts: {len(posts)}")
print("workshop chapters: 3")
print("workshop SVGs: 5")
