---
layout: post
title:  "Jetson xavier部署基于tkDNN-TensorRT加速的yolo"
date:   2021-03-17 17:24:25 +0800
categories: jekyll update
---

Yolov3和v4：
https://github.com/AlexeyAB/darknet

经过TensorRT加速的yolo：
https://github.com/ceccocats/tkDNN

tkDNN是基于TensorRT的深度神经网络推理引擎，在TensorRT api的基础上进行封装，提供了便利的接口可以直接将常用网络的权重转为TensorRT的形式，包括darknet,  resnet, centernet, mobilenetSSD。


加速效果
2x times for batch=1 and 3x-4x times for batch=4

使用tkDNN分两步，首先将网络原始模型分层输出成bin文件，  
https://github.com/ceccocats/tkDNN#how-to-export-weights
之后将bin文件解析转为.rt模型文件，对于darknet，tkDNN提供了接口可以直接调用  
https://github.com/ceccocats/tkDNN#darknet-parser  
得到的模型文件可以直接用TensorRT推理  
https://github.com/ceccocats/tkDNN#run-the-demo  


部署自己训练的模型  
Darknet训练出来的是.weight文件，首先需要.weight每一层转为.bin，  
https://github.com/ceccocats/tkDNN#1export-weights-from-darknet  
在layers和debug文件夹中分别得到了每一层的bin和debug文件  
.bin文件转.rt的代码在  
https://github.com/ceccocats/tkDNN/blob/master/tests/darknet/yolo4.cpp  
需要修改其中文件路径，编译，运行就能得到.rt文件  
使用.rt文件进行推理可以参考  
https://github.com/ceccocats/tkDNN/blob/master/demo/demo/demo.cpp  
 
