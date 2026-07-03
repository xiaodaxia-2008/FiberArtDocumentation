## v0.18.5 (2026.7.3)
- Added trajectory generation panel
- Added dynamic motion trail display
- Fixed other bugs

## v0.13.7 (2025.6.19)
- Fixed an issue where post-processing calculation failure caused crashes.

## v0.13.5 (2025.6.4)
- Fixed an issue with projecting distant 3D points onto the Mesh.

## v0.13.3 (2025.6.4)
- Used FreeCAD-style 3D gizmos.
- Fixed issues with the "Projected Path on Envelope Surface" link strategy.
- Enabled direct setting of TopoShape nodes as envelope surfaces.
- New ply names are no longer rounded by default.

## v0.13.2 (2025.5.28)
- Added the ability to set general shapes as envelope surfaces.

## v0.13.1 (2025.5.27)
- Used the shortest path on the envelope cylindrical surface to construct the connection path.

## v0.13.0 (2025.5.27)
- Added path connection via projection onto a cylindrical surface.
- Improved the interface for setting parameters of ply nodes.
- Added cylindrical surface nodes and their editor.
- Imported STEP models now support re-exporting as STEP or STL.

## v0.12.1 (2025.5.20)
- Fixed some issues with the shortest path connection.

## v0.12.0 (2025.5.19)
- Added shortest path connection strategy.

## v0.11.0 (2025.3.18)
- Implemented exporting plies as STEP/GLTF/PLY/STL files.

## v0.9.14 (2024.12.3)
- Fixed issues caused by modifying the longitudinal layup direction.

## v0.9.14 (2024.12.2)
- Recognizes straight lines when importing models, supporting direct selection as reference line segments.

## v0.9.13 (2024.11.23)
- Used new ZenLicense with network time verification for authorization.

## v0.9.13 (2024.11.7)
- Used new ZenLicense for permission management.
- Added batch mode.
- Added layout import and export.

## v0.9.11 (2024.9.3)
- Fixed bugs.

## v0.9.9 (2024.8.30)
- Added custom tow functionality.
- Added tow overlap elimination.
- Improved 3D interaction.

## v0.9.8 (2024.8.27)
- Added slope restart functionality.

## v0.9.7 (2024.8.23)
- Fixed projection errors from points to curves.
- Improved mesh parameterization.
- Added base classes like Curve and Surface.

## v0.9.6 (2024.7.9)
- Optimized simulation execution process.
- Added guide paths.
- Optimized parameter settings.

## v0.9.5 (2024.6.14)
- Implemented optimization-based multi-axis linkage solver.

## v0.9.4 (2024.6.10)
- Implemented roller deformation analysis.

## v0.9.3 (2024.5.28)
- Implemented simulation module.
- Implemented KUKA CNC program export.

## v0.9.2 (2024.4.19)
- Added curve generation on mesh.
- Fixed geodesic calculation failure in release mode.
- Integrated new documentation.
- Improved node name conflicts.

## v0.9.1 (2024.4.18)
- Added heatmap display for steering radius and placement angle error.
- Added software incremental update functionality.

## v0.8.0 (2024.4.12)
- Added natural curve planner.
- Added natural curve/parallel offset planner.
- Added display of maximum deviation angle.

## v0.8.0 (2024.4.8)
- Added SteeringRadius calculation.
- Modified so that each Ply has its own parameter set.
- Redesigned the planning interface.
- Improved planner architecture, supporting combined algorithms.

## v0.7.0 (2024.3.23)
- Added mesh partitioning algorithm.
- Added shape stitching.
- Fixed serialization issues.

## v0.6.9 (2024.3.15)
- Fixed significant errors when getting Pose from PathOnMesh.
- Added idle path smoothing function.
- Cleaned up and improved parameter names.
- Added some TestCases.

## v0.6.8 (2024.3.12)
- Used SE3 spatial interpolation for return paths in post-processing to avoid excessive rotation speed.

## v0.6.7 (2024.3.8)
- Fixed out-of-order issues in trajectory post-processing.
- Most node attribute editing is now implemented as plugins.
- Added distance error control from PathOnMesh to Mesh.
- Improved Tow display.

## v0.6.6 (2024.2.7)
- Supported multi-language for parameter settings.
- Improved automatic selection of reference nodes.

## v0.6.5 (2024.2.6)
- Reshaped the overall operation process.
- Added estimated coverage calculation functionality.

## v0.6.4 (2024.2.5)
- Improved post-processing module.
- Improved the processing workflow for importing STEP/IGES.

## v0.6.2 (2024.1.31)
- Improved authorization detection.
- Added parallel calculation of fixed-angle reference paths.
- Added KR480R3330MT robot model.
- Implemented model thickness increase.
- Fixed destructor bugs.
- Fixed UI duplication issues in node attribute editor.

