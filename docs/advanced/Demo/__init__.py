#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Copyright © 2024 Zen Shawn. All rights reserved.

@file __init__.py
@author Zen Shawn
@email xiaozisheng2008@hotmail.com
@date 17:16:46, April 18, 2024
"""

try:
    from PySide6 import QtWidgets, QtCore
    import shiboken6 as shiboken
except ImportError:
    from PySide2 import QtWidgets
    import shiboken2 as shiboken, QtCore

import PyFiberArt


def create_demo():
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


create_demo()