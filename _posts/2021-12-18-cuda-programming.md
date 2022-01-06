---
layout: post
title:  "cuda programming"
date:   2021-12-18 17:53:26 +0800
categories: jekyll update
---

## cuda中的基本概念
![img1]({{site.usr}}/img/cuda1.png)

### Host Device
Host是CPU，Device是GPU

### grid, block, thread
thread是最基本的执行单元，thread组成block，block组成grid，同一个block中的thread共享内存。  

### kernel函数的参数
kernel函数是thread执行的程序，形式如`Kernel<<<Dg,Db, Ns, S>>>(param list)`   
`Dg`：grid的维度，即一个grid有多少个block，类型可以是`int`或`dim3`   
`Db`：block的维度，即一个block有多少个thread，类型可以是`int`或`dim3`   
`Ns`：可选参数，用于设置每个block除了静态分配的shared Memory以外，最多能动态分配的shared memory大小，单位为byte。不需要动态分配时该值为0或省略不写.
`S`:可选参数，用于设置核函数运行在哪个流中，类型是`cudaStream_t`，初始为0    

https://developer.nvidia.com/blog/cuda-dynamic-parallelism-api-principles/