## v0.6.0 (2024.1.24)
- Implemented planning based on placement surface and placement area boundaries.
- Implemented curve-on-surface intersection calculation in parameter space.
- Implemented determining whether a point on a surface is within the placement area.
- Improved boundary coverage during planning.
- Added mesh processing algorithms.
- Used FlyWeight to encapsulate Path and Mesh.
- Supported using Python to extend Node attribute editors.
- Moved unused code like OffsetDirectionalSegment to the Deprecated folder.
- Improved import of IGES and STEP formats.

## v0.5.5 (2023.12.22)
- Fixed merging issues of export path speed change points and tool entry points.

## v0.5.4 (2023.12.22)
- Supported changing speed during the placement phase (after pressing, before cutting) in export paths.

## v0.5.3 (2023.12.17)
- Added support for compiling with Qt 5.15 and Python 3.8, enabling execution on Windows 7 systems; currently only supports 64-bit operating systems.
- Added packaging system dependencies.
  
## v0.5.2 (2023.12.14)
- Added variable-angle reference trajectory generation algorithm.
- Refactored extension line calculation algorithm for PathOnMesh.
- Added splash screen.
- Refactored geodesic calculation code.
- Refactored orthogonal curve calculation algorithm using plane intersection.
- Improved post-processing projection onto centerline calculation.
- Added a plugin for measuring the distance between selected points.
- Added a plugin for measuring the mesh bounding box.
- Added a planning angle calculation plugin for 90-degree continuous placement on cylinders.


## v0.3~v0.5.1 (2023.12.11)
- Improved spatial curve intersection solving algorithm.
- Improved ply overlap detection and control methods.
- Added placement area and length statistics.
- Implemented post-processing via Python plugins.
- Integrated ZenLicense.
- Integrated Sentinel SDK.
- Implemented TowMesh remeshing to avoid lag issues due to excessive display volume.
- Added TowSegment, laying the foundation for models with cutouts.
- PathOnMesh
    - Optimized PathOnMesh, reducing reliance on FaceLocation in favor of dense sampling numerical methods.
    - Optimized offset function of PathOnMesh, added maximum offset per pass; using iterative intermediate offsets if exceeded.
    - Added point-to-curve projection.
    - Added parameter space curve calculation.
- Optimized hierarchical structure of planning parameters, separating advanced parameters.
- Enabled relay planning using different algorithms for the same ply.
- Enabled continued planning for incomplete ply imports.
- Mostly completed Python bindings for FiberArt core classes.
- Added a flexible parameter editor based on JSON-schema.
- Supported compilation as dynamic libraries.
- Integrated OCC for importing STEP and IGES models.

## v0.2.4 (2023.7.20~2023.7.22)
- Upgraded Qt to 6.5.2 LTS.
- Improved README and dependency installation instructions.
- Removed a large amount of unused code.

## v0.2.3 (2023.6.15~2023.7.20)
- Added Python plugin functionality.
- Fixed export path bugs.

## v0.2.2 (2023.5.29~6.15)
- Added MeshPropertyWidget and PathOnMeshPropertyWidget.
- Added shortest path calculation.
- Improved TangentGeodesic calculation.
- Added extraction of Mesh boundaries.
- Added Mesh trimming.
- Added Mesh smoothing.

## v0.2.1 (2023.5.5~5.29)
- Refactored FiberPathPlanner to improve asynchronous calculation and interactive display, avoiding UI lag.
- Fixed Polyline intersection algorithm.
- Added overlap control when planning conical parts with fixed angles (not yet perfect).
- Added processing operations like surface centering and scaling options.

## v0.2.0 (2023.4.24~2023.5.5)
- Updated XScript to use ChaiScript as an embedded script instead of Python.
- Improved accuracy for curve offset calculations.

## v0.1.9 (2023.4.14~2023.4.24)
- Fixed an error in key point sorting when exporting AFPLY.
- Fixed compatibility issues with the export format and PQArt.


## v0.1.8 (2023.4.6~2023.4.14)
- Added 3D camera node to implement Capture simulation for FOV display.
- Improved XScript.
- Added a pick-and-place simulation example combined with 3D vision.

## v0.1.7 (2023.4.4~2023.4.6)
- Fixed an issue where the ply reference path was not set correctly in simulations.
- Added some simple geometric nodes, such as cylinders, cones, and spheres.

## v0.1.6 (2023.3.16~2023.4.4)
- Optimized XScript.
- Fixed node destruction issues after selection and deletion.
- Added copy/paste functionality for position/orientation and joint angles.
- Optimized internal implementation for robot control.
- Optimized internal implementation for placement simulation control.
- Added continuous linear interpolation path functionality in arbitrary space.

## v0.1.5 (2023.3.1~2023.3.16)
- Improved post-processing module for generating G-code from FiberPly.
- Modified PlyParameter to use a custom configuration UI instead of a simple JSON editor.
- No longer support saving scenes in text format, only binary mode—simplifying code and preventing data leakage.
- Added XScriptNode to support defining operations like motion and gripping via scripts (2023.3.15).


## Previous untracked version

- Improved logger, renamed global `LOG_DEBUG` etc. to `FA_LOG_DEBUG` (2022.12.5).
