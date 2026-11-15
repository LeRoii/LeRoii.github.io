---
layout: article
title: Ubuntu 下 Python、OpenCV 与开发工具：基础概念说明
permalink: /workshop/python-opencv-devtools-concepts/
section: workshop
description: 对照第二周任务解释 Python、OpenCV、VS Code、Git、GitHub、SSH 与 conda
---

# Ubuntu 下 Python、OpenCV 与开发工具：基础概念说明

> 配套任务：[《Ubuntu 下 Python、OpenCV 与常用开发工具一周任务书》](/tasks/ubuntu-python-opencv-week2/)<br>
> 适用对象：已完成 Ubuntu、C/C++、OpenCV 入门任务，准备第一次用 Python 做图像处理的学生<br>
> 阅读方法：先读第 1 节建立全局认识，操作到哪个任务，再查相应章节

这份材料解释任务书中的工具**是什么、为什么要用、彼此怎样配合**。它不是要求你再安装一遍软件。读完后，你应能判断：一段程序到底在哪台电脑、由哪个 Python 运行；一张图片从哪里读入、到哪里输出；本地 Git 与 GitHub、SSH 与 SFTP、系统 Python 与 conda 环境分别有什么作用。

## 1. 一张图看清本周的开发流程

```text
上周装好的 Ubuntu 电脑
    │
    ├─ VS Code：编辑代码、选择 Python 解释器、查看报错
    │       ↓
    ├─ Python 解释器：执行 process_image.py
    │       ↓
    ├─ OpenCV：读取图片 → 灰度 → 模糊 → 边缘检测 → 保存图片
    │
    ├─ Git：在本机记录代码的每次有效变化
    │       ↓
    └─ GitHub：把 Git 提交推送到网络仓库

另一台电脑 ── SSH/SFTP ──→ 上周装好的 Ubuntu 电脑

选做：conda 独立环境 ──→ 用另一个 Python 和 OpenCV 再运行同一份代码
```

这里有三个不同的“位置”：**代码文件所在的位置**、**程序实际运行的位置**和**仓库保存的位置**。例如，你可以坐在 Windows 电脑前使用 MobaXterm，但通过 SSH 执行的命令运行在 Ubuntu 电脑上；GitHub 只保存推送上去的内容，不会替你运行图像处理程序。

| 任务书部分 | 本节需要理解的关键问题 |
| --- | --- |
| 任务 A | Python、解释器、包和版本之间是什么关系？ |
| 任务 B | VS Code 怎样调用 Python？图片如何变成边缘图？ |
| 任务 C | Git 为什么需要多次提交？`.gitignore` 做什么？ |
| 任务 D | Git 与 GitHub 为什么是两层？推送是什么意思？ |
| 任务 E | SSH 怎样跨电脑执行命令？SFTP 为什么能传文件？ |
| 提高任务 | conda 环境为什么能与系统 Python 并存？ |

## 2. Python 程序到底怎样运行

### 2.1 先与上周的 C/C++ 比一比

上周你编写了 `.c`、`.cpp` 文件，调用 GCC/G++（较大的工程还用 CMake 组织构建），得到可执行程序，再运行它。本周编写 `.py` 文件，在终端调用 Python 来运行。两种语言都能实现图像处理，也都要正确安装 OpenCV；差别主要在**代码写法、运行步骤和适用场景**。

| 对比点 | 上周的 C/C++ | 本周的 Python |
| --- | --- | --- |
| 源文件 | `.c`、`.cpp` | `.py` |
| 入门阶段的运行方式 | 先编译、链接，再运行生成的程序 | 调用 Python 解释器运行脚本 |
| 变量类型 | 通常需要写明类型，如 `int count` | 通常不用在变量名前声明类型，如 `count = 3`；运行时仍有类型检查 |
| 代码组织 | 语句、函数、头文件、库和构建配置 | 语句、函数、模块和包 |
| OpenCV 使用 | 包含头文件，并在构建时链接 OpenCV 库 | `import cv2`，由当前 Python 环境加载对应的包 |
| 适合本周练习的原因 | 有利于理解编译、链接和底层控制 | 用较少代码验证图像处理思路，便于快速调整参数 |

