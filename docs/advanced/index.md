# FiberArt 软件进阶教程

本节说明需要结合设备、坐标系、脚本或后处理模板的功能。建议先完成[当前版本工作流](../user_guides/current_workflow.md)，再按任务阅读：

- [多轴联动系统运动学设置](kinematics.md)：轨道、机器人和位置机的求解策略；
- [位姿与标定](pose_calibration.md)：位姿格式、工件标定和 TCP 标定；
- [后处理定制](post_process.md)：内置 Jinja2 模板和自定义设备程序；
- [插件开发](plugin.md)：Python SDK、Qt 面板和插件安装。

设备程序在实际运行前必须经过坐标系、关节限位、碰撞和 I/O 检查。
