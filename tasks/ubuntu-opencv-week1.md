---
layout: article
title: Ubuntu 与 OpenCV 开发环境一周任务书
permalink: /tasks/ubuntu-opencv-week1/
section: tasks
description: 在实体计算机上完成 Ubuntu 独占安装、C/C++ 工具链配置和 OpenCV 基础工程
---

# Ubuntu 与 OpenCV 开发环境一周任务书

> 适用对象：电子创新工作室入门学生  
> 任务周期：1 周  
> 组织方式：结果清单型，学生自行安排具体时间  
> 操作平台：实体计算机（不是虚拟机）  
> 安装方式：Ubuntu 独占整块目标硬盘  

> **操作前请先阅读：** [Ubuntu 与 OpenCV 开发基础概念](/workshop/ubuntu-opencv-concepts/)。该讲义解释任务书中的 ISO、UEFI、分区、APT、GCC、CMake、pkg-config、OpenCV 和图像处理流程，帮助你先理解“这些是什么、为什么要做”，再开始操作。

## 一、任务说明

本任务要求你独立完成一次从“空白计算机”到“可以编译运行 OpenCV 程序”的完整环境搭建。教师只负责提供统一镜像、必要的安全提示和组织验收，不替学生完成安装、输入命令或修改程序。

本周不按“每天必须完成哪一步”考核，而按最终成果验收。你可以自行安排时间，但必须在一周结束前完成全部必做成果，并能够现场重新操作。

建议优先使用教师统一提供的 Ubuntu LTS 镜像。若教师未指定版本，可选用当前仍受支持的 Ubuntu Desktop LTS；截至 2026-11-02，Ubuntu 官方列出的最新桌面 LTS 为 **Ubuntu 26.04.1 LTS**，Ubuntu 24.04.5 LTS 也仍在标准支持期。不同版本的安装界面可能略有差异，但本任务的基本流程和命令相同。

## 二、任务目标

完成本任务后，你应能：

- 解释 Ubuntu LTS、ISO 镜像、启动盘、UEFI、分区和文件系统等基本概念；
- 独立制作 Ubuntu 启动 U 盘，并从 U 盘启动计算机；
- 确认备份和目标硬盘无误后，将 Ubuntu 以独占方式安装到指定硬盘；
- 使用终端完成软件更新和软件包安装；
- 使用 GCC、G++ 分别编译并运行简单的 C、C++ 程序；
- 使用 CMake 配置和构建一个小型 C++ 工程；
- 安装 Ubuntu 软件仓库提供的 OpenCV 开发包；
- 使用 OpenCV 读取图像，完成灰度转换、模糊和边缘检测并保存结果；
- 用“现象—假设—检查—结果”的方式记录和排查问题；
- 在不依赖他人操作的情况下，现场重新构建并运行自己的工程。

## 三、安全红线

> **重要安全提醒：**本任务采用“擦除磁盘并安装 Ubuntu / Erase disk and install Ubuntu”。该操作会清空所选目标硬盘上的原有系统、分区、软件和个人文件。删除的数据通常无法恢复。

以下条件没有全部满足时，**禁止点击安装界面中的最终确认按钮**：

- [ ] 已确认本机允许清除原系统，且不需要保留 Windows；
- [ ] 文档、照片、代码、聊天记录和浏览器资料等已备份到另一块存储设备或云端；
- [ ] 已随机打开至少 3 个备份文件，确认备份不是空目录或损坏文件；
- [ ] 已记录目标硬盘的品牌、型号和容量；
- [ ] 若计算机有多块硬盘，已确认哪一块可以清空；
- [ ] 启动 U 盘中的原有文件也已备份，因为制作启动盘会清空 U 盘；
- [ ] 已拍摄安装前的磁盘信息，照片中能清楚看到硬盘型号和容量；
- [ ] 笔记本已连接电源，安装过程中不得强制关机或拔出电源；
- [ ] 对安装界面中任何磁盘名称或容量存在疑问时，立即停止，不允许猜测。

## 四、准备条件

### 1. 硬件与资料

- 一台允许清空目标硬盘的 x86-64 台式机或笔记本；
- 一个容量不小于 12 GB 的 U 盘；
- 一个用于保存原始资料的移动硬盘、其他 U 盘或可靠云盘；
- 稳定网络；
- 教师提供或从 Ubuntu 官方网站下载的 Desktop LTS ISO 镜像；
- 一张自备测试图片，命名为 `input.jpg`，内容不得涉及个人隐私；
- 一份纸质或电子故障记录表。

