## v0.13.7(2025.6.19)
- 修复后处理计算失败闪退的问题

## v0.13.5(2025.6.4)
- 修复远距离的三维点投影到Mesh上的问题

## v0.13.3(2025.6.4)
- 使用FreeCAD风格的三维球
- 修复“包络面上的投影路径”连接策略的问题
- 可以直接设置TopoShape节点作为包络面
- 新建铺层的名称默认不再取整

## v0.13.2(2025.5.28)
- 增加设置通用的形状作为包络面

## v0.13.1(2025.5.27)
- 使用包络圆柱面上的最短路径构造连接路径

## v0.13.0(2025.5.27)
- 增加投影到圆柱面进行路径连接
- 改进铺层节点设置参数的界面
- 增加圆柱面节点及其编辑器
- 导入的Step模型支持再导出位Step或者Stl

## v0.12.1(2025.5.20)
- 修复最短路径连接的一些问题

## v0.12.0(2025.5.19)
- 增加最短路径连接策略

## v0.11.0(2025.3.18)
- 实现将铺层导出为step/gltf/ply/stl文件

## v0.9.14(2024.12.3)
- 修复修改纵向铺放方向引发的问题

## v0.9.14(2024.12.2)
- 导入模型时识别直线，从而支持直接选择作为参考线段

## v0.9.13(2024.11.23)
- 使用新的ZenLicense，使用网络时间校验授权

## v0.9.13(2024.11.7)
- 使用新的ZenLicense进行权限管理
- 增加批量模式
- 增加布局导入导出

## v0.9.11(2024.9.3)
- 修复bug

## v0.9.9(2024.8.30)
- 增加自定义丝束功能
- 增加丝束重叠消除
- 改进3D交互

## v0.9.8(2024.8.27)
- 增加斜坡重送功能

## v0.9.7(2024.8.23)
- 修复点到曲线的投影错误
- 改进mesh参数化
- 增加Curve、Surface等基类

## v0.9.6(2024.7.9)
- 优化仿真执行过程
- 增加引导路径
- 优化参数设置

## v0.9.5(2024.6.14)
- 实现基于优化的多轴联动求解器

## v0.9.4(2024.6.10)
- 实现压辊变形量分析

## v0.9.3(2024.5.28)
- 实现仿真模块
- 实现导出KUKA CNC程序

## v0.9.2(2024.4.19)
- 增加在mesh上生成曲线
- 修复release模式下计算测地线失败问题
- 集成新的文档
- 改进节点名称冲突

## v0.9.1(2024.4.18)
- 增加热力图显示转向半径、铺放角度误差
- 增加软件增量更新功能

## v0.8.0(2024.4.12)
- 增加自然曲线规划器
- 增加自然曲线/平行偏移规划器
- 增加显示最大偏离角度

## v0.8.0(2024.4.8)
- 增加计算SteeringRadius
- 修改为每个Ply拥有自己的参数集合
- 规划界面改版
- 规划器架构改进，支持组合算法

## v0.7.0(2024.3.23)
- 新增划分网格算法，
- 新增缝合形状
- 修复序列化问题

## v0.6.9(2024.3.15)
- 修复PathOnMesh获取Pose时误差大的问题
- 新增空行程路径平滑功能
- 对参数名称进行了整理改进
- 增加了一些TestCase

## v0.6.8(2024.3.12)
- 后处理回程路径使用SE3空间插值，避免旋转速度太大

## v0.6.7(2024.3.8)
- 修复轨迹后处理乱序问题
- 大多数节点属性编辑以插件形式实现
- 增加构造PathOnMesh到Mesh的距离误差控制
- 改进Tow的显示

## v0.6.6(2024.2.7)
- 参数设置支持多语言
- 改进自动选择参考节点

## v0.6.5(2024.2.6)
- 重塑整体操作流程
- 增加预估覆盖率的功能

## v0.6.4(2024.2.5)
- 改进后处理模块
- 改进导入step/iges的处理流程

## v0.6.2(2024.1.31)
- 改进授权检测
- 增加并行计算固定角度的参考路径
- 增加KR480R3330MT机器人模型
- 实现模型厚度增加
- 修复析构bug
- 修复节点属性编辑器UI重复问题

## v0.6.0(2024.1.24)
- 实现基于铺放曲面及铺放区域的边界来进行规划
- 实现曲面曲线在参数空间进行相交计算
- 实现判断曲面上一点是否在铺放区域内
- 提高规划时边界区域的覆盖率
- 增加Mesh处理算法
- 使用FlyWeight封装Path和Mesh
- 支持使用python扩展Node的属性编辑器
- 移动不用的OffsetDirectionalSegment等相关代码到Deprecated文件夹
- 改进IGES、STEP格式的导入

