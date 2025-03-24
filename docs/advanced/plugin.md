# FiberArt插件开发教程

## 插件安装

1. 打开FiberArt
2. 在菜单栏选择**插件**,然后点击**插件管理**
3. 在弹出的界面中点击**安装插件**
4. 在文件选择框中导航到插件所在的文件夹，点击选择
5. 安装完成后，重启软件，在菜单栏**插件**的子菜单中可以找到安装的插件（和具体插件的功能有关系，一般都在这里）

## 插件开发

开发具有GUI界面的插件，原理是用户自己使用PySide开发一个Widget，然后将这个Widget放入一个QDockWidget，再将QDockWidget嵌入到FiberArt的QMainWindow中。

在python脚本中，用户可以通过FiberArt Python SDK 接口来调用FiberArt的相关功能，比如创建节点、获取选择的节点、调用节点的方法、属性等。

## 自定义插件示例

参考[这个简单的插件例子](./Demo/__init__.py)

```py title="Demo/__init__.py" linenums="1"
--8<-- "docs/advanced/Demo/__init__.py:10:-1"
```

`Demo`相当于一个普通的Python模块，在FiberArt软件启动过程中，会执行 `import Demo` 语句。