### 2. 校验 Ubuntu 镜像

从 Ubuntu 官方网站下载 ISO 后，不要立即制作启动盘。先计算文件的 **SHA-256**，并与官方下载目录中的 `SHA256SUMS` 对比。两者必须完全一致；若不一致，应删除该 ISO 并重新下载。

Windows PowerShell 示例：

```powershell
Get-FileHash .\ubuntu-26.04.1-desktop-amd64.iso -Algorithm SHA256
```

Linux 示例：

```bash
sha256sum ubuntu-26.04.1-desktop-amd64.iso
```

实际文件名以教师提供或本人下载的镜像为准。将校验结果保存到提交材料中。不要使用来历不明的“精简版”“美化版”或第三方修改镜像。建议将命令输出复制到 `iso_sha256.txt`，同时记录对照的官方 `SHA256SUMS` 中对应行。

### 3. 双系统知识说明（本周只理解，不实装）

双系统是让 Windows 和 Ubuntu 共存，开机时选择进入哪个系统。它通常涉及 UEFI 启动、Windows BitLocker、Intel RST/AHCI、空闲分区、引导项和数据备份，操作复杂度明显高于独占安装。

本周不要求配置双系统，也不允许学生自行进行手动分区。后续需要双系统时，应先完成专项学习，并在教师指导下使用专门设备操作。

## 五、必做成果清单

### 成果 A：完成 Ubuntu 独占安装

- [ ] 使用官方 ISO 制作启动 U 盘；
- [ ] 从 U 盘进入 Ubuntu 安装环境；
- [ ] 再次核对目标硬盘的型号和容量后，选择“擦除磁盘并安装 Ubuntu”；
- [ ] 设置本人能够记住的用户名和密码；
- [ ] 安装完成后拔出 U 盘并正常进入桌面；
- [ ] 重新启动两次，均能正常进入系统；
- [ ] 声音、显示、键盘、鼠标和有线/无线网络至少完成基本检查；
- [ ] 使用以下命令记录系统信息：

```bash
mkdir -p ~/week1_evidence
cat /etc/os-release | tee ~/week1_evidence/os_release.txt
uname -a | tee ~/week1_evidence/uname.txt
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL \
  | tee ~/week1_evidence/lsblk.txt
```

> 提醒：`lsblk` 的作用是查看磁盘和分区。只允许查看，不要在不理解的情况下执行 `fdisk`、`parted`、`mkfs` 或 `dd` 等可能破坏数据的命令。

### 成果 B：完成基础 C/C++ 开发环境

先更新软件包索引并安装基础工具：

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y build-essential cmake git pkg-config
```

若 `sudo apt update` 或安装过程报错，不得继续复制大量未知命令。先记录完整报错，再按“常见问题排查”处理。

安装后执行：

```bash
gcc --version
g++ --version
cmake --version
git --version
pkg-config --version
```

将输出保存到 `evidence/tool_versions.txt`：

```bash
mkdir -p evidence
{
  gcc --version | head -n 1
  g++ --version | head -n 1
  cmake --version | head -n 1
  git --version
  pkg-config --version
} | tee evidence/tool_versions.txt
```

### 成果 C：独立编译 C 程序

新建 `hello_c.c`：

```c
#include <stdio.h>

int main(void) {
    printf("Hello, Ubuntu C!\n");
    return 0;
}
```

编译并运行：

```bash
gcc -Wall -Wextra -O2 hello_c.c -o hello_c
./hello_c
```

验收要求：

- 能解释源文件和可执行文件的区别；
- 能解释 `-Wall`、`-Wextra` 和 `-o` 的作用；
- 修改输出内容后重新编译，运行结果必须发生对应变化。

### 成果 D：独立编译 C++ 程序

新建 `hello_cpp.cpp`：

```cpp
#include <iostream>
#include <vector>

