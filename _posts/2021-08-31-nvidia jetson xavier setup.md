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
### 进入命令行
```
sudo init 3
```

### 进入图像界面
```
sudo init 5
```

### 关掉图像界面
```
sudo systemctl set-default multi-user.target
```

### 打开图像界面
```
sudo systemctl set-default graphical.target
```