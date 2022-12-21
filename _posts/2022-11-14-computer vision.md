---
layout: post
title:  "computer vision"
date:   2022-11-14 19:13:26 +0800
categories: jekyll update
---

### 投影变换
投影变换就是把世界坐标系中的3D物体转换为图像坐标系中2D平面图形的过程。   
投影变换包括正交投影，透视投影(perspective projection)  
[参考](https://zhuanlan.zhihu.com/p/430306805)

### 仿射变换
仿射变换是投影变换的一种特殊形式，是一种二维坐标到二维坐标之间的线性变换，保持图形的平直性(straightness)和平行性(parallelness)，即变换后直线还是直线，曲线还是曲线，平行线还是平行线。   
仿射变换由基本的变换组合实现，包括平移(translation)、缩放(scale)、旋转(rotation)、错切(shear)。   
[参考](https://zhuanlan.zhihu.com/p/387408410)

### 图像梯度
梯度是一个向量，有大小和方向，梯度的方向是函数变化最快的方向。   
图像梯度的产生：图像中每两个像素做差，结果赋值给原来像素，像素之间的差值形成的图像就是梯度图像。  
图像梯度是指图像某像素在x和y两个方向上的变化率（与相邻像素比较），是一个二维向量，由2个分量组成X轴的变化、Y轴的变化。  
一维函数的一阶微分的定义是：   
$$
{df\over dx}=\lim_{\epsilon\to0}{f(x+\epsilon)-f(x)\over \epsilon}
$$
可以把图像看作是二维函数，二维函数偏微分的定义是：   
$$
{\partial f(x,y)\over \partial x}=\lim_{\epsilon\to0}{f(x+\epsilon,y)-f(x,y)\over \epsilon}
$$
$$
{\partial f(x,y)\over \partial y}=\lim_{\epsilon\to0}{f(x,y+\epsilon)-f(x,y)\over \epsilon}
$$
图像是一个离散的二维函数,$\epsilon$不能无限小，图像是按照像素来离散的，最小的$\epsilon$为1，因此上面的偏微分变为   
$$
{\partial f(x,y)\over \partial x}=f(x+1,y)-f(x,y)
$$
$$
{\partial f(x,y)\over \partial y}=f(x,y+1)-f(x,y)
$$
这分别是图像在(x, y)点处x方向和y方向上的梯度，从上面的表达式可以看出来，图像的梯度相当于2个相邻像素之间的差值。   
梯度与算子的关系参考[这里](https://blog.csdn.net/u013185349/article/details/84583572)

### 图像特征点
特征点可以理解为图像中具有代表性的点，例如边缘和角点，特征点由**关键点**和**描述子**构成   
* 关键点是指该特征点在图像里的位置，有些特征点还具有朝向、大小等信息   
* 描述子通常是一个向量，按照某种人为设计的方式，描述了该关键点周围像素的信息。描述子是按照“外观相似的特征应该有相似的描述子”的原则设计的。因此，只要两个特征点的描述子在向量空间上的距离相近，就可以认为它们是相同的特征点。

[参考](https://blog.csdn.net/qq_28087491/article/details/118805512)