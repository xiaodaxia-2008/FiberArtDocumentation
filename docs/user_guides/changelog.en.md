## v0.18.7 (2026.7.8)
- Fixed robot import issues
- Enhanced trajectory generation functionality

## v0.18.6 (2026.7.7)
- The collision detection panel can now be shown or hidden from the Function menu, keeping the interface clearer and common actions easier to reach.
- Collision checks can now be created for two selected nodes, making detection targets more explicit and reducing interference from unrelated objects.
- Collision model display can be toggled from the context menu, and the action also works after loading older scene files.
- Fixed status bar message colors affecting the unit widget, making the interface display more consistently.
- All users are encouraged to update for more reliable collision detection and display behavior.

## v0.18.5 [6a972c5f] (2026.7.3)
- Added trajectory generation panel
- Added dynamic motion trail display
- Fixed other bugs

## v0.18.4 [48493b7d] (2026.6.27)
- Fixed node name conflicts during import
- Fixed incomplete display issues when importing certain CAD models

## v0.18.3 [d0ecfd0] (2026.6.26)
- Fixed issue where imported plies were not visible, ensuring results are immediately displayed
- Improved normal calculation accuracy, enhancing rendering and display quality
- Fixed other known issues to improve overall software stability
- All users are strongly encouraged to update to this version

## v0.18.2 [688e022] (2026.6.23)
- Added variable-angle path planning mode — paths automatically adjust angles based on surface shape for complex trajectory requirements
- Expanded robot type support for broader production line compatibility
- Fixed incomplete scene file loading after save for improved data reliability
- Fixed plugin loading compatibility issues to prevent crashes due to interface changes
- All users are strongly encouraged to update for a more stable experience

## v0.18.1 [641ea82d] (2026.6.17)
- Software updates now support one-click download and installation — upgrade packages can be fetched directly when a new version is detected
- Download progress is shown in real-time for clear status tracking
- Fixed license verification logic to ensure only matching versions work properly, preventing version mismatch issues
- All users are strongly encouraged to update

## v0.18.0 [7a05dbd2] (2026.6.17)
- Improved scene file save and load for better compatibility and stability
- Optimized installer generation and distribution for more reliable installation experience
- Updated user documentation and welcome page for simpler upgrade and file management guidance
- Fixed several known issues and performance optimizations

## v0.17.2 [5865733c] (2026.6.10)
- Added startup welcome dialog and usage instructions
- Updated KUKA Remote Controller user guide (Feishu doc)
- Fixed KRLFS.jinja post-processor compatibility and code clarity
- Fixed missing header includes after PCH toggle
- Updated package.ps1: Sentinel packaging enabled by default
- Documentation migration: user guide moved to Feishu doc, added help link

## v0.17.1 [c942c6df] (2026.6.9)
- Updated AGENTS.md

## v0.17.0 [90ce145c] (2026.6.9)
- Refactored ZIP serialization: CBOR archive fully replaces Binary; ZIP extension changed to .afscenez/.afnodez
- Refactored serialization: removed macros, unified make_nvp, dropped m_ prefix
- Refactored Node save/load: moved to .cpp with explicit instantiation
- Refactored ZipManager: v4 PIMPL, memory cache replaces lazy file reading
- Performance optimization: unified unsigned char, removed temporary performance monitoring code
- Added URDF collision detection mesh and .cpp serialization support
- Added pose calibration functions and pytest tests
- Updated post-processor Jinja2 templates
- Refactored lead-in/lead-out distances as independent odd/even channel configuration

## v0.16.5 [68c98453] (2026.6.5)
- Added FiberPly core logic and UI components
- Added warning suppression tool and path post-processing logic
- Refactored ZipManager (PIMPL, std::filesystem::path, serialization benchmarks)
- Added GeometryModel and SceneGraph infrastructure (mesh processing, serialization tools)
- Added trajectory export plugin (Jinja2 template support)
- Added KRL post-processor templates
- Added cereal CBOR archive support and serialization benchmarks
- Added hierarchical nested JSON serialization specification

## v0.16.4 [1cd35912] (2026.6.2)
- Fixed known bugs

## v0.16.3 [41e95ad9] (2026.6.1)
- Added component library and cloud robot library
- Added collision detection functionality
- Added expression calculation module
- KUKA Remote Controller support for file management
- Improved simulation and interaction controls

## v0.16.2 [7b53927a] (2026.5.20)
- Fixed rotation ambiguity in path interpolation

## v0.16.1 [463cfbce] (2026.5.19)
- Added documentation

## v0.16.0 [7f08a82a] (2026.5.19)
- Optimized robot remote control plugin: temporarily pauses high-frequency position sync during file download/upload
- Introduced delayed dialog mechanism to avoid nested event loops causing socket state re-entry and channel blocking

## v0.15.15 [663b140d] (2026.5.18)
- Added KUKA robot remote control plugin (RemoteController)
- Implemented asynchronous non-blocking VarProxy communication mechanism
- Added remote file management functionality

## v0.15.10 [3da449a9] (2026.3.26)
- Deprecated some construction warnings to clean up build output