以同一个“输出一句话”为例，上周的 C 程序要先编译，本周的 Python 程序可直接交给解释器：

```bash
gcc hello.c -o hello_c
./hello_c

python3 hello.py
```

不要把表格理解为“Python 不会编译”或“C/C++ 不能快速试验”。Python 的常见实现会在内部处理字节码等运行细节；这里只比较你在这两周任务中**亲手操作的流程**。C/C++ 通常更适合需要严格控制资源和运行时间的设备端程序，Python 适合快速写出验证思路的程序和调用现成工具。电赛项目常会同时用到两者，因此要能读懂并选择合适的工具，而不是只学其中一种。

### 2.2 语言、脚本、解释器

**Python** 是编程语言，规定变量、函数、条件和循环等写法。`src/process_image.py` 是用这种语言写成的**源文件**，也常叫脚本。源文件本身只是文本，计算机不会因为你保存了它就自动执行。

**Python 解释器**是读取并执行 Python 代码的程序。在 Ubuntu 终端中输入：

```bash
python3 src/process_image.py data/input.jpg output 50 150
```

命令里的 `python3` 是解释器，后面是要运行的脚本和传给脚本的参数。可以把解释器理解为“读懂操作说明并逐步执行的人”，而 `.py` 文件是“操作说明”。任务书要求查看 `sys.executable`，就是要找到此刻真正工作的解释器文件路径。

Python 和 C/C++ 都需要明确依赖哪些库，代码也都可能因为路径、版本和输入错误而失败。换了语言，不代表可以跳过环境检查和结果验证。

### 2.3 `python`、`python3` 与解释器路径

一台电脑上可能同时存在多个 Python：Ubuntu 系统 Python、conda 环境中的 Python，以及其他软件附带的 Python。命令名相似，不代表调用的是同一个文件。

```bash
python3 -c 'import sys; print(sys.executable)'
```

`sys.executable` 输出当前解释器的实际路径。Ubuntu 本周必做任务通常使用 `/usr/bin/python3`；如果 VS Code 选择了另一个环境，即使终端里 `import cv2` 成功，编辑器运行时也可能报告 `No module named cv2`。诊断这类问题时，应先比较两边的 `sys.executable`，不要反复安装包。

### 2.4 模块、包、库与 `import cv2`

**模块**是可导入的代码单元；**包**通常把多个模块组织起来；日常说的**库**是可复用代码的泛称。OpenCV 是计算机视觉库，Python 中用 `import cv2` 访问它的功能。NumPy 是数值数组库，OpenCV 的 Python 图像对象通常与 NumPy 数组配合使用。

在 Ubuntu 中，`sudo apt install python3-opencv` 是让系统软件包管理器安装 Python 版 OpenCV；`import cv2` 是让**当前解释器**加载它。安装成功与加载成功是两步，所以任务书既让你安装，又让你执行 `python3 -c 'import cv2'`。不同 Ubuntu 版本的软件仓库可能提供不同 OpenCV 版本，只要任务所需函数存在并可运行即可。

### 2.5 APT、pip、conda 为什么不能随意混用

三者管理范围不同：

| 工具 | 主要管理对象 | 本周用途 |
| --- | --- | --- |
| `apt` | Ubuntu 的系统软件包及依赖 | 安装系统 Python、`python3-opencv`、Git、OpenSSH 服务 |
| `pip` | 某个 Python 环境里的 Python 包 | 本周必做不需要使用 |
| `conda` | 独立环境、Python 版本以及该环境的包 | 只用于选做提高任务 |

