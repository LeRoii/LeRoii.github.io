---
layout: post
title:  "add images in github pages"
date:   2021-03-09 16:26:26 +0800
categories: jekyll update
---
markdown中添加图片的语法如下
```
![img](<path to image>)
```
`path to image`的设置决定了能不能顺利在生成的页面中看到图片，正确的做法应该是：
在与`_posts`同级的目录下建一个`img`文件夹用来存放需要显示的图片，
`path to image`设置为`{ {site.usr} }/img/dir.png`，
在`_config.yml`文件中设置`url`的值为github pages的地址