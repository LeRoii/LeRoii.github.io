---
layout: article
title: Ubuntu 下 Python、OpenCV 与常用开发工具一周任务书
permalink: /tasks/ubuntu-python-opencv-week2/
section: tasks
description: 在 Ubuntu 本机完成 Python OpenCV 图像处理，练习 VS Code、Git、GitHub 和 SSH
---

# Ubuntu 下 Python、OpenCV 与常用开发工具一周任务书

> 适用对象：已完成《Ubuntu 与 OpenCV 开发环境一周任务书》的学生<br>
> 周期：1 周；建议周内 5 个晚上，每晚约 1.5～2 小时<br>
> 主开发平台：实验室 Ubuntu 台式机或笔记本，本机运行 Python 程序<br>
> 远程连接平台：学生自有 Windows 电脑可使用 MobaXterm；没有 Windows 电脑的学生使用 Ubuntu 自带的 SSH 客户端完成同等练习<br>
> 验收方式：学生在现场按本任务书逐项操作、记录结果，自行完成验收

> **动手前先阅读：** [Python、OpenCV 与开发工具基础概念](/workshop/python-opencv-devtools-concepts/)，了解 Python 与 C/C++ 的运行方式、图像处理流程、Git/GitHub、SSH/SFTP 和 conda 环境各自的作用。

## 一、这周要解决什么问题

上一周已经用 C/C++ 完成 Ubuntu 和 OpenCV 环境搭建。这一周用 Python 再做一次小型图像处理工程，并学习日常开发会反复用到的四件事：用 VS Code 编写和调试、用 Git 保存修改过程、用 GitHub 保存和分享代码、用 SSH 从另一台电脑连接 Ubuntu。

本周的 Python 程序必须首先在 **Ubuntu 本机的系统 Python 环境**运行成功。Anaconda 只放在提高任务中，不作为必做环境，也不用于替代本机环境的验收。

## 二、完成标准与成果

一周结束时，项目目录至少包含：

```text
opencv_week2/
├── README.md              # 运行方法、结果说明、自验收记录
├── .gitignore
├── src/
│   └── process_image.py   # 自己编写的 Python 程序
├── data/
│   └── input.jpg          # 自备、不含隐私的测试图片
└── output/
    ├── gray.jpg
    ├── blur.jpg
    └── edges.jpg
```

必须能够现场完成以下操作：

1. 在 Ubuntu 终端确认当前 Python、OpenCV 和 Git 的版本，说明 Python 程序实际使用哪个解释器。
2. 用 VS Code 打开整个项目目录，选择系统 Python 解释器，运行和修改程序。
3. Python 程序从命令行接收图片路径和输出目录，读取图片，生成灰度图、模糊图和边缘图；输入文件不存在时给出清楚的报错。
4. 修改边缘检测参数，再运行一次，指出输出发生了什么变化。
5. 用 Git 留下至少 **3 次有意义的提交**，能查看提交记录和工作区状态。
6. 将项目推送到自己的 GitHub 仓库，并能在网页上找到源码与 README。若现场网络确实无法连接 GitHub，先完成本地 Git 验收，在 README 中记录错误信息与待补做时间。
7. 从另一台电脑通过 SSH 登录上周装好的 Ubuntu 机器，执行 `hostname`、`pwd`，再传输一个不含隐私的小文本文件。自有 Windows 电脑可用 MobaXterm；没有 Windows 电脑则用另一台 Ubuntu 电脑的 SSH/SFTP 工具。

## 三、开始前的准备

- 上周的 Ubuntu 系统和基本网络可以正常使用；准备一张自摄或可公开使用的 `input.jpg`。
- 能用本人账号登录 Ubuntu，知道终端、文件管理器和浏览器的基本操作。
- 准备个人 GitHub 账号；仓库可设为 **private**，但现场应能在本人登录状态下查看。
- 远程连接练习以**上周自己安装的 Ubuntu 机器**为目标机；另备一台学生自有 Windows 电脑或另一台 Ubuntu 电脑。两台电脑应接入能够相互通信的网络。提前记住 Ubuntu 的用户名和登录密码。
- 不要把系统密码、GitHub 令牌、SSH 私钥写入代码、README、截图或仓库。

## 四、必做任务

### 任务 A：Ubuntu 本机 Python 与 OpenCV

在 Ubuntu 终端安装发行版提供的软件包：

```bash
sudo apt update
sudo apt install -y python3 python3-opencv python3-numpy git
python3 --version
python3 -c 'import sys, cv2; print(sys.executable); print(cv2.__version__)'
git --version
```

记录 `sys.executable` 的输出。它用于确认程序用的是哪个 Python。若 `import cv2` 失败，先检查是否选择了错误的解释器，不要直接在系统 Python 上运行 `sudo pip install`。本周统一使用 Ubuntu 软件仓库中的 `python3-opencv`，不同机器的 OpenCV 版本号不要求相同。