如果你在系统 Python 中随意使用 `sudo pip install`，可能让系统管理的软件与手工安装的软件相互覆盖，也可能遇到 Ubuntu 对系统 Python 的保护提示。任务书统一采用 `apt`，是为了让初学者在相同的 Ubuntu 环境中复现结果；提高任务再学习隔离环境。

## 3. VS Code、项目目录和命令行参数

### 3.1 VS Code 是编辑器，不是 Python

**VS Code** 帮你打开文件夹、编辑代码、提示语法、查看终端和调试程序。它不是 Python 解释器，也不会替你安装 OpenCV。**Python 扩展**让 VS Code 识别 Python 文件并选择解释器。因此“VS Code 能打开 `.py` 文件”与“程序能运行”是两回事。

任务书要求先“打开文件夹”，是为了把 `src/`、`data/`、`output/` 和 `README.md` 放在同一个项目视图中。若只打开单个文件，运行时的当前目录可能与你以为的项目根目录不同，`data/input.jpg` 就找不到。

### 3.2 路径、当前目录和输入输出

`data/input.jpg` 是**相对路径**，相对于当前工作目录，而不是相对于 `process_image.py` 所在目录。假设项目位于 `/home/student/opencv_week2`，在项目根目录运行时：

```text
当前目录：/home/student/opencv_week2
输入路径：data/input.jpg
实际文件：/home/student/opencv_week2/data/input.jpg
```

先用 `pwd` 看当前目录，用 `ls data` 看文件是否存在。若在 `src/` 内运行同一条命令，`data/input.jpg` 会被解释为 `src/data/input.jpg`，自然可能读取失败。任务书要求在 README 写完整运行命令，就是为了让其他人在正确目录复现。

### 3.3 四个位置参数代表什么

```bash
python3 src/process_image.py data/input.jpg output 50 150
```

| 位置 | 内容 | 作用 |
| --- | --- | --- |
| 1 | `src/process_image.py` | 要执行的脚本 |
| 2 | `data/input.jpg` | 输入图片路径 |
| 3 | `output` | 保存结果的目录 |
| 4 | `50` | Canny 低阈值 |
| 5 | `150` | Canny 高阈值 |

“四个位置参数”不包括脚本名。它们是脚本接收的四个值。`50` 和 `150` 从终端传来时原本是文字，程序需要把它们转换为整数；`argparse` 可以帮助检查参数数量和类型，并自动生成 `--help` 说明。

### 3.4 错误处理为什么也是成果

`cv2.imread` 读取失败时可能返回 `None`。如果不检查就继续做灰度转换，后面会出现不容易理解的错误。先检查输入是否存在、是否成功读取，再处理图像，报错就能指向真正的问题。

同样，保存结果时也要检查是否写入成功。一个程序“没有红字报错”，不等于结果文件已经正确生成。任务书要求现场换一张图片运行，是为了检验程序能否处理新输入，而不是只会展示上一次的图片。

## 4. OpenCV：从像素到边缘图

### 4.1 图像是数字，不是纸上的照片

电脑中的图片是按行列排列的**像素**。彩色图像的每个像素一般包含多个颜色通道；灰度图每个像素主要用一个亮度值表示。常见 8 位图像的通道值范围是 0～255，0 接近黑，255 接近白。

OpenCV 的 `imread` 默认读取彩色图像时使用 **BGR** 通道顺序，即蓝、绿、红；很多网页或绘图工具谈的是 RGB 顺序。用 `cv2.COLOR_BGR2GRAY` 转灰度时，写 BGR 是为了与 `imread` 的默认结果匹配。

### 4.2 为什么按“灰度 → 模糊 → 边缘”处理

| 步骤 | 常用函数 | 直观作用 | 本任务中的原因 |
| --- | --- | --- | --- |
| 读取 | `cv2.imread` | 把图片文件变为内存中的像素数据 | 后面的处理只能对成功读入的数据操作 |
| 灰度 | `cv2.cvtColor` | 用亮度表现画面 | 先把颜色信息简化，便于观察明暗变化 |
| 高斯模糊 | `cv2.GaussianBlur` | 平滑邻近像素 | 减少微小噪声造成的杂乱边缘 |
| 边缘检测 | `cv2.Canny` | 找出明显的亮度变化边界 | 得到适合观察轮廓的结果 |
| 保存 | `cv2.imwrite` | 把结果写成图片文件 | 方便比较两组参数和提交成果 |