int main() {
    const std::vector<int> values{1, 2, 3, 4, 5};
    int sum = 0;
    for (const int value : values) {
        sum += value;
    }
    std::cout << "sum = " << sum << '\n';
    return 0;
}
```

编译并运行：

```bash
g++ -std=c++17 -Wall -Wextra -O2 hello_cpp.cpp -o hello_cpp
./hello_cpp
```

验收要求：

- 能说明为什么 C++ 程序使用 `g++`；
- 能修改数组内容，并预测修改后的求和结果；
- 不能只展示可执行文件，必须保留源码和编译命令。

### 成果 E：安装并确认 OpenCV

使用 Ubuntu 软件仓库安装 OpenCV 开发包：

```bash
sudo apt update
sudo apt install -y libopencv-dev
```

查看 OpenCV 版本：

```bash
pkg-config --modversion opencv4
```

若能输出版本号，说明 `pkg-config` 已找到 OpenCV。不同 Ubuntu LTS 中 OpenCV 的具体版本可能不同，不要求所有学生版本号完全一致。

### 成果 F：构建并运行 OpenCV 基础工程

#### 1. 创建目录

```bash
mkdir -p ~/opencv_week1/src ~/opencv_week1/data ~/opencv_week1/output
cd ~/opencv_week1
```

目录完成后应为：

```text
opencv_week1/
├── CMakeLists.txt
├── src/
│   └── main.cpp
├── data/
│   └── input.jpg
├── output/
└── build/            # 配置工程后生成
```

将测试图片复制为 `~/opencv_week1/data/input.jpg`。

#### 2. 编写 `src/main.cpp`

```cpp
#include <filesystem>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "用法: " << argv[0]
                  << " <输入图片> <输出目录>\n";
        return 1;
    }

    const std::filesystem::path input_path = argv[1];
    const std::filesystem::path output_dir = argv[2];
    std::filesystem::create_directories(output_dir);

    const cv::Mat image = cv::imread(input_path.string(), cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "读取图片失败: " << input_path << '\n';
        return 2;
    }

    cv::Mat gray;
    cv::Mat blurred;
    cv::Mat edges;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    cv::GaussianBlur(gray, blurred, cv::Size(5, 5), 1.2);
    cv::Canny(blurred, edges, 60, 150);

    const bool gray_ok = cv::imwrite((output_dir / "gray.jpg").string(), gray);
    const bool blurred_ok = cv::imwrite((output_dir / "blurred.jpg").string(), blurred);
    const bool edges_ok = cv::imwrite((output_dir / "edges.jpg").string(), edges);

    if (!gray_ok || !blurred_ok || !edges_ok) {
        std::cerr << "结果图片保存失败\n";
        return 3;
    }

    std::cout << "OpenCV version: " << CV_VERSION << '\n'
              << "输入尺寸: " << image.cols << " x " << image.rows << '\n'
              << "结果已保存到: " << output_dir << '\n';
    return 0;
}
```

#### 3. 编写 `CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.16)
project(opencv_week1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(OpenCV REQUIRED COMPONENTS core imgcodecs imgproc)

add_executable(opencv_week1 src/main.cpp)
target_link_libraries(opencv_week1 PRIVATE ${OpenCV_LIBS})
target_include_directories(opencv_week1 PRIVATE ${OpenCV_INCLUDE_DIRS})
target_compile_options(opencv_week1 PRIVATE -Wall -Wextra)
```

#### 4. 配置、构建和运行

在 `~/opencv_week1` 目录执行：

```bash
cmake -S . -B build
cmake --build build
./build/opencv_week1 data/input.jpg output
ls -lh output
```

运行成功后，`output` 目录至少包含：

- `gray.jpg`：灰度图；
- `blurred.jpg`：高斯模糊图；
- `edges.jpg`：Canny 边缘图。

用图像查看器打开 3 张结果图片，确认它们不是空文件，并能说明每一步处理的作用。

#### 5. 从空构建目录重新构建

现场验收前必须练习一次完整重建：

```bash
cd ~/opencv_week1
rm -rf build
cmake -S . -B build
cmake --build build
./build/opencv_week1 data/input.jpg output
```

`rm -rf build` 只能在确认当前目录为 `~/opencv_week1` 且目标仅为可重新生成的 `build` 目录时执行。禁止照抄此命令删除其他目录。

### 成果 G：形成故障记录

至少记录一个本人实际遇到的问题；若全程无错误，教师可在验收时指定一个可恢复故障，例如临时改错图片路径或文件名。

故障记录模板：

```text
日期和阶段：
现象（完整报错，不只写“不能运行”）：
当时执行的命令：
我的三个可能原因：
我先检查了什么，为什么：
检查结果：
最终原因：
解决方法：
如何避免再次发生：
```

## 六、提交材料清单

以“班级-姓名-UbuntuOpenCV第一周”为文件夹名称，提交以下内容：

```text
班级-姓名-UbuntuOpenCV第一周/
├── 01_安装与系统信息/
│   ├── 安装前磁盘信息.jpg
│   ├── iso_sha256.txt
│   ├── os_release.txt
│   ├── uname.txt
│   └── lsblk.txt
├── 02_基础编译/
│   ├── hello_c.c
│   ├── hello_cpp.cpp
│   └── 运行结果截图.png
├── 03_OpenCV工程/
│   ├── CMakeLists.txt
│   ├── src/main.cpp
│   ├── data/input.jpg
│   ├── output/gray.jpg
│   ├── output/blurred.jpg
│   └── output/edges.jpg
├── 04_过程记录/
│   ├── tool_versions.txt
│   ├── 故障记录.md
│   └── 一周总结.md
└── README.md
```

注意：

- 不提交 `build` 目录，验收时现场重新生成；
- 截图应能看到本人用户名、命令和完整输出，不能只截最后一行；
- 不要在截图或文件中暴露真实密码、个人密钥、访问令牌等敏感信息；
- `README.md` 应写明系统版本、OpenCV 版本、构建方法和运行方法；
- 一周总结不少于 300 字，重点说明“我能够独立完成什么”和“仍不会什么”。

## 七、现场验收

教师从以下项目中进行现场抽查。学生应当自己操作，不允许同伴代为输入命令。

| 验收项目 | 分值 | 达标证据 |
|---|---:|---|
| 安全与磁盘认识 | 15 | 能指出目标硬盘，说明独占安装的数据后果和备份方法 |
| Ubuntu 系统可用 | 15 | 正常启动，能查看系统版本、磁盘和网络信息 |
| C 程序编译运行 | 10 | 修改源码后使用 GCC 重新编译，结果正确 |
| C++ 程序编译运行 | 10 | 使用 G++ 和 C++17 编译，能解释基本命令 |
| 工具链确认 | 10 | 能查看 GCC、G++、CMake、Git、pkg-config 版本 |
| OpenCV 安装确认 | 10 | `pkg-config --modversion opencv4` 输出版本号 |
| OpenCV 工程重建 | 20 | 从空 `build` 目录配置、编译并运行成功 |
| 问题排查与表达 | 10 | 能复盘实际故障，或独立定位教师设置的简单错误 |
| **合计** | **100** |  |

判定规则：

- **基本达标**：总分不低于 70 分，且“安全与磁盘认识”“OpenCV 工程重建”均不得为 0 分；
- **需整改**：总分低于 70 分，或只能展示截图、不能现场重新操作；
- **优秀**：总分不低于 90 分，能够清楚解释 CMake、OpenCV 链接过程并完成至少一项提高任务。

## 八、建议进度

结果清单型任务不强制每天完成固定内容，但建议按以下节奏避免最后集中赶工：

| 建议阶段 | 建议完成内容 | 阶段检查点 |
|---|---|---|
| 前 1/3 周 | 备份、启动盘、目标硬盘自查、Ubuntu 独占安装 | 能连续两次正常启动，系统信息已保存 |
| 中间 1/3 周 | 系统更新、开发工具安装、C/C++ 编译 | 两个基础程序均可修改后重新编译 |
| 后 1/3 周 | OpenCV、CMake 工程、故障记录和整理材料 | 从空构建目录重建成功，提交目录完整 |

如果第 3 天结束时仍未完成 Ubuntu 安装，应主动向教师报告阻塞原因，不得等到最后一天。

## 九、常见问题排查

### 1. 计算机不能从 U 盘启动

依次检查：

1. U 盘是否确实通过镜像写入工具制作，而不是直接复制 ISO 文件；
2. 启动菜单中是否选择了带有 `UEFI` 标识的 U 盘；
3. ISO 是否来自 Ubuntu 官方网站；
4. 重新制作启动盘后是否仍失败；
5. 记录计算机型号、启动菜单照片和错误信息，交教师判断 Secure Boot 或硬件兼容问题。

不要在不理解的情况下随意修改 BIOS/UEFI 中的 SATA、RST、AHCI 或安全启动设置。

### 2. `sudo apt update` 失败

检查：

```bash
ping -c 4 archive.ubuntu.com
timedatectl
```

确认网络和系统时间是否正常，并保存 `apt` 的完整报错。不要把网上找到的未知软件源直接写入系统配置。

### 3. 找不到 `libopencv-dev`

先更新索引：

```bash
sudo apt update
apt policy libopencv-dev
```

若软件源未启用 `universe`，执行：

```bash
sudo add-apt-repository universe
sudo apt update
sudo apt install -y libopencv-dev
```

### 4. `pkg-config` 找不到 `opencv4`

检查：

```bash
dpkg -l | grep opencv
pkg-config --list-all | grep -i opencv
find /usr -name 'opencv4.pc' 2>/dev/null
```

若 `libopencv-dev` 没有成功安装，先解决安装问题；不要随意修改 `PKG_CONFIG_PATH` 掩盖错误。

### 5. CMake 报 `Could not find OpenCV`

依次执行：

```bash
pkg-config --modversion opencv4
dpkg -L libopencv-dev | grep 'OpenCVConfig.cmake'
rm -rf build
cmake -S . -B build
```

确认 `CMakeLists.txt` 中使用的是 `find_package(OpenCV REQUIRED ...)`，并检查拼写和大小写。

### 6. 程序提示“读取图片失败”

检查：

```bash
pwd
ls -lh data/input.jpg
file data/input.jpg
```

程序中的相对路径从“执行命令时所在的目录”开始计算。推荐始终在 `~/opencv_week1` 目录执行任务书中的运行命令。

### 7. 编译后运行的仍是旧结果

可能原因是修改后没有重新编译，或运行了另一个目录中的同名程序。执行：

```bash
cmake --build build --clean-first
./build/opencv_week1 data/input.jpg output
```

并使用 `pwd`、`ls -l build/opencv_week1` 确认当前路径和文件更新时间。

## 十、提高任务

提高任务只在全部必做成果通过后开展，任选其一即可：

1. 将高斯模糊核大小或 Canny 阈值改为命令行参数，并对比不同参数结果；
2. 使用 `cv::VideoCapture` 读取 USB 摄像头，显示或保存连续 100 帧；
3. 读取一个短视频，输出灰度视频或边缘检测视频；
4. 为工程添加第二个源文件和头文件，把图像处理封装为函数；
5. 初始化 Git 仓库，至少形成“初始工程、加入 OpenCV、完成图像处理”3 次有意义的提交；
6. 编写一个 `build.sh`，能够检查输入图片是否存在并自动完成配置、编译和运行。

## 十一、学生自检

提交前逐项确认：

- [ ] 我能说明独占安装与双系统的区别；
- [ ] 我能说明为什么必须备份，并能指出备份保存在哪里；
- [ ] 我能使用终端查看当前目录和文件；
- [ ] 我能独立使用 GCC、G++ 编译程序；
- [ ] 我能说明“编译错误”和“运行错误”的区别；
- [ ] 我能解释 `CMakeLists.txt` 中 `find_package`、`add_executable` 和 `target_link_libraries` 的作用；
- [ ] 我能从空 `build` 目录重新构建 OpenCV 工程；
- [ ] 我能说明灰度、模糊和边缘检测的基本作用；
- [ ] 我有一份真实、完整的故障记录；
- [ ] 我没有在提交材料中泄露密码或访问令牌。

## 十二、官方参考资料

以下链接均为官方资料，访问日期为 2026-11-02：

1. [Ubuntu 当前版本与支持周期](https://ubuntu.com/project/docs/release-team/list-of-releases/)：确认 LTS 版本和支持期限；
2. [下载 Ubuntu Desktop](https://ubuntu.com/download/desktop)：下载官方 Desktop ISO；
3. [Ubuntu Desktop 安装教程](https://ubuntu.com/tutorials/install-ubuntu-desktop)：启动盘、备份和安装总体流程；
4. [Ubuntu Desktop 磁盘安装说明](https://ubuntu.com/desktop/docs/en/24.04/tutorial/install-ubuntu-desktop/)：解释“擦除磁盘并安装 Ubuntu”和多硬盘选择风险；
5. [Ubuntu 软件包：libopencv-dev](https://packages.ubuntu.com/search?keywords=libopencv-dev)：确认不同 Ubuntu LTS 中的 OpenCV 开发包；
6. [OpenCV 官方 Linux 安装说明](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html)：编译器、CMake、Git 和 OpenCV 环境说明；
7. [CMake 官方教程](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)：CMake 工程和构建流程；
8. [GNU GCC 调用说明](https://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html)：GCC/G++ 编译流程；
9. [Git 官方 Linux 安装说明](https://git-scm.com/install/linux.html)：使用发行版软件包管理器安装 Git。

---

任务完成的标志不是“安装过”或“看过教程”，而是你能在教师面前从空构建目录开始，独立完成配置、编译、运行、解释和排错。
