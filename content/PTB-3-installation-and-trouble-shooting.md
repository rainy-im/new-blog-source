Title: PTB-3 安装手册
Date: 2015-1-4
Category: Psychology
Tags: Matlab, PTB-3, Psychology
Slug: PTB-3-installation-and-trouble-shooting
Authors: rainy
Keywords: PTB-3, Matlab, 心理学实验工具包, SYNCHRONIZATION FAILURE
Description: 这几年杂而不精的技术学习之旅
Summary: Psychtoolbox-3(PTB-3) 是一组 Matlab（或 [Octave](http://www.octave.org/)）的工具包，主要用来编写心理学实验程序。我分别尝试了在 Windows XP 系统的 Matlab 09b、Mac OSX 系统的 Octave 3.8.2 和 Matlab 14b 上安装 PTB-3 并运行了简单的 Demo，记录了一些安装过程中可能遇到的坑及解决方法。

### 1. 关于 [Psychtoolbox-3](http://psychtoolbox.org/)

Psychtoolbox-3(PTB-3) 是一组 Matlab（或 [Octave](http://www.octave.org/)）的工具包，主要用来编写心理学实验程序，之前的版本是 2，PTB-3 是在原先 2 的基础上通过重写一些 Matlab 相关的 C 扩展以更好地与 OpenGL 交互，代码也开源托管在 [GitHub](https://github.com/Psychtoolbox-3/Psychtoolbox-3) 上，可以非常方便地下载、安装不同的开发版本，遇到问题也可以与作者直接交流（如果作者原意理你的话:P）。

安装 PTB-3 首先需要安装 Matlab （如果没有版权又不想使用盗版可以尝试使用开源的替代方案 Octave），根据官网的文档说明：

> The current version supports Matlab 7.x and Octave 3.2.x on Mac OSX, Linux and Windows.

国内用 Linux 做心理学研究的应该还比较少，大多数应该还是使用 Windows 系统，我分别尝试了在 Windows XP 系统的 Matlab 09b、Mac OSX 系统的 Octave 3.8.2 和 Matlab 14b 上安装 PTB-3 并运行了简单的 Demo，记录了一些安装过程中可能遇到的坑及解决方法。

### 2. 系统与软、硬件要求

PTB-3 到目前为止最新的稳定版本为 [3.0.12](http://psychtoolbox.org/news/2014/11/05/Psychtoolbox-3.0.12-Released/)，从官网提供的 [System Requirements](http://psychtoolbox.org/requirements/) 文档中可以查看详细的系统与软、硬件需求，总体来说基本的趋势如下：

1. 向后兼容32位的 Matlab 及操作系统但最新的 3.0.12 及以后的版本将不再支持32位，因此以我们实验室的机器来看最多只能用 3.0.11 :(；
2. Matlab 与 Octave 基本上最新的版本不太会有问题，老的版本如果有问题安装出错会有提示；
3. 操作系统 Windows 主流的 XP、Win7 应该没有问题，最新升级的 Mac OSX 10.10 将布满了坑；
4. 其它硬件需求包括显卡、声卡基本上不是太老的机器都不会有问题，不过可能存在某些硬件驱动未安装的情况也会在安装过程中报错提示。

### 3. 下载安装

安装之前首先判断是否已经安装过旧的版本，在 Matlab 中输入

    :::matlab
    >> PsychtoolboxVersion
      ans =
    
    3.0.12 - Flavor:  - Corresponds to SVN Revision 
    For more info visit:
    https://github.com/Psychtoolbox-3/Psychtoolbox-3

想要删除旧的版本，需要找到旧版本的安装路径：

    :::matlab
    >> PsychtoolboxRoot
    
在 Matlab 中通过 `pathtool` 弹出搜索路径管理界面，Remove 掉所有旧版本的 PTB 相关的目录就可以了。Octave 也有类似的[路径管理命令](https://www.gnu.org/software/octave/doc/interpreter/Manipulating-the-Load-Path.html)，我用的最新版本可能是有 Bug ，`rmpath` 命令没有达到移除的效果，可以通过编辑`~/.octave` 文件直接删除掉里面与 PTB 相关的路径。

下载与安装新版本有两中方式，一种是下载官方提供的 [DownloadPsychtoolbox.m](https://raw.github.com/Psychtoolbox-3/Psychtoolbox-3/master/Psychtoolbox/DownloadPsychtoolbox.m)，并在 Matlab 中运行，则可以自动下载安装。

鉴于我们的网络状况我一般会用第二种方式，先去 GitHub 下载 Zip 压缩包，然后在本地安装（官网有提供最新的 [Zip File](https://github.com/Psychtoolbox-3/Psychtoolbox-3/zipball/master) 下载链接，如果想要其它版本则需要去 GitHub 选择下载），选择不同版本的下载方式如下：

![下载说明](/images/PTB-3-GitHub-Zip-Dl.png)

解压缩之后通过 Matlab 进入到解压后的目录中的 Psychtoolbox 子目录，执行：

    :::matlab
    % @/path/to/Psychtoolbox-3-PTB_Beta-2014-11-06_V3.0.12/Psychtoolbox 
    >> SetupPsychtoolbox
   
如果没有终止或报错，可以看到最后的 `Enjoy!`，就是安装成功！

### 4. 可能遇到的问题与解决方法

除了版本兼容性等问题，最容易出现的错误如下：

> ----- ! PTB - ERROR: SYNCHRONIZATION FAILURE ! ----

至于具体原因或背后的原理以后再说，解决方法有提示通过`help SyncTrouble`查看原因，（OSX系统中）一般与内核驱动有关，可以通过查看`help PsychtoolboxKernelDriver`寻找解决方案：

    :::bash
    cd /System/Library/Extensions/
    sudo unzip /PathToPsychtoolbox/Psychtoolbox/PsychHardware/PsychtoolboxKernelDriver64Bit.kext.zip

如果需要删除就的版本或升级则需要：

    :::bash
    sudo kextunload /System/Library/Extensions/PsychtoolboxKernelDriver.kext
    sudo rm -R /System/Library/Extensions/PsychtoolboxKernelDriver.kext
    
另外 OSX 10.10 需要额外的步骤：

    :::bash
    sudo nvram boot-args="kext-dev-mode=1"
    reboot

















