---
layout: post
title:  "nvidia jetson xavier setup"
date:   2021-08-31 09:53:26 +0800
categories: jekyll update
---

## 安装vscode
vscode官方提供arm版本，可以直接从官网下载

## 安装qt
```
sudo apt-get install qt5-default qtcreator -y
```

## 关闭gnome
- 进入命令行
```
sudo init 3
```

- 进入图像界面
```
sudo init 5
```

- 关掉图像界面
```
sudo systemctl set-default multi-user.target
```

- 打开图像界面
```
sudo systemctl set-default graphical.target
```

## 查看jetpack版本
```
cat /etc/nv_tegra_release
sudo apt-cache show nvidia-jetpack
```

## NX环境部署流程
1. 烧录镜像   
烧录与底板适配的l4t镜像，版本3261，[烧录方法](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3261/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/quick_start.html#)
2. 安装基本开发环境  
2.1 jetpack 4.6.1  
可以通过nvidia sdk manager安装，也可以apt-get install jetpack  
2.2 CJson
通过源码安装
```
mkdir build 
cd build
cmake ..
make 
```
2.3 mosquitto  
```
apt-get install mosquitto mosquitto-clients mosquitto-dev
```
通过源码安装，源码解压后
```
make
sudo make install
```
2.4 poco
通过源码安装，  
https://github.com/pocoproject/poco/tree/master

