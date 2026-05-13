# FiberArt Plugin Development Tutorial

## Plugin Installation

1. Open FiberArt.
2. Select **Plugin** from the menu bar, then click **Plugin Management**.
3. In the popup interface, click **Install Plugin**.
4. In the file selection dialog, navigate to the folder where the plugin is located and click to select.
5. After the installation is complete, restart the software. The installed plugin can be found in the submenu of **Plugin** in the menu bar (depending on the specific plugin's function, they are generally located here).

## Plugin Development

To develop a plugin with a GUI, the principle is that the user develops a Widget using PySide themselves, then places this Widget into a QDockWidget, and then embeds the QDockWidget into FiberArt's QMainWindow.

In the Python script, users can use the FiberArt Python SDK interface to call relevant FiberArt functions, such as creating nodes, getting selected nodes, calling node methods, attributes, etc.

## Custom Plugin Example

Refer to [this simple plugin example](./Demo/__init__.py).

```py title="Demo/__init__.py" linenums="1"
--8<-- "docs/advanced/Demo/__init__.py:10:-1"
```

`Demo` acts as a regular Python module. During the startup of the FiberArt software, an `import Demo` statement is executed.