`GaussianBlur(gray, (5, 5), 0)` 中的 `(5, 5)` 是所用邻域的大小；初学时可理解为“每个位置综合附近 5×5 范围的信息”。模糊不是让程序更高级，而是帮助边缘检测少受细碎噪声影响。保存灰度图、模糊图和边缘图，可以逐步定位哪一步出现问题。

### 4.3 Canny 的两个阈值

Canny 通过图像亮度变化判断哪些位置可能是边缘。它使用低阈值和高阈值：强变化更容易被认为是确定边缘，较弱变化要结合是否与强边缘相连来判断。程序里应满足 `0 ≤ 低阈值 < 高阈值`。

把阈值从 `50,150` 改为 `100,200`，通常会减少被保留的弱边缘，但具体结果取决于图片内容和前面的模糊处理。不要机械写“数值越大边缘一定越少”；应对照保存的两张结果图，说出**自己的图片**发生了什么变化。

### 4.4 同一份源码、不同参数

把输入图片和阈值写成命令行参数，是为了避免每换一张图片就改源代码。这样同一份程序可被重复使用：

```text
源码保持不变 + 输入/参数可变化 → 结果可比较、问题可复现
```

实验记录中保留参数和值，比只保留一张 `edges.jpg` 更有用；否则过几天可能已忘记这张图是怎样生成的。

## 5. Git：在本地留下可信的修改过程

### 5.1 Git 解决什么问题

写程序时常遇到：“昨天还能跑，今天改了几行就坏了”“两个文件都叫 final.py，不知道哪个是最新”。**Git** 是版本控制工具，可以记录某一时刻项目文件的状态，并说明这次改了什么。

一个项目的 Git 工作流程可以简化为：

```text
工作区：正在编辑的文件
   ↓ git add
暂存区：准备纳入下一次提交的改动
   ↓ git commit
本地仓库：已经保存的提交历史
   ↓ git push
GitHub 仓库：网络上的对应提交
```

`git add` 不等于已经提交，`git commit` 不等于已经上传 GitHub。任务书要求至少 3 次**有意义**的提交，是为了能看到“项目结构 → 读图与灰度 → 完整流程”的成长过程，而不是临时把最终代码拆成三次空泛提交。

### 5.2 状态、提交与忽略文件

- `git status`：查看哪些文件已修改、已暂存或尚未跟踪；提交前先看，避免误加文件。
- `git add`：选择要进入下一次提交的文件。
- `git commit -m "..."`：保存一条带说明的本地记录。
- `git log --oneline`：简要查看已有提交。
- `.gitignore`：告诉 Git 哪些**未被跟踪**的文件通常不应纳入仓库，例如 Python 缓存、编辑器本机配置。

`.gitignore` 不是安全保险箱：如果密码已提交过，再加入 `.gitignore` 不能把旧提交中的密码抹掉。因此要在第一次提交前就检查仓库内容；不要把密码、令牌、私钥、含个人信息的照片放进项目。

### 5.3 README 为什么是工程的一部分

`README.md` 是项目入口，回答“这是什么、怎样准备输入、怎样运行、应该看到什么、出了问题先检查什么”。对只看过你的仓库、没有听过你现场解释的人来说，README 就是最短的使用说明。任务书要求记录版本和运行命令，是为了让他人知道同一代码在什么环境和参数下得到结果。

## 6. GitHub：把本地提交放到网络仓库

**Git** 在本机就能工作，断网时仍可提交。**GitHub** 是托管 Git 仓库的网络平台，便于备份、共享和协作。创建 GitHub 账号并不会自动上传本机文件；只有将本地仓库与远程仓库关联，再执行 `git push`，对应的提交才会出现在 GitHub。

