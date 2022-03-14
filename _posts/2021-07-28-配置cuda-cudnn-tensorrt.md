---
layout: post
title:  "配置cuda-cudnn-tensorrt"
date:   2021-07-28 17:41:26 +0800
categories: jekyll update
---

### ubuntu 配置开发环境

装好系统后，依次做更新显卡驱动，装cuda，装cudnn，装tensorrt，装ros

### 更新显卡驱动
点屏幕左下角show application，搜索Additional Drivers，选择nvidia官方驱动，更新完后重启电脑   
`nvidia-smi`能出现正常结果则驱动更新完成

为了方便整个安装流程，最好后面所有环境都通过.deb文件来装，因为如果想通过.deb文件来安装tensorrt，则cuda和cudnn必须通过.deb文件安装，  
而且三个库的版本必须对齐，cudnn和tensorrt都依赖cuda版本，必须根据cuda版本来选择对应的cudnn和tensorrt版本   

### 装cuda
搜索cuda即可找到nvidia cuda官方页面，里面有关于下载和安装的说明，一般会提供最新版本的连接，如果不想装最新版本，
在这里https://developer.nvidia.com/cuda-toolkit-archive

找以前的版本，cuda安装说明https://docs.nvidia.com/cuda/index.html#installation-guides

`nvcc -V`如果出现cuda版本号则安装完成    
这里会默认安装cuda和显卡驱动，可能会产生问题，最好选择只安装cuda toolkit，参考
https://zhuanlan.zhihu.com/p/143429249


### 装cudnn
同样搜索cudnn，选择对应版本，下载三个.deb文件，然后`sudo dpkg -i`   
以前的cudnn版本    
https://developer.nvidia.com/rdp/cudnn-archive   
cudnn安装说明    
https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html   
`find /usr -name cudnn.h`如果能找到头文件则安装成功    
`dpkg -l|grep cudnn`也可以用于验证是否安装了cudnn

### 装tensorrt
搜tensorrt，目前官方好像只提供了最新版本的tensorrt，archived页面没找到   
https://developer.nvidia.com/tensorrt   

下载地址，有之前的版本  
https://developer.nvidia.com/nvidia-tensorrt-download  
安装说明   
https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-debian   
验证安装   
`dpkg -l|grep TensorRT`  

### 装cmake
官网下载源文件后解压，进入文件夹
```
./bootstrap  
make   
sudo make install  
cmake --version
```

### OpenCV
参考https://www.cnblogs.com/carle-09/p/12377707.html


```
sudo cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local  -D OPENCV_GENERATE_PKGCONFIG=ON -DOPENCV_EXTRA_MODULES_PATH=/modules ..
```

```
cmake -D CMAKE_INSTALL_PREFIX=/usr/local -D CMAKE_BUILD_TYPE=Release -D OPENCV_GENERATE_PKGCONFIG=ON -D ENABLE_CXX11=1 -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D OPENCV_ENABLE_NONFREE=True -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=ON -D WITH_CUDA=ON -D WITH_TBB=ON -D ENABLE_FAST_MATH=1 -D WITH_OPENMP=ON -D WITH_CUFFT=ON -D WITH_CUBLAS=ON -D WITH_GTK=ON -D WITH_GTK_2_X=ON ..
```
