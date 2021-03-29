---
layout: post
title:  "IR VIS fusion"
date:   2021-03-25 10:04:26 +0800
categories: jekyll update
---

### DDcGAN
https://github.com/jiayi-ma/DDcGAN

通过GAN实现红外可见光融合，generator产生融合图像，两个discriminator分别区分融合图像与红外和 可见光图像的差异，generator的目标是产生足够真实且同时包含红外和可见光信息的融合图像，使discriminator无法区分融合图像与原始图像,通过训练使generator生成的融合图像同时具备红外图像与可见光图像的特点。  
#### 量化评价指标
论文中采用的量化评价指标有entropy(EN)，mean gradient(MG)，spatial frequency(SF)，standard deviation(SD)，peak signal-to-noise ratio(PSNR)，correlation coefficient(CC)，structural similarity index measure(SSIM)，visual information fidelity(VIF)

### DensuFuse
采用encoder+fusion layer+decoder的方法，encoder和decoder分别包含4层3x3的卷积，encoder主要用于特征提取，这一部分使用MS COCO训练，decoder用于重构融合图像，作者提供了两种fusion layer的实现方法，一种是直接相加，即直接把红外和可见光图像分别经过encoder之后输出的feature map相加，另一种是基于L1 norm的融合方法，首先分别计算红外和可见光feature map的L1 norm，将两张图像的L1 norm相加，之后使用类似与加权平均的方法融合(相加)两组feature map。

### Infrared and visible image fusion using a deep learning framework
主要思路是将待融合的红外图像与视觉图像分解为基础部分与细节部分，之后分别对这两部分分别采取不同的策略进行融合得到融合基础部分与融合细节部分，最后利用这两部分重建融合图像