---
layout: post
title:  "numpy-note"
date:   2021-07-12 17:41:26 +0800
categories: jekyll update
---

np.array的乘法操作有*,multiply,dot,matmul,其中*和multiply是元素相乘，   
对于二维矩阵dot和matmul结果相同，都是矩阵乘法，dot会根据参数维度的不同产生不同的结果

```python
a = np.array([[1,2],[3,4]])
b = np.array([6,7]).reshape(-1,1)
c = np.array([[1,2],[3,4]])

#element wise, not matrix multiply
print("a*c:\n",a*c)
print("np.multiply(a,c):\n",np.multiply(a,c))
print("a*b:\n",a*b)
print("np.multiply(a,b):\n",np.multiply(a,b))
```
结果：  
```
a*c:
 [[ 1  4]
 [ 9 16]]
np.multiply(a,c):
 [[ 1  4]
 [ 9 16]]
a*b:
 [[ 6 12]
 [21 28]]
np.multiply(a,b):
 [[ 6 12]
 [21 28]]
```
```python
#matrix multiply
print("np.matmul(a,c):\n",np.matmul(a,c))
print("a.dot(c):\n",a.dot(c))
print("np.matmul(a,b):\n",np.matmul(a,b))
print("a.dot(b):\n",a.dot(b))
```
结果：
```
np.matmul(a,c):
 [[ 7 10]
 [15 22]]
a.dot(c):
 [[ 7 10]
 [15 22]]
np.matmul(a,b):
 [[20]
 [46]]
a.dot(b):
 [[20]
 [46]]
```

```python
c = a.dot(b)
print("c:",c)
inva = np.linalg.inv(a)
print('inva:',inva)
newb = inva.dot(c)
print('newb:',newb)

q = inva.dot(a)
print('q:',q)
```

结果：
```
c: [[20]
 [46]]
inva: [[-2.   1. ]
 [ 1.5 -0.5]]
newb: [[6.]
 [7.]]
q: [[1.00000000e+00 0.00000000e+00]
 [1.11022302e-16 1.00000000e+00]]
 ```

 ### notice
 如果要使用*来做矩阵乘法，需要使用np.matrix而不是np.array