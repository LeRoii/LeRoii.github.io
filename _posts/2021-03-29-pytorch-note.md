---
layout: post
title:  "pytorch-note"
date:   2021-03-29 17:34:26 +0800
categories: jekyll update
---

## pytorch

### Tensor
pytorch中的基本数据结构，类似于数组或矩阵，pytorch中的网络输入，输出以及参数都是存储在Tensor中，与Numpy的ndarrays不同的是Tensor可以运行在GPU和其他硬件加速器上
### Dataset&DataLoaders
Dataset和DataLoaders提供了操作数据集的接口，Dataset包含了很多常用数据集，可以直接在pytorch中使用
### torchvision.transforms
transforms模块用于对图像进行预处理，一般在输入网络之前需要将图像转为归一化的Tensor，常用的接口是ToTensor，它将图像或ndarray转为Tensor并且把像素值归一化在0-1之间，多个transform操作可以通过Compose封装

### torchvision.transforms.Normalize(mean, std, inplace=False)
mean和std是长度为n的一维list，n为图像通道数，一般是1(gray)或3(rgb),归一化的意思是```output[channel] = (input[channel] - mean[channel]) / std[channel]```

## Loss Function
### nn.MSELoss(Mean Square Error)
for regression task

### nn.NLLLoss(Negative Log Likelihood)
for classification

### nn.CrossEntropyLoss
combine nn.LogSoftmax and nn.LLLoss

## unsqueeze() & squeeze()
`unsqueeze()`函数起升维的作用,参数表示在哪个地方加一个维度   
`squeeze()`降维