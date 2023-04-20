---
title: MakeFile.Python & C++ Programe Toturial
cover: "/images/C-Language2.png"
tags: [Programe,C++,Python]
categories: [C++]
excerpt: 对于习惯IDE的Programmer来说 底层实际上是非常陌生的领域 然而下探到C++编译机制，对于一个合格的工程师又是非常有必要掌握的技术因此  本篇文章将讲解利用MakeFile 来实现Python C++混编的目的
---
# MakeFile.Python & C++ 混编教程 上

对于习惯IDE的Programmer来说 底层实际上是非常陌生的领域 然而下探到C++编译机制，对于一个合格的工程师又是非常有必要掌握的技术因此  本篇文章将讲解利用MakeFile 来实现Python C++混编的目的

首先不同平台的编译，存在着显著的差别：
>Linux/UnixLike平台的动态链接库一般为.so为结尾（shared object）
>
>Windows平台的动态链接库一般为.dll为结尾（Dynamic Link Library ）

## Linux Part：
### 编译器
在Linux中  主流编译器为Clang以及GNU（GCC，G++）
GCC中支持的语言常用的有
C、C++、Java、Object-C
结构类似于一个标准Unix编译器

而Clang是支持C++，CObject-C，Object-C++语言的编译器前端
其底层采用了LLVM底层虚拟机，在编译Object-C时对比GCC快三倍

总体上：


* GCC特性：

除支持C/C++/ Objective-C/Objective-C++语言外，还是支持Java/Ada/Fortran/Go等；当前的Clang的C++支持落后于GCC；支持更多平台；更流行，广泛使用，支持完备。

* Clang特性：

编译速度快；内存占用小；兼容GCC；设计清晰简单、容易理解，易于扩展增强；基于库的模块化设计，易于IDE集成；出错提示更友好


****
我们先以GCC为例讲解以下一个典型的C++编译指令是如何工作的

#### 一个典型的Unix like平台的 C++程序编译要经过哪些步骤？