## v0.15.2 [1d23c088] (2026.5.14)
- Refactored logging system: unified FA_LOG_DEBUG to SPDLOG_DEBUG, each module maintains modular logging by redefining SPDLOG_DEBUG

## v0.15.1 [853dc105] (2025.11.14)
- Improved path post-processing
- When using slope restart, the ramp end point can now be defined outside the boundary instead of exactly on it

## v0.15.0 [0519becf] (2025.11.11)
- Added variable-angle function definition
- Added translation system
- Improved serialization functionality, now implementable in .cpp files
- Added Trajectory module (incomplete)
- Added filament winding module with basic UI

## v0.14.6 [45d5cbce] (2025.9.5)
- Improved post-processing handling of positioner angle cycles
- Optimized layup simulation

## v0.14.5 [56d9577c] (2025.9.3)
- Improved 3D display interface
- Improved parameter editing interface
- Modified highlight display method
- Optimized IK calculation for connection paths

## v0.14.4 [b7573e0a] (2025.9.1)
- Added disk axisymmetric planner

## v0.14.3 [34882e6d] (2025.8.29)
- Fixed selection errors
- Improved post-processor

## v0.14.2 [ecd800ee] (2025.8.28)
- Improved mesh generation algorithm
- Improved interface

## v0.14.1 [12e7e616] (2025.8.26)
- Improved planning algorithm applicability
- Fixed other known bugs

## v0.14.0 [3b453670] (2025.8.14)
- Optimized 3D display performance
- Fixed other bugs

## v0.13.9 [69fbe676] (2025.6.26)
- Fixed bidirectional layup connection strategy issue

## v0.13.9 [69fbe676] (2025.6.26)
- Added import/export of plies in JSON format, allowing users to import their own pre-calculated plies

## v0.13.8 [e96f4244] (2025.6.20)
- Fixed straight-line connection strategy issue

## v0.13.7 [e430e1c0] (2025.6.19)
- Fixed an issue where post-processing calculation failure caused crashes.

## v0.13.5 [8bf582cd] (2025.6.4)
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

## v0.9.3 [734d42fc] (2024.5.28)
- Improved layup simulation and post-processing
- Added custom mesh parameterization (cylindrical projection, ARAP, seam parameterization, etc.)
- Added robot drag interaction (base/flange/TCP/tool tip)
- Added scene graph drag-and-drop for node hierarchy adjustment
- Added post-processing UI and NC script parsing
- Optimized kinematics solver, added positioner factory and track parameters
- Fixed scene serialization and node destruction issues

## v0.9.2 (2024.4.19)
- Added curve generation on mesh.
- Fixed geodesic calculation failure in release mode.
- Integrated new documentation.
- Improved node name conflicts.

## v0.9.1 (2024.4.18)
- Added heatmap display for steering radius and placement angle error.
- Added software incremental update functionality.

## v0.9.0 [fc8da80e] (2024.4.12)
- Added natural path planner (Natural Parallel)
- Added reference path planner (RefPath Planner)
- Added KUKA CNC export
- Added steering radius heatmap visualization
- Improved geodesic tracing algorithm
- Optimized dense layup point support
- Refactored path planner core code

## v0.8.0 (2024.4.12)
- Added natural curve planner.
- Added natural curve/parallel offset planner.
- Added display of maximum deviation angle.

## v0.8.0 (2024.4.8)
- Added SteeringRadius calculation.
- Modified so that each Ply has its own parameter set.
- Redesigned the planning interface.
- Improved planner architecture, supporting combined algorithms.

## v0.7.0 [0d517c0c] (2024.3.23)
- Added adaptive path planning method
- Added steering radius calculation and testing
- Added Netgen mesh repair and optimization
- Introduced color system, improved highlight display
- Added path interface and CRTP refactoring
- Added Python plugin node property editor
- Improved layup simulation coverage performance monitoring

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

## v0.6.6 [d31d5810] (2024.2.7)
- Added guide curve (Guide Curve) planning algorithm
- Added English UI support
- Improved layup planner with parallel fixed-angle reference path computation
- Added surface Delaunay remeshing
- Improved post-processor
- Added KR480R3330MT robot model
- Fixed multiple serialization and UI issues

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

## v0.6.0 [6981729f] (2024.1.25)
- Implemented planning based on placement surface and placement area boundaries
- Implemented curve-on-surface intersection calculation in parameter space
- Implemented determining whether a point on a surface is within the placement area
- Improved boundary coverage during planning
- Refactored STEP/IGES import
- Added isotropic remeshing (automatic on CAD import)
- Used FlyWeight pattern to encapsulate Path and Mesh, reducing memory usage
- Supported using Python to extend Node attribute editors
- Moved unused code like OffsetDirectionalSegment to the Deprecated folder
- Added Sentinel encryption packaging support

## v0.5.5 [788865a5] (2023.12.22)
- Fixed merging issues of export path speed change points and tool entry points.

