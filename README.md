在学习`python`的过程中，使用`conda`管理环境，避免环境混乱。<br>
本仓库`python`选取的运行的环境是`3.10.20`<br>
其他具体环境可参考`environmental.yml`文件
### 配置conda环境
我的电脑原系统本身就有`python3`环境（Xcode里面自带），为避免不同项目因不同环境产生冲突，使用`conda`为不同项目提供不同的运行环境。
由于`Anaconda`占用空间较大，本次我选择安装`Miniconda`，但其非常精简，库需要自己手动安装。
##### 安装方式
1. `Anaconda`官网下载安装包安装
2. 命令行安装，官网上也有教程
##### 创建特定的环境
```
conda create -n environment_name python=版本号
```
这个过程终端会询问 `Proceed ([y]/n)?` 输入`y`即可
##### 查看已有的环境
```
conda env list
```
当时我创建特定环境之后，查看环境仍然使用的系统环境。
原因是我之前在系统的`~/.zrshc`文件手动配置了运行环境。解决办法就是找到那个命令行将那行代码注释掉即可。
##### 环境使用
```
# 进入环境
conda activate environment_name
# 退出环境
conda deactivate
```
##### 安装基础库
```
conda install 想安装的库
```
##### 使用Jupyter Notebook
安装`Jupyter`之后，进入所需环境之后，在命令行输入`jupyter notebook`，浏览器会自动打开。选择创建相关文件后，当前本地目录会生成一个`.ipynb`后缀名的文件。<br>
**这个时候千万不要关闭终端，关了之后浏览器上的服务就没了。** <br>
如果不想在浏览器中使用的话，可以在vs code里面装一个 `Jupyter`插件同样也可以使用