在项目目录中先建立 `src`、`data`、`output` 三个文件夹。创建 `src/hello.py` 并打印自己的姓名或小组代号，确认 `python3 src/hello.py` 能运行，再开始图像处理程序。

### 任务 B：用 VS Code 编写 Python 程序

从 [VS Code 官方下载页](https://code.visualstudio.com/download)安装适合 Ubuntu 的版本；在 VS Code 中安装 Microsoft 的 Python 扩展。使用 **“打开文件夹”** 打开 `opencv_week2`，通过 **Python: Select Interpreter** 选择本机的系统 Python（通常是 `/usr/bin/python3`）。在 VS Code 集成终端中再次运行任务 A 的版本检查命令。

独立编写 `src/process_image.py`，实现下面的流程：

```text
命令行参数：输入图片路径、输出目录、Canny 低阈值、Canny 高阈值
       ↓
读取输入图片；若读取失败，提示路径错误并退出
       ↓
灰度转换 → 高斯模糊 → Canny 边缘检测
       ↓
保存 gray.jpg、blur.jpg、edges.jpg；在终端输出保存位置
```

可参考的 OpenCV 函数：`cv2.imread`、`cv2.cvtColor`、`cv2.GaussianBlur`、`cv2.Canny`、`cv2.imwrite`。参数处理可先用 `sys.argv`，学有余力再用 `argparse`。输出目录可用 `pathlib.Path(...).mkdir(parents=True, exist_ok=True)` 创建。建议先固定阈值写通程序，再改成命令行参数。

约定四个位置参数依次为“输入图片、输出目录、低阈值、高阈值”。完成后应能在项目根目录运行：

```bash
python3 src/process_image.py data/input.jpg output 50 150
```

至少运行两组不同阈值，例如 `50,150` 和 `100,200`；两次运行之间先将第一组的 `edges.jpg` 复制为 `edges_50_150.jpg`，避免被覆盖。观察并用自己的话写出“边缘数量或细节如何变化”。还要用一条不存在的图片路径测试错误提示。

> 程序不要求实时摄像头、模型训练或图形界面。重点是把输入、处理、输出和错误处理连成一条可重复运行的流程。

<details markdown="1">
<summary>完成自己的程序并尝试排错后，再展开参考代码</summary>

下面是与上述四个位置参数对应的一个完整实现。先对照自己的程序找差异，再运行；不要直接复制后作为“独立编写”的成果。

```python
#!/usr/bin/env python3
"""读取一张图片，保存灰度、模糊和边缘检测结果。"""

import argparse
from pathlib import Path

import cv2


def main() -> int:
    parser = argparse.ArgumentParser(description="OpenCV 图像处理练习")
    parser.add_argument("input", type=Path, help="输入图片路径")
    parser.add_argument("output", type=Path, help="输出目录")
    parser.add_argument("low", type=int, help="Canny 低阈值")
    parser.add_argument("high", type=int, help="Canny 高阈值")
    args = parser.parse_args()

    if args.low < 0 or args.high < 0 or args.low >= args.high:
        parser.error("阈值应满足 0 ≤ 低阈值 < 高阈值")

    image = cv2.imread(str(args.input))
    if image is None:
        parser.error(f"无法读取图片：{args.input}；请检查路径和文件格式")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, args.low, args.high)

    args.output.mkdir(parents=True, exist_ok=True)
    for name, result in (
        ("gray.jpg", gray),
        ("blur.jpg", blur),
        ("edges.jpg", edges),
    ):
        path = args.output / name
        if not cv2.imwrite(str(path), result):
            parser.error(f"保存失败：{path}")
        print(f"已保存：{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

</details>

### 任务 C：用 Git 记录开发过程

在项目目录初始化 Git。先配置自己的姓名和邮箱；邮箱可以使用 GitHub 的隐私邮箱，不要求公开个人邮箱。

```bash
git init
git config user.name "你的姓名或代号"
git config user.email "你的邮箱"
git status
```

在 `.gitignore` 中排除 `__pycache__/`、`*.pyc`、`.vscode/` 和其他临时文件。建议提交节奏：① 项目结构与 README；② 能读取图片并保存灰度图；③ 加入模糊、边缘检测和错误提示。每次提交前使用 `git status` 检查要提交的文件，提交后使用 `git log --oneline` 回看过程。提交说明应写清楚改动，例如“加入图片读取和灰度输出”，不要连续使用“修改”“完成”等笼统文字。

第一次提交的基本命令如下；后续每完成一个阶段，重复检查、添加和提交：

```bash
git status
git add README.md .gitignore src/
git commit -m "建立项目结构和运行说明"
git log --oneline
```

不要将大型数据、个人照片、密码或令牌提交到仓库。测试图片若来源不适合公开，可只在本地保留，并在 README 说明如何自备图片。

### 任务 D：GitHub 保存项目

在 GitHub 创建自己的仓库（可选 private），将本地项目关联并推送。GitHub 登录和推送可以按官方文档选择 HTTPS 或 SSH 方式；GitHub 账号密码不能直接当作 Git 推送凭据。仓库网页上应能看到 `src/process_image.py`、`README.md` 和至少 3 次提交记录。

README 至少写明：项目做什么、Ubuntu 上使用的 Python/OpenCV 版本、准备图片的方法、运行命令、生成哪些文件、两组参数的观察结果、自己遇到的一个问题及解决过程。运行命令要能由同学照着复现，不能只写“点击运行”。

### 任务 E：SSH 与文件传输

先了解：**SSH** 是远程登录和执行命令；**SFTP** 是通过 SSH 安全传输文件。目标机就是上周自己装好 Ubuntu 的那台电脑。在这台 Ubuntu 电脑上检查用户名、局域网地址并安装 SSH 服务：

```bash
whoami
hostname -I
sudo apt update
sudo apt install -y openssh-server
sudo systemctl start ssh
systemctl status ssh --no-pager
```

`hostname -I` 可能显示多个地址，应选择与连接电脑位于同一网络的地址。`systemctl status` 出现 `active (running)` 才说明服务已启动。连接电脑应能访问目标机；若两台电脑处于隔离的校园 Wi-Fi，即使地址正确也可能无法连接，可换用同一可互通的局域网。参考 [Ubuntu 官方 OpenSSH 说明](https://ubuntu.com/server/docs/how-to/security/openssh-server/)。

- **自有 Windows 电脑路径**：安装 [MobaXterm Home Edition](https://mobaxterm.mobatek.net/download-home-edition.html)，新建 SSH 会话，填写上周 Ubuntu 电脑的 IP 和本人用户名；登录后运行 `hostname`、`pwd`，使用侧边 SFTP 面板传输一个 `hello_remote.txt`。
- **Ubuntu 电脑路径**：在另一台 Ubuntu 电脑用 `ssh 用户名@目标IP` 登录，运行相同命令；用 `sftp` 或 `scp` 传输同一个文本文件。

在 README 中写清楚“从哪类设备连接到上周的 Ubuntu 电脑、执行了什么命令、文件传输是否成功”，但不要记录密码、完整私人 IP 地址或其他人的账号。练习结束后，如果平时不需要远程登录，可在目标机运行 `sudo systemctl stop ssh`，关闭本次启动的 SSH 服务。

## 五、建议的一周节奏

| 时间 | 建议进度 | 当晚应留下的结果 |
| --- | --- | --- |
| 第 1 晚 | 检查系统 Python、OpenCV；搭建目录；安装 VS Code 扩展 | 版本信息、`hello.py` 运行结果 |
| 第 2 晚 | 完成读取图片、灰度和模糊输出 | 两张处理结果、第一和第二次 Git 提交 |
| 第 3 晚 | 完成 Canny、参数与错误提示 | 两组参数结果、第三次 Git 提交 |
| 第 4 晚 | 整理 README，推送 GitHub | 能打开的仓库页面与可复现命令 |
| 第 5 晚 | 完成 SSH/SFTP 练习，现场自验收并补缺 | 自验收记录、最后一次复现结果 |

可以按个人进度调整顺序，但不要把全部内容留到最后一天。

## 六、验收记录

在实验室现场亲自重新操作。勾选“通过”前必须看到实际结果；失败项记录现象和下一步处理，不凭记忆打勾。

| 检查项 | 自验收操作 | 结果 |
| --- | --- | --- |
| Python 与 OpenCV | 输出解释器路径和 OpenCV 版本，确认 VS Code 选中同一解释器 | □ 通过　□ 待补 |
| 图像处理 | 换一张图片，从终端运行程序，生成三张输出图 | □ 通过　□ 待补 |
| 参数理解 | 改变两个 Canny 阈值，说明图像变化 | □ 通过　□ 待补 |
| 错误处理 | 输入不存在的图片路径，看到明确提示且没有误生成结果 | □ 通过　□ 待补 |
| Git | `git status` 无意外文件，`git log --oneline` 有至少 3 次有意义提交 | □ 通过　□ 待补 |
| GitHub | 登录自己的仓库网页，找到源码、README 和提交记录 | □ 通过　□ 网络待补 |
| SSH/SFTP | 从另一台电脑登录，执行 `hostname`、`pwd` 并传输文本文件 | □ 通过　□ 环境待补 |
| 独立复现 | 关闭并重新打开 VS Code，按 README 的命令重新运行 | □ 通过　□ 待补 |

自验收结束时，在 README 记录日期、使用设备、未通过项和下一步计划。保留项目源码与 Git 历史，必要时可向同学展示操作过程，但自验收记录由本人填写。

## 七、提高任务：Anaconda（选做）

完成全部必做内容后，可以在个人电脑上安装 Anaconda Distribution 或 Miniconda，并在独立环境中再次运行同一个程序。它们都提供 `conda`；Anaconda Distribution 自带的软件较多，下载体积较大，Miniconda 是较小的起点。本节仅选做，**先保存好系统 Python 的必做验收结果**。

### 1. 安装并确认 conda

根据自己的系统，从 [Anaconda 官方下载页](https://www.anaconda.com/download)选择 Linux 或 Windows 安装包；Linux 的安装步骤可参考 [conda 官方 Linux 安装说明](https://docs.conda.io/projects/conda/en/stable/user-guide/install/linux.html)。核对安装包的系统类型和 CPU 架构。Windows 上双击官方安装包，按向导安装到个人目录，完成后打开 **Anaconda Prompt**。Ubuntu 上下载官方 `.sh` 安装包，在终端进入下载目录，用 `bash 文件名.sh` 启动安装器，阅读并按提示选择个人目录；安装完成后重新打开终端。不要用 `sudo` 把 conda 安装到系统目录。确认：

```bash
conda --version
conda info --envs
```

若 Ubuntu 终端提示 `conda: command not found`，先按安装向导提示完成 shell 初始化并重新打开终端，不要使用 `sudo conda`。安装过程中如询问是否每次打开终端自动激活 `base`，建议选择否，便于继续辨认系统 Python；若已自动进入 `(base)`，先运行 `conda deactivate`。

### 2. 创建独立环境并安装 OpenCV

在同一台电脑中创建名为 `week2_cv` 的环境。下面从 `conda-forge` 一次安装 Python、OpenCV 和 NumPy，避免分别从不同渠道拼装：

```bash
conda create -n week2_cv -c conda-forge python=3.11 opencv numpy
conda activate week2_cv
python -c "import sys, cv2; print(sys.executable); print(cv2.__version__)"
conda info --envs
```

如果当前系统或网络无法解析出这些软件包，记录错误，不影响必做任务。不要为完成选做内容卸载系统 Python 或修改前面用 `apt` 安装的 OpenCV。

### 3. 用同一份代码做对比

在**已激活**的环境中，进入原项目根目录，运行：

```bash
python src/process_image.py data/input.jpg output 50 150
```

打开 VS Code 时如果要用 conda 环境运行，应重新选择 `week2_cv` 对应的解释器。比较系统环境与 conda 环境的 `sys.executable`、`cv2.__version__`，并说明两者是否生成了同样的三类图片。完成后运行 `conda deactivate`，再确认 `python3 -c 'import sys; print(sys.executable)'` 的输出。将比较结果写入 README 的“提高任务”小节。

### 4. 选做达标检查

- [ ] 能说清 Anaconda Distribution、Miniconda、conda 和环境分别是什么。
- [ ] 能创建、激活、退出 `week2_cv`，并能指出当前使用的 Python 路径。
- [ ] 同一份 `process_image.py` 能在独立环境中运行。
- [ ] 用 3～5 句话解释为什么项目可能需要隔离环境，以及为什么本周必做仍使用系统 Python。

## 八、遇到问题时先查什么

| 现象 | 先检查 |
| --- | --- |
| 终端能 `import cv2`，VS Code 不能 | VS Code 选中的 Python 解释器是否与终端 `sys.executable` 一致 |
| `cv2.imread` 返回空值 | 图片路径是否正确、文件是否存在、是否有读取权限 |
| 输出图没有变化 | 是否重新运行程序、旧文件是否被覆盖、阈值是否真的传入程序 |
| `git push` 失败 | 网络、仓库地址、认证方式、错误信息；不要反复输入账号密码猜测 |
| SSH 连接失败 | 目标 IP、两台设备网络、目标机 SSH 服务状态、账号权限 |

记录问题时用“现象—自己猜测的原因—检查命令或操作—结果”四项写清楚，便于下次独立排查。

## 九、官方参考资料

- [Ubuntu 的 Python OpenCV 软件包](https://packages.ubuntu.com/python3-opencv)
- [VS Code：Python 入门与解释器选择](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub：设置 Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
- [GitHub：使用 Git](https://docs.github.com/en/get-started/using-git)
- [Ubuntu：OpenSSH 服务](https://ubuntu.com/server/docs/how-to/security/openssh-server/)
- [MobaXterm 文档](https://mobaxterm.mobatek.net/documentation.html)
- [Anaconda 下载与入门](https://www.anaconda.com/download)
- [conda：创建和管理环境](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