## v0.5.4 [cf9b90c9] (2023.12.22)
- Supported changing speed during the placement phase (after pressing, before cutting) in export paths.
- Added acceleration/deceleration point labels
- Added installation data and example surface meshes
- Added translation system support (QM files)
- Refactored cmake deployment scripts

## v0.5.3 [9928da81] (2023.12.17)
- Added support for compiling with Qt 5.15 and Python 3.8, enabling execution on Windows 7 systems; currently only supports 64-bit operating systems.
- Added packaging system dependencies.
  
## v0.5.2 [65e608f3] (2023.12.14)
- Added variable-angle reference trajectory generation algorithm.
- Refactored extension line calculation algorithm for PathOnMesh.
- Added splash screen.
- Refactored geodesic calculation code.
- Refactored orthogonal curve calculation algorithm using plane intersection.
- Improved post-processing projection onto centerline calculation.
- Added a plugin for measuring the distance between selected points.
- Added a plugin for measuring the mesh bounding box.
- Added a planning angle calculation plugin for 90-degree continuous placement on cylinders.

## v0.5.1 [2414a9c0] (2023.12.11)
- Initialized the v0.5 series
- Introduced refactored algorithm library and plugin framework
- Basic path planning and post-processing support

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

## v0.2.4 [d5d1e2f] (2023.7.22)
- Refactored dependencies, updated Qt 6.5.2 LTS
- Added Doxygen documentation support
- Removed submodules, introduced Quarter as internal module
- Moved pybind11 submodule to ThirdParty
- Added PluginManager
- Added open/save status report
- Fixed save ply parameters
- Refactored post-processor and ply parameter initialization

## v0.2.3 [629e60e] (2023.7.20)
- Added Python plugin framework
- Added IsoContour path planning functionality
- Added immediate parameter application
- Added geodesic contour example
- Added FastMarching example
- Fixed section line functionality
- Refactored connection path and plane-mesh intersection

## v0.2.2 [838afd4] (2023.6.15)
- Added MeshPropertyWidget and PathOnMeshPropertyWidget
- Added shortest path calculation
- Improved TangentGeodesic calculation
- Added extraction of Mesh boundaries
- Added Mesh trimming
- Added Mesh smoothing

## v0.2.1 (2023.5.5~5.29)
- Refactored FiberPathPlanner to improve asynchronous calculation and interactive display, avoiding UI lag.
- Fixed Polyline intersection algorithm.
- Added overlap control when planning conical parts with fixed angles (not yet perfect).
- Added processing operations like surface centering and scaling options.

## v0.2.0 [2922279] (2023.5.6)
- Updated XScript to use ChaiScript as embedded script, no longer dependent on Python
- Improved accuracy for curve offset calculations
- Use native file dialogs for better UX

## v0.1.9 [c0aaaa4] (2023.4.24)
- Fixed various bugs in AFPLY export

## v0.1.8 [5708b86] (2023.4.14)
- Added 3D camera node for Capture simulation FOV display
- Improved XScript
- Added pick-and-place simulation example with 3D vision

## v0.1.7 [41a5714] (2023.4.6)
- Fixed issue where simulation did not correctly set the ply reference path

## v0.1.6 [39a4fd3] (2023.4.4)
- Optimized XScript
- Fixed node destruction issues after selection and deletion
- Added copy/paste for position/orientation and joint angles
- Optimized internal robot control implementation
- Optimized internal layup simulation control
- Added continuous linear interpolation path in arbitrary space

## v0.1.5 [03d8493] (2023.3.16)
- Improved post-processing module for generating G-code from FiberPly
- Modified PlyParameter to use custom configuration UI, no longer a simple JSON editor
- No longer support saving scenes in text format, only binary mode
- Added XScriptNode for defining motion and gripping operations via scripts

## v0.1.4 [3d961ef] (2023.3.6)
- Fixed PlyPlannerWidget not displaying
- Fixed Node destruction issue

## v0.1.2 [e0d4653] (2023.2.25)
- Implemented layup process simulation
- Implemented 6+1 kinematics
- Implemented analytical and numerical robot kinematics algorithms
- Resolved resource destruction issues
- Replaced threads with coroutines for increased stability

## v0.0.7 [cf59606] (2022.9.29)
- Added Sentinel encryption support
- Added display and export of post-processing paths (.afply format)
- Added Windows 10/11 x64 platform support
- Added QtIFW packaging support

## v0.0.6 [5259985] (2022.8.26)
- Fixed a large number of bugs
- Added geodesic-based curve offset on Mesh
- Added fixed-angle path planning method

## v0.0.4 [16fd310] (2022.5.23)
- Fixed many bugs in SceneManager

## v0.0.2 [0309260] (2022.4.13)
- Switched to Coin3D as the 3D display engine
- Implemented parallel plane cutting and curve-on-surface offset algorithms
- Used OpenMP for computation acceleration

## v0.0.1 [8b22442d] (2022.1.22)
- Project initialized, first creation

## Previous untracked version

- Improved logger, renamed global `LOG_DEBUG` etc. to `FA_LOG_DEBUG` (2022.12.5).

