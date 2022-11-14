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

### 基本概念
- Element   
Element是Gstreamer中最重要的对象类型之一。一个element实现一个功能（读取文件，解码，输出等），程序需要创建多个element，并按顺序将其串连起来，构成一个完整的pipeline。
- Pad  
Pad是一个element的输入/输出接口，分为src pad（生产数据）和sink pad（消费数据）两种。
两个element必须通过pad才能连接起来，pad拥有当前element能处理数据类型的能力（capabilities），会在连接时通过比较src pad和sink pad中所支持的能力，来选择最恰当的数据类型用于传输，如果element不支持，程序会直接退出。在element通过pad连接成功后，数据会从上一个element的src pad传到下一个element的sink pad然后进行处理。
当element支持多种数据处理能力时，我们可以通过Cap来指定数据类型   
下面的命令通过Cap指定了视频的宽高，videotestsrc会根据指定的宽高产生相应数据
```
gst-launch-1.0 videotestsrc ! "video/x-raw,width=1280,height=720" ! autovideosink
```
- Cap   
Cap(capabilities)指定了element的各种属性，一般用单引号或双引号括起来  


### tips
- 可以通过`gst-inspect-1.0`查看插件的各种属性
- `video/x-raw`是cpu内存，`video/x-raw(memory:NVMM)`是gpu内存
- 元素之间通过!连接，两个相邻元素的输入输出Pad必须对应，即前一个元素的输出是`video/x-raw`，后一个元素的输入也必须是`video/x-raw`，不能是`video/x-raw(memory:NVMM)`

- 显示videotest画面
```
gst-launch-1.0 videotestsrc ! video/x-raw, width=1920, height=1080 ! autovideosink
```
其中`videotestsrc`和`autovideosink`都属于*element*，  
通常“sink”插件可以将获取的视频流输出到显示器  
autovideosink is a video sink that automatically detects an appropriate video sink to use. It does so by scanning the registry for all elements that have "Sink" and "Video" in the class field of their element information, and also have a non-zero autoplugging rank.
- videotest存成jpg图像
```
gst-launch-1.0 videotestsrc num-buffers=1 ! video/x-raw, width=1920, height=1080 ! jpegenc ! filesink location=img.jpg
```

- videotest存成视频
```
gst-launch-1.0 videotestsrc num-buffers=200 ! 'video/x-raw, width=(int)1280, height=(int)720, format=(string)I420' ! omxh264enc ! qtmux ! filesink location=test.mp4 -e
```

- h264解码
```
gst-launch-1.0 filesrc location=./test.mp4 ! qtdemux ! queue ! h264parse ! nvv4l2decoder ! nv3dsink -e
```
`qtdemux`指的是`QuickTime demuxer`，  
`mux`指的是将视频文件，音频文件和字幕文件合并为某一个视频格式，比如mp4或mkv  
`demux`是`mux`的逆过程，就是从合成的多媒体文件中分解视频，音频和字幕  
`queue`用于多线程，在source pad上创建新线程，解耦sink和source pad上的处理