![](https://img-blog.csdnimg.cn/img_convert/4ece889e044de7f9c8de37222789cb40.jpeg)


(更详细的解释参照[C++编译过程](https://blog.csdn.net/csdn_violin/article/details/79430384)，不再赘述)


而一个 gcc --h显示的帮助信息**最常用**的部分如下：
```bash
-B <directory>           Add <directory> to the compiler's search paths
#添加编译器的搜索路径（例如头文件等）
-v                       Display the programs invoked by the compiler
#显示被编译器调用的程序
-###                     Like -v but options quoted and commands not executed
-E                       Preprocess only; do not compile, assemble or link
#只预处理不编译汇编或者链接
-S                       Compile only; do not assemble or link
#只编译不汇编和链接
-c                       Compile and assemble, but do not link
#编译和汇编，不连接
-o <file>                Place the output into <file>
#输出到文件
-pie                     Create a position independent executable
#创建与位置无关的可执行文件
-shared                  Create a shared library
#创建一个共享库
```
我们来尝试编译一个helloworld
>main.cpp

```c++
#include<iostream>
using namespace std;
int main(){
    cout<<"c++ is best language"<<endl;
    return 0
}
```
对于这样一个非常基础的没有额外依赖的cpp文件来说，编译过程当然也相当简单。


```bash
g++ -c main.cpp
#只编译和汇编main.cpp不链接生成main.o的目标代码文件
```
如果我们还想执行这个代码就要生成可执行文件

```bash
g++ -o main.out main.o
#输出到.out可执行文件

#也可以合并执行
g++ -o hello.out hello.cpp
#直接编译并输出到可执行文件
```
则./xx.out 就可以运行编译完成的可执行文件了
但是这个并不是典型的应用场景  我们用下面的三个代码来模拟日常更常用的C++工作模式




>head.h

```c
#ifndef HEAD_H
#define HEAD_H
#include "head.h"
#include <iostream>
using namespace std;
class Human
{
private:
    /* data */
public:
void Say();
void SaywithPython();
};
#endif
```
>function.cpp

```c
#include "head.h"

void Human::Say(){
    cout<<"Im Human ,You are shit"<<endl;
}
void Human::SaywithPython(){
    cout<<"Python is best language"<<endl;
}

```

>main.cpp

```c
#include <iostream>
#include "head.h"
using namespace std;

int main(){
    cout <<"C++ is best language"<<endl;
    Human Jarvis;
    Jarvis.Say();
    return 0;

}
```

这一小段程序包含了非常多的技巧

首先定义了head以及function本地头文件和实现，在cpp文件中实现了
两个公开的方法

在main中又调用了实例化对象中的该方法

由于涉及了多个文件因此我们必须有一种方法来指定编译器的行为——MakeFile

```makefile
build : main.o function.o
	g++ -o build main.o function.o
main.o : main.cpp head.h
	g++ -g -c main.cpp
function.o : head.h function.cpp
	g++ -g -c function.cpp
clean :
	rm main.o function.o build
#pylib : function.cpp
#	g++ -o pylib.so -shared -fPIC function.cpp
```
其中整个的格式为：
```bash
target ... : prerequisites ...
　　command    #tab
```

* target为目标文件

* prerequisites为生成目标文件所需的文件

* command为编译该目标文件所需的指令

所以目前我们可以按照之前的C++编译流程图 整理出的依赖顺序为：
1.编译function.cpp依赖于head.h 生成function.o 即：
```bash
function.o : head.h function.cpp
	g++ -g -c function.cpp
```
2.编译main.cpp依赖于head.h 生成 main.o 即：

```bash
main.o : main.cpp head.h
	g++ -g -c main.cpp
```

3.编译可执行文件依赖于main.o function.o 生成指定的可执行文件（build）即：
```bash
build : main.o function.o
	g++ -o build main.o function.o
```
具体在执行过程中则遵循依赖，书写则从可执行文件开始（如果确实要生成可执行文件的话）

至此命令行中输入
```bash
make
```
就可以进行编译啦
```bash
#结果如同
g++ -g -c main.cpp
g++ -g -c function.cpp
g++ -o build main.o function.o
```
生成了build可执行文件
结果：
```bash
c++ is best language

Im Human ,You are shit
```
通过这一步我们解决了C++编译的问题，那我们怎么解决Python和C++的混编呢？

重新编写
>function.cpp

```c
#include "head.h"

void Human::Say(){
    cout<<"Im Human ,You are shit"<<endl;
}
void Human::SaywithPython(){
    cout<<"Python is best language"<<endl;

}

extern "C"{
    Human pythonman;
    void SaywithPython(){
        pythonman.SaywithPython();
        cout<<"C++ IS SHIT!!"<<endl;
    }
}
```

##### 通常来说，在模块的头文件中对本模块提供给其他模块引用的函数和全局变量以关键字extern声明。

Tips:

* extern是C/C++语言中表明函数和全局变量的作用范围的关键字，该关键字告诉编译器，其申明的函数和变量可以在本模块或其他模块中使用。


* 被extern "C"修饰的变量和函数是按照C语言方式进行编译和链接的

* extern int a; 仅仅是一个变量的声明，其并不是在定义变量a，并未为a分配空间。变量a在所有模块中作为一种全局变量只能被定义一次，否则会出错。

* extern对应的关键字是static，static表明变量或者函数只能在本模块中使用，因此，被static修饰的变量或者函数不可能被extern C修饰。



这一步的目的是通过MakeFile生成动态链接库，在Unix like系统中一般为.so文件：

```bash
build : main.o function.o
	g++ -o build main.o function.o
main.o : main.cpp head.h
	g++ -g -c main.cpp
function.o : head.h function.cpp
	g++ -g -c function.cpp
clean :
	rm main.o function.o build

pylib : function.cpp
	g++ -o pylib.so -shared -fPIC function.cpp
#通过 -shared 生成 .so文件
```

通过
```bash
make pylib
```
就可以生成pylib.so文件
此时我们开始建立python脚本

> main.py

```python
import ctypes
ll=ctypes.cdll.LoadLibrary
#载入动态链接库
lib=ll('/home/winshare/Leetcode/MakeFileTutorial/pylib.so')
#ll('动态链接库文件的地址')
lib.SaywithPython()
```
输出：
```bash
Python is best language
C++ IS SHIT!!
```
至此  我们完成了Python调用C++的实践

