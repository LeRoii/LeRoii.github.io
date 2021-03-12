---
layout: post
title:  "python package and module"
date:   2021-03-09 16:26:25 +0800
categories: jekyll update
---

一个 `.py` 文件是一个module  
python中的 `import xxx` 和 `from xxx import yyy` 中的 `xxx` 一般都是module，即都能找到一个对应的`xxx.py`文件，`yyy`一般是`xxx.py`中定义的函数或类
使用自定义module需要将文件所在路径加入`PYTHONPATH`中，否则会提示出错  

一个package是一个包含__init__.py文件的目录(directory)，里面可以有0或多个module，使用package可以避免模块名冲突，通过
`package.module`的方式调用package中的module


![pythontestdir]({{site.usr}}/img/dir.png)

有文件结构如上的目录，在pythontest文件夹下有sdk文件夹，里面包含一个自己定义的package(pkg)，pkg模块含有一个module(pkg.py)和另一个package(subpkg)，subpkg有一个module(subpkgmodule)，testimport文件用来测试对各模块的引用，内容如下，testimport-inside.py和testimport-outside.py的内容相同，只是文件位置不同，但是在执行testimport-inside.py的时候会报错，testimport-outside.py的时候不会  

PYTHONPATH内容为
```
zpwnag@ubuntu20:/space/code/tmp/pythontest$ echo $PYTHONPATH
/opt/ros/noetic/lib/python3/dist-packages:/space/code/tmp/pythontest/sdk
```

testimport-inside.py/testimport-outside.py
```python
from pkg import pkgModuleFct
pkgModuleFct()
```

pkg.py
```python
from pkg.subpkg.subpkgmodule import subpkgModuleFct

def pkgModuleFct():
    print('pkg module fct in pkg.py')
```

pkgmodule.py
```python
from pkg.subpkg.subpkgmodule import subpkgModuleFct

def pkgModuleFct():
    print('pkg module fct in pkgmodule.py')
```

pkg中的__init__.py，这里面的程序会在import pkg的时候执行

```python
from .pkg import pkgModuleFct
print('import pkg!')
```
subpkgmodule.py
```python
def subpkgModuleFct():
    print('sub pkg module fct')
```
执行testimport-inside.py的结果
```
zpwnag@ubuntu20:/space/code/tmp/pythontest$ python sdk/pkg/testimport-inside.py 
Traceback (most recent call last):
  File "sdk/pkg/testimport-inside.py", line 1, in <module>
    from pkg import pkgModuleFct
  File "/space/code/tmp/pythontest/sdk/pkg/pkg.py", line 1, in <module>
    from pkg.subpkg.subpkgmodule import subpkgModuleFct
ModuleNotFoundError: No module named 'pkg.subpkg'; 'pkg' is not a package
zpwnag@ubuntu20:/space/code/tmp/pythontest$
```

执行testimport-outside.py的结果
```
zpwnag@ubuntu20:/space/code/tmp/pythontest$ python testimport-outside.py 
import pkg!
pkg module fct in pkg.py
zpwnag@ubuntu20:/space/code/tmp/pythontest$
```

如果把pkg中__init__.py的`from .pkg import pkgModuleFct`注释掉  
执行testimport-outside.py的结果
```
zpwnag@ubuntu20:/space/code/tmp/pythontest$ python testimport-outside.py 
import pkg!
Traceback (most recent call last):
  File "testimport-outside.py", line 2, in <module>
    from pkg import pkgModuleFct
ImportError: cannot import name 'pkgModuleFct' from 'pkg' (/space/code/tmp/pythontest/sdk/pkg/__init__.py)
zpwnag@ubuntu20:/space/code/tmp/pythontest$
```

这里`from pkg import pkgModuleFct`本意是从pkg.py的module中import pkgModuleFct这个函数，
但是因为pkg.py这个module的名字和pkg package的名字重复了，
解释器把这句话理解为从名为的pkg包中import名为pkgModuleFct的module
增加一个新的名为pkgModuleFct的module，内容为
```python
print('import pkgModuleFct.py')
```
执行testimport-outside.py的结果
```
zpwnag@ubuntu20:/space/code/tmp/pythontest$ python testimport-outside.py 
import pkg!
import pkgModuleFct.py
zpwnag@ubuntu20:/space/code/tmp/pythontest$
```

如果在pkg中__init__.py的加上`from .pkg import pkgModuleFct`，就是告诉解释器从当前目录下的pkg文件中引入pkgModuleFct，这样也不会出错

package和module的名字尽量不要重复