```text
Ubuntu 本地仓库 ── git push ──→ GitHub 仓库
Ubuntu 本地仓库 ←─ git pull / git fetch ── GitHub 仓库
```

**private 仓库**只对获准访问的人可见，但仍不能在其中放密码或私钥。网络故障时本地 Git 提交仍有效，可以先完成本机自验收，之后再补推送。推送需要合适的身份认证；GitHub 不把普通账号密码当作 Git 操作的直接凭据，按官方文档选择 HTTPS 的凭据管理方式或 SSH 密钥即可。

## 7. SSH、SFTP 与 MobaXterm：跨电脑操作

### 7.1 本地电脑、远程电脑与服务

本周把上周安装的 Ubuntu 电脑作为**目标机**，另一台 Windows 或 Ubuntu 电脑作为**连接端**。目标机运行 SSH 服务，连接端使用 SSH 客户端。两台电脑要有可互通的网络，连接端还需知道目标机的 IP 地址和 Ubuntu 用户名。

```text
连接端（Windows / Ubuntu）
       │ SSH 登录：发送命令、接收文本结果
       │ SFTP 传输：发送或取回文件
       ↓
目标机（上周装好的 Ubuntu，运行 SSH 服务）
```

SSH 登录成功后，终端里输入的 `hostname`、`pwd` 是在**目标 Ubuntu 电脑上运行**的。`hostname` 返回目标机名称；`pwd` 返回远程账号的当前目录。这两条命令可帮助你确认“我到底连到了哪台电脑、现在在哪个目录”。

### 7.2 IP 地址、用户名和端口

**IP 地址**是设备在网络中的地址；**用户名**决定以哪个账号登录；**端口**用于区分同一台电脑上的不同服务，SSH 默认使用 22 端口。任务书中的 `ssh 用户名@目标IP` 相当于说“以这个用户身份连接这台机器的 SSH 服务”。

`hostname -I` 可能显示不止一个地址，因为电脑可能有有线、无线、虚拟网络等多个接口。应使用连接端可达的局域网地址。两台设备都能上网，并不代表它们彼此能通信；某些校园 Wi-Fi 会隔离终端，这时连接会超时。

### 7.3 SSH、SFTP、MobaXterm 的关系

- **SSH**：加密的远程登录通道，主要用于执行命令。
- **SFTP**：基于 SSH 的安全文件传输，适合把 `hello_remote.txt` 送到 Ubuntu 或取回来。
- **MobaXterm**：Windows 上集成 SSH 终端和图形化 SFTP 文件浏览器的工具。它是客户端，不是 Ubuntu 的 SSH 服务。
- **OpenSSH**：Ubuntu 中常见的 SSH 客户端与服务端实现。`openssh-server` 安装在目标机，`ssh` 命令运行在连接端。

Windows 上使用 MobaXterm 与 Ubuntu 上使用 `ssh`/`sftp`，要验证的是同一件事：**能够远程登录，并能传输文件**。MobaXterm 的图形面板是操作方式，不能代替对“文件究竟在本机还是远程机器”的判断。

### 7.4 常见连接失败对应哪一层

| 现象 | 先检查的层次 |
| --- | --- |
| 连接超时 | 两台电脑的网络是否互通、目标 IP 是否选对 |
| 连接被拒绝 | 目标 Ubuntu 的 SSH 服务是否启动、端口是否可访问 |
| 提示认证失败 | 用户名、密码或密钥是否正确 |
| 登录成功但找不到文件 | 当前目录与文件所在机器是否弄错 |

排错时先区分“网络到不了”“服务没启动”“账号不正确”“路径不正确”，不要把所有情况都归结为“SSH 坏了”。

## 8. Anaconda 与 conda：选做内容为什么放在后面

### 8.1 四个容易混淆的名称

