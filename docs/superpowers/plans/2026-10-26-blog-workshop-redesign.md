# Blog Workshop Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有 Jekyll 个人博客改造成以“电子创新工作室资料”为首页重点、以“过往资料”承接旧文章的美观资料站，并发布前三章电子设计基础讲义。

**Architecture:** 继续使用 GitHub Pages 支持的 Jekyll 与 Minima 依赖，通过仓库内自定义布局和样式覆盖默认主题。首页、归档页、关于页和讲义页分别承担单一职责，旧 `_posts` 文件与永久链接保持不变。

**Tech Stack:** Jekyll 3.9、GitHub Pages、Liquid、HTML、SCSS、Markdown、SVG

**Spec:** `docs/superpowers/specs/2026-10-26-blog-workshop-redesign-design.md`

## Global Constraints

- 保留现有 `_posts` 文件名和历史文章链接。
- 首页只突出“电子创新工作室资料”，旧文章通过“过往资料”访问。
- 主按钮为 10-12px 圆角矩形，不使用胶囊形按钮。
- 讲义使用修订版 Markdown，包含5幅SVG，不包含三个“实训任务”小节。
- 不引入登录、评论、后台或新的静态站点框架。
- 只在本地修改和验证；不推送、不发布。

## Review Focus

- GitHub Pages 的 `baseurl` 为空时，所有内部链接和资源路径仍应从站点根目录正确解析。
- 长中文标题、宽表格和代码块在 390px 手机宽度下不得造成整页横向溢出。
- 讲义引用的5幅SVG必须全部存在且能够由浏览器加载。
- “过往资料”必须包含当前所有历史文章，且文章链接继续使用 Jekyll 生成的原路径。
- 无 JavaScript 时，导航、首页入口、章节锚点和文章阅读仍应可用。

---

### Task 1: 建立站点结构与导航

**Files:**
- Modify: `_config.yml`
- Create: `_layouts/default.html`
- Create: `_includes/site-header.html`
- Create: `_includes/site-footer.html`
- Modify: `index.markdown`
- Create: `archive.md`
- Modify: `about.markdown`

**Interfaces:**
- Consumes: 现有 `site.posts`、`site.title`、`site.description`。
- Produces: `/`、`/workshop/`、`/archive/`、`/about/` 四个稳定入口及共享导航。

- [ ] **Step 1:** 编写结构检查，断言配置和页面包含四个入口、栏目中文名称及 `site.posts` 归档循环。
- [ ] **Step 2:** 运行结构检查，确认因布局和栏目尚未创建而失败。
- [ ] **Step 3:** 创建共享布局和导航，更新站点元数据、首页、归档页和关于页。
- [ ] **Step 4:** 再次运行结构检查，确认四个入口和历史文章循环全部通过。

### Task 2: 导入工作室讲义与矢量图

**Files:**
- Create: `workshop/index.md`
- Create: `workshop/electronics-foundations.md`
- Create: `assets/images/electronics/figure-1-1-led-circuit.svg`
- Create: `assets/images/electronics/figure-2-1-solder-joint.svg`
- Create: `assets/images/electronics/figure-3-1-voltage-parallel.svg`
- Create: `assets/images/electronics/figure-3-2-current-series.svg`
- Create: `assets/images/electronics/figure-3-3-safe-powerup.svg`

**Interfaces:**
- Consumes: `电子设计基础训练自学讲义_第1-3章_修订版.md` 及其 `images/` 目录。
- Produces: `/workshop/` 资料入口和 `/workshop/electronics-foundations/` 长文讲义。

- [ ] **Step 1:** 编写内容检查，断言讲义包含三章、5个SVG引用，且不存在“实训任务”标题。
- [ ] **Step 2:** 运行检查，确认目标文件不存在时失败。
- [ ] **Step 3:** 添加 Jekyll front matter，迁移讲义正文，改写SVG路径并复制5幅图。
- [ ] **Step 4:** 运行内容检查，确认章节、图像、链接和删除项全部通过。

### Task 3: 实现所选视觉风格和响应式布局

**Files:**
- Create: `assets/css/style.scss`
- Create: `_layouts/home.html`
- Create: `_layouts/archive.html`
- Create: `_layouts/article.html`

**Interfaces:**
- Consumes: Task 1 的共享布局与 Task 2 的资料页面。
- Produces: 米白、深灰、电蓝的技术期刊风格，以及 `.button-primary` 10-12px 圆角矩形按钮。

- [ ] **Step 1:** 编写静态样式检查，断言主色变量、阅读宽度、按钮圆角、移动端断点和表格滚动规则存在。
- [ ] **Step 2:** 运行样式检查，确认样式与专用布局尚未创建时失败。
- [ ] **Step 3:** 实现首页、归档和文章布局，加入所选视觉稿中的标题层级、章节索引、示意电路装饰和圆角按钮。
- [ ] **Step 4:** 实现桌面与手机响应式样式，确保导航可换行、正文与表格不溢出。
- [ ] **Step 5:** 运行静态样式检查，确认全部规则通过。

### Task 4: 构建、链接与视觉验证

**Files:**
- Create: `scripts/verify_site.py`
- Output only: `_site/`（本地构建产物，不提交）

**Interfaces:**
- Consumes: 完成后的 Jekyll 源文件。
- Produces: 可由 GitHub Pages 构建的静态站点和验证报告。

- [ ] **Step 1:** 实现 `scripts/verify_site.py`，检查页面文件、front matter、内部链接、SVG XML、旧文章数量和禁止项。
- [ ] **Step 2:** 运行 `python3 scripts/verify_site.py`，要求零错误。
- [ ] **Step 3:** 安装或调用锁定版本 Bundler，运行 `bundle exec jekyll build`，要求构建成功。
- [ ] **Step 4:** 启动本地静态站点，以 1440×1024 和 390×844 截取首页、归档页和讲义页。
- [ ] **Step 5:** 检查截图中的导航、圆角按钮、长标题、表格、SVG和手机端溢出；修复后重新构建与截图。
- [ ] **Step 6:** 运行 `git diff --check`、`git status --short` 和最终验证脚本，记录未推送状态。
