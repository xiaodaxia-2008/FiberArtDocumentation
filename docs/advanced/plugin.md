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

## 插件例子

参考[这个简单的插件例子](./Demo/__init__.py)

/// settings | Basic CSS Setup

//// collapse-code
```css
/* Critic Markup */
.markdown-body .critic {
  font-family: inherit;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  border-style: solid;
  border-width: 1px;
  padding-top: 0.1em;
  padding-bottom: 0.1em;
  text-decoration: none;
}

.markdown-body .critic:before,
.markdown-body .critic:after {
  content: '\00a0';
  padding-top: 0.1em;
  padding-bottom: 0.1em;
  font-size: initial;
}

.markdown-body .block:before,
.markdown-body .block:after {
  content: '';
}

.markdown-body mark.critic {
  border-color: #ff8600;
  background: #ffddaa;
}

.markdown-body ins.critic {
  border-color: #00bb00;
  background: #ddffdd;
}

.markdown-body del.critic {
  border-color: #dd0000;
  background: #ffdddd;
}

.markdown-body ins.break,
.markdown-body del.break {
  font-size: 0;
  border: none;
}

.markdown-body ins.break:before,
.markdown-body del.break:before {
  content: '\00a0\b6\00a0';
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}

.markdown-body ins.after,
.markdown-body del.after {
  content: '';
}

.markdown-body ins.break:before {
  color: #00bb00;
  border: 1px solid #00bb00;
  background: #ddffdd;
}

.markdown-body del.break:before {
  color: #bb0000;
  border: 1px solid #bb0000;
  background: #ffdddd;
}

.markdown-body span.critic {
  background: #ddddff;
  border: 0;
  border-top: 1px solid #0000bb;
  border-bottom: 1px solid #0000bb;
}

.markdown-body span.critic:before,
.markdown-body span.critic:after {
  font-size: inherit;
  background: #ddddff;
  border: 1px solid #0000bb;
}

.markdown-body span.critic:before {
  content: '\00a0\bb';
  border-right: none;
  -webkit-border-top-left-radius: 3px;
  -moz-border-top-left-radius: 3px;
  border-top-left-radius: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -moz-border-bottom-left-radius: 3px;
  border-bottom-left-radius: 3px;
}

.markdown-body span.critic:after {
  content: '\ab\00a0';
  border-left: none;
  -webkit-border-top-right-radius: 3px;
  -moz-border-top-right-radius: 3px;
  border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 3px;
  -moz-border-bottom-right-radius: 3px;
  border-bottom-right-radius: 3px;
}

.markdown-body .block {
  display: block;
  padding: .02em;
}
```
////
///

```python
# filename: Demo/__init__.py

from PySide6 import QtWidgets, QtCore
import shiboken6 as shiboken
import PyFiberArt


translate = QtCore.QCoreApplication.translate
"""Create a demo plugin."""
win: QtWidgets.QMainWindow = shiboken.wrapInstance(
    PyFiberArt.GetMainWindow().Ptr(), QtWidgets.QMainWindow
)

# create a simple widget
w = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()
w.setLayout(layout)

label = QtWidgets.QLabel(translate("DemoPlugin", "This is a demo plugin."))
layout.addWidget(label)

btn = QtWidgets.QPushButton(translate("DemoPlugin", "Click Me!"))
layout.addWidget(btn)

def btn_cb():
    label.setText(translate("DemoPlugin", f"You clicked me!"))

btn.clicked.connect(btn_cb)


# add it to FiberArt mainwindow
dw = QtWidgets.QDockWidget(translate("DemoPlugin", "Demo Plugin"), win)
dw.setWidget(w)
win.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw)
dw.setVisible(False)
dw.setObjectName("_Demo_")

# add toggle view action
menu: QtWidgets.QMenu = win.findChild(QtWidgets.QMenu, "menuPlugins")
if menu:
    menu.addAction(dw.toggleViewAction())
```

`Demo`相当于一个普通的Python模块，在FiberArt软件启动过程中，会执行 `import Demo` 语句。
