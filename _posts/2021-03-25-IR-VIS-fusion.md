---
layout: post
title:  "IR VIS fusion"
date:   2021-03-25 10:04:26 +0800
categories: jekyll update
---

## Related Work
### 基于传统方法
基于传统的图像融合方法可分几类，有multi-scale transform, sparse representation, subspace, saliency-base methods, hybrid models等  

#### multi-scale transform 多尺度变换
首先对图像做多尺度变换，之后使用特定规则对分解后的图像进行融合，最后做逆变换生成融合图像

#### sparse representation 稀疏表示
稀疏表示是用字典中的元素（就是字典中的样本）的线性组合尽可能的描述（还原）测试样本

### 基于深度学习
基于深度学习的方法相比传统方法能够更好的提取图像特征，同时在一些方法中可以无需人工设计图像融合的规则和策略，常用的方法有CNN，GAN，Siamese network, autoencoder

### DDcGAN
https://github.com/jiayi-ma/DDcGAN

通过GAN实现红外可见光融合，generator产生融合图像，两个discriminator分别区分融合图像与红外和 可见光图像的差异，generator的目标是产生足够真实且同时包含红外和可见光信息的融合图像，使discriminator无法区分融合图像与原始图像,通过训练使generator生成的融合图像同时具备红外图像与可见光图像的特点。  
#### 量化评价指标
论文中采用的量化评价指标有entropy(EN)，mean gradient(MG)，spatial frequency(SF)，standard deviation(SD)，peak signal-to-noise ratio(PSNR)，correlation coefficient(CC)，structural similarity index measure(SSIM)，visual informates(roion fidelity(VIF)  
红外和可见光融合结果的评价指标不明确，ground truth也很难确认

### FusionGAN
第一个将GAN用于红外和可见光融合的端到端网络，在训练时首先将红外和可见光图像叠加(concatnate)在一起输入generator，generator生成同时带有红外和可见光特征的融合图像，同时将可见光图像输入给discriminator，discriminator试图将融合图像和可见光图像区分开，这样使generator产生的融合图像逐渐带有更多的可见光图像的细节   
generator和discriminator均由5个卷积层组成，discriminator本质上是一个分类器，用于区分融合图像和可见光图像   
由于图像数量有限，作者通过从原有图像剪裁patch的方式来丰富训练样本，从45对红外可见光图像对中剪裁出64381对patch，首先通过generator生成融合图像，然后将融合图像与可见光图像用于discriminator的训练，更新discriminator权重，之后将红外和可见光图像输入generator，更新generator权重


### U2Fusion
一种无监督的端到端的图像融合网络，可以针对多模态，多曝光，多焦点的场景,无需人工设计融合规则，  
在训练的阶段使用VGG16提取图像特征，之后对每一个feature map的每一个通道计算Laplacian算子，Frobenius范数，将两组feature map计算的结果通过softmax映射到0-1之间，来表示feature map对原始图像信息的保留程度，以此为依据设计loss  
两个输入图像进行concat操作后直接输入DenseNet生成融合图像，DenseNet由10个卷积层构成，通过训练时对loss的调整，DenseNet最后一层输出的特征图就是融合结果

### DensuFuse
采用encoder+fusion layer+decoder的方法，encoder和decoder分别包含4层3x3的卷积，encoder主要用于特征提取，这一部分使用MS COCO训练，decoder用于重构融合图像，作者提供了两种fusion layer的实现方法，一种是直接相加，即直接把红外和可见光图像分别经过encoder之后输出的feature map相加，另一种是基于L1 norm的融合方法，首先分别计算红外和可见光feature map的L1 norm，将两张图像的L1 norm相加，之后使用类似与加权平均的方法融合(相加)两组feature map。

### Infrared and visible image fusion using a deep learning framework
主要思路是将待融合的红外图像与视觉图像分解为基础部分与细节部分，之后分别对这两部分分别采取不同的策略进行融合得到融合基础部分与融合细节部分，最后利用这两部分重建融合图像