| 名称 | 是什么 |
| --- | --- |
| Anaconda Distribution | 打包了 conda、Python 和较多常用软件的发行套件 |
| Miniconda | 较小的安装起点，主要提供 conda、Python 和基础依赖 |
| conda | 创建环境、安装包和管理依赖的工具 |
| conda 环境 | 一套相对独立的 Python 和软件包组合，有自己的名称与路径 |

Anaconda 不是另一门编程语言。即使安装了 Anaconda，写的仍是 Python，调用的仍是 `cv2.imread` 等 OpenCV 函数。变化的是**由哪个 Python 解释器执行、OpenCV 安装在哪个环境中**。

### 8.2 为什么要创建环境

假设项目甲需要某个 Python 与 OpenCV 组合，项目乙需要另一个组合。如果都修改系统环境，容易相互影响。conda 可以分别建立 `project_a`、`project_b`，各自保存依赖。`conda activate week2_cv` 是把当前终端切换到这个环境；此时运行 `python`，应找到该环境里的解释器。`conda deactivate` 则退出当前环境。

本周先用系统 Python，是因为所有人刚完成同样的 Ubuntu 安装，可用同一套 `apt` 命令开始；选做 conda 是在掌握“解释器与包对应关系”之后，再比较另一种环境管理方法。不能只在 conda 里运行成功，就声称系统 Python 的必做任务已完成。

### 8.3 软件源与版本比较

`apt` 从 Ubuntu 软件仓库安装；`conda` 从配置的软件渠道安装，渠道也叫 **channel**。选做任务使用 `-c conda-forge` 指定渠道，创建 `week2_cv` 环境并安装所需包。两边的 Python 和 OpenCV 版本可能不同，这正是比较内容。`sys.executable` 给出最直接的证据，不能只看终端提示符的颜色或名称。

环境隔离有边界：它管理的是软件依赖，不会自动把你的代码、图片、Git 提交或 GitHub 仓库复制一份。同一份 `process_image.py` 可以在两个环境中运行，但输入文件和输出目录仍要按路径正确指定。

## 9. 自验收时怎样证明“真的会了”

软件版本截图只能证明某个软件曾显示过版本，不能证明能完成任务。现场自验收要做四件事：

1. **换输入**：换一张图片，确认程序仍能生成三张结果。
2. **改参数**：调整 Canny 阈值，观察并解释变化。
3. **看记录**：查看 Git 提交与 GitHub 页面，确认源码、README 和版本记录一致。
4. **跨电脑**：远程登录上周装好的 Ubuntu，确认命令运行位置并传输文件。

如果某一步失败，按“看到什么现象 → 猜测哪一层出错 → 用什么命令或操作检查 → 检查后得到什么结论”记录。**能定位问题**是开发能力的一部分；暂时没解决也要留下可复现的线索。

### 想一想

1. 为什么 Ubuntu 终端可以 `import cv2`，VS Code 里却提示找不到 `cv2`？首先查什么？
2. 在 `src/` 目录里运行程序，为什么 `data/input.jpg` 可能找不到？
3. 已经 `git commit`，为什么 GitHub 网页上仍看不到最新代码？
4. 在 Windows 上用 MobaXterm 登录 Ubuntu 后，`pwd` 显示的是哪台电脑的目录？
5. conda 环境中运行成功，为什么还要单独验证 Ubuntu 系统 Python？

## 10. 官方资料入口

- [Ubuntu：Python OpenCV 软件包](https://packages.ubuntu.com/python3-opencv)
- [VS Code：Python 入门与解释器选择](https://code.visualstudio.com/docs/python/python-tutorial)
- [OpenCV：图像处理教程](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [GitHub：Git 入门](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git)
- [Ubuntu：OpenSSH 服务](https://ubuntu.com/server/docs/how-to/security/openssh-server/)
- [MobaXterm：SSH 与 SFTP 功能](https://mobaxterm.mobatek.net/features.html)
- [conda：管理环境](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
