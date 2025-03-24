"""
Copyright © 2024 Zen Shawn. All rights reserved.

@file __init__.py
@author Zen Shawn
@email xiaozisheng2008@hotmail.com
@date 17:16:46, April 18, 2024
"""

import PyFiberArt
from FiberArtDefaultPlugins.utils import (
    QtWidgets,
    add_plugin_widget,
    decorator_factory_selected_node,
)


def create_demo():
    # create the widget
    w = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    w.setLayout(layout)

    label = QtWidgets.QLabel("这是一个示例插件，试试选中一个节点，然后点击按钮")
    layout.addWidget(label)

    btn = QtWidgets.QPushButton("显示选中节点")
    layout.addWidget(btn)

    @decorator_factory_selected_node(PyFiberArt.Node)
    def btn_cb(node: PyFiberArt.Node):
        label.setText(f"你选择了{node.GetName()}")

    btn.clicked.connect(btn_cb)

    add_plugin_widget(w, win_title="自定义插件", visible=True)


create_demo()
