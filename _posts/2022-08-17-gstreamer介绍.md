---
layout: post
title:  "gstreamer介绍"
date:   2022-08-17 22:10:26 +0800
categories: jekyll update
---
<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

### gstreamer介绍
gstreamer是一个开源的，跨平台的多媒体框架，通过管道（Pipeline）的方式，将多媒体处理的各个步骤串联起来，
可以参考[这里](https://blog.csdn.net/quicmous/article/details/116916420?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164992915616782248547615%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=164992915616782248547615&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-116916420.nonecase&utm_term=%E7%AE%A1%E9%81%93&spm=1018.2226.3001.4450)

gstreamer的核心思想是通过各种元素(elements)和插件构造媒体管道流(pipeline)



### tips
- 可以通过`gst-inspect-1.0`查看插件的各种属性
- `video/x-raw`是cpu内存，`video/x-raw(memory:NVMM)`是gpu内存
- 元素之间通过!连接，两个相邻元素的输入输出必须对应
