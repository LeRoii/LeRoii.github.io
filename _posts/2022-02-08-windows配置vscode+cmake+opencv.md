---
layout: post
title:  "windows配置vscode+cmake+opencv开发环境"
date:   2022-02-08 09:53:26 +0800
categories: jekyll update
---

## step 1
下载`mingw`，`cmake`，`opencv`源码   
### mingw下载地址    
[https://sourceforge.net/projects/mingw-w64/files/mingw-w64/](https://sourceforge.net/projects/mingw-w64/files/mingw-w64/)

根据需要选不同的版本，32位选i686，64位选x86_64，其他随意   
下下来解压到一个文件夹即可，将bin文件添加到环境变量   
验证`mingw`安装完成   
`cmd`中输`gcc -v`，没有出错即安装完成   

### cmake下载地址   
[https://cmake.org/files/v3.17/](https://cmake.org/files/v3.17/)

后缀`.zip`的下下来没有gui，解压后可以直接用，   
后缀`.msi`需要安装，有gui   
验证`cmake`安装完成   
`cmd`中输`cmake --version`，显示版本号没有出错即安装完成

## step 2
### 编译`opencv`   
[https://blog.csdn.net/NeoZng/article/details/122778711](https://blog.csdn.net/NeoZng/article/details/122778711)

跟着这个操作即可完成   
## step 3
### 配置`vscode`环境    
需要安装的插件： 
`C/C++`, `C++ Intellisense`, `CMake`, `CMake Tools`   
安好之后最好重启一下`vscode`，`CMakeLists.txt`如下：
```
cmake_minimum_required(VERSION 2.8)

Project(test)

find_package(OpenCV REQUIRED)
message(STATUS "Opnecv ;ibrary status: ")
message(STATUS "> version: ${OpenCV_VERSION} ")
message(STATUS "libraries: ${OpenCV_LIBS} ")
message(STATUS "> include: ${OpenCV_INCLUDE_DIRS}  ")

include_directories(${OpenCV_INCLUDE_DIRS}) 
add_executable(test main.cpp)
target_link_libraries(test ${OpenCV_LIBS})
```

用vscode打开工程文件夹后会出现下图，选`yes`，会自动生成`build`文件夹
![cmake1]({{site.usr}}/img/cmake1.png)

如果插件都装好了vscode下面状态栏应该是这样
![cmake2]({{site.usr}}/img/cmake2.png)

第一次可能需要选一下编译器，点`No Kit Selected`，上面会弹出来一些选项，选择`mingw`
![cmake3]({{site.usr}}/img/cmake3.png)

点击`build`可以编译，点`[all]`选择要执行的文件