## v0.5.5(2023.12.22)
- 修改了一下导出路径速度改变点和进刀点的合并问题

## v0.5.4(2023.12.22)
- 导出路径支持改变铺放阶段（压紧以后，剪切之前）的速度

## v0.5.3(2023.12.17)
- 增加支持编译Qt5.15和python 3.8，从而支持在windows 7系统上运行；目前仅支持64位操作系统
- 增加打包系统依赖
  
## v0.5.2(2023.12.14)
- 增加变角度参考轨迹生成算法
- 重构PathOnMesh计算延长线算法
- 增加splashscreen
- 重构计算测地线的代码
- 重构平面相交计算正交曲线算法
- 改进后处理投影到中心线的计算
- 增加测量选择的点的距离的插件
- 增加测量mesh包围盒的插件
- 增加计算圆柱90度连续铺放时规划角度计算插件


## v0.3~v0.5.1 (2023.12.11)
- 改进空间曲线交点求解算法
- 改进铺层重叠检测及控制方式
- 增加铺放面积及长度统计
- 后置处理放到python插件中实现
- 集成ZenLicense
- 集成Sentinel SDK 
- TowMesh remeshing，避免显示量过大卡顿问题
- 增加TowSegment，为规划开孔类等模型奠定基础
- PathOnMesh
    - 优化PathOnMesh，弱化FaceLocation的作用，侧重使用密集采样的数值方法
    - 优化PathOnMesh的偏移功能，增加每次最大偏移量；超过的话使用迭代中继偏移
    - 点投影到曲线
    - 增加计算参数空间曲线
- 规划参数优化层级结构，分离出高级参数
- 可以对同一铺层使用不同的规划算法接力规划
- 可以导入没有规划完成的铺层继续规划
- 基本完成了FiberArt核心类的python binding
- 增加了基于json-schema的灵活参数编辑器
- 支持编译为动态库
- 集成了OCC，可以导入step，iges模型

## v0.2.4 (2023.7.20~2023.7.22)
- 升级Qt到6.5.2LTS
- 改进README，依赖安装方式
- 删除了大量未用的代码

## v0.2.3 (2023.6.15~2023.7.20)
- 增加了python插件功能
- 修复导出路径bug

## v0.2.2 (2023.5.29~6.15)
- 增加了MeshPropertyWidget和PathOnMeshPropertyWidget
- 增加计算最短路径
- 改进TangentGeodesic计算
- 增加提取Mesh边界
- 增加裁剪Mesh
- 增加平滑Mesh

## v0.2.1 (2023.5.5~5.29)
- 重构FiberPathPlanner, 提升异步计算功能和交互显示，避免UI卡顿
- 修复Polyline求交点算法
- 在固定角度规划圆锥类零件时，增加搭接控制，但是还不完善
- 增加曲面居中、缩放选项等处理操作

## v0.2.0 (2023.4.24~2023.5.5)
- 更新XScript使用ChaiScript作为内嵌脚本，不再使用python
- 提升计算曲线偏移的精度

## v0.1.9 (2023.4.14~2023.4.24)
- 修复导出AFPLY时，对关键点排序错误的问题
- 修复导出格式与PQArt的兼容性问题


## v0.1.8 (2023.4.6~2023.4.14)
- 增加3D相机节点，实现Capture仿真显示FOV
- 改进XScript
- 增加结合3D视觉的抓取仿真例子

## v0.1.7 (2023.4.4~2023.4.6)
- 修复仿真没有正确设置铺层参考路径的问题
- 增加了一些简单几何体的节点，如圆柱体、圆锥体、球体等

## v0.1.6 (2023.3.16~2023.4.4)
- 优化XScript
- 修复选择节点后删除节点析构问题
- 增加复制/粘贴位置姿态和关节角度的功能
- 优化内部对机器人控制的实现
- 优化内部对铺放仿真控制的实现
- 增加了任意空间的连续直线插值路径功能

## v0.1.5 (2023.3.1~2023.3.16)
- 改进从FiberPly生成G代码的后处理模块
- 修改PlyParameter为定制配置的UI，不是简单的json编辑器
- 不再支持保存场景为text格式，只支持二进制模式——简化代码和防止数据泄露
- 增加XScriptNode，支持通过脚本定义运动、抓取等操作 2023.3.15


## Previous untracked version

- 改进logger，将全局的 `LOG_DEBUG` 等改为 `FA_LOG_DEBUG`, 2022.12.5
