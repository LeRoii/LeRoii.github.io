---
layout: post
title:  "tensorflow-note"
date:   2021-04-27 09:19:26 +0800
categories: jekyll update
---

### tf.name_scope
1. 在某个tf.name_scope()指定的区域中定义的所有对象及各种操作，他们的“name”属性上会增加该命名区的区域名，用以区别对象属于哪个区域；  
2. 将不同的对象及操作放在由tf.name_scope()指定的区域中，便于在tensorboard中展示清晰的逻辑关系图，这点在复杂关系图中特别重要。


### tf.reduce_mean
计算张量沿指定轴上的平均值