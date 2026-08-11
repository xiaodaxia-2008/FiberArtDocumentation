# Current Workflow

This page describes the FiberArt 0.22.0 interface and workflow. The main process is to prepare geometry and equipment, create or plan plies, inspect the result, configure the motion system, simulate, and export a machine program.

## 1. Create a Project and Import Models

1. Use **File > Open** to open a project or file. In the open-file dialog, choose a file-type filter such as **CADPart**, **CADAssembly**, **CADOneShape**, **SurfaceMesh**, **Model**, **Scene**, or **Node**; you can also choose **All** and let FiberArt select the factory from the file extension. Use **Save** or **Save As** to save the project. You can also start from the blank scene shown at startup and add nodes.
2. Open STEP/IGES, mesh, scene-node, and other plugin-supported data through **File > Open**. Open **File > Import > Component Library** to load equipment components: filter by **Type** (robot, track, positioner, etc.) and **Brand**, search by **Name**, or click **Update** to fetch the latest component catalog from the cloud; the table shows the component model, brand, payload, reach, and installation status. Double-click a row or click **Open** to load the selected component.
3. When opening equipment models (robot, tool, track, positioner), FiberArt preserves the model's original pose and tries to attach it automatically: robots are attached under an existing track and tools under an existing robot. The attachment order does not affect the final assembly result.
4. Select a node in the scene tree and double-click it to open the property editor. Right-click a node to see its available actions.
5. For CAD surfaces used in placement calculations, verify units, orientation, and tessellation settings. Convert a surface to a mesh when required by the operation.

To create a coordinate frame, choose **Model > Frame** to add a default frame node directly, without an extra confirmation dialog.

Projects save the complete scene. Individual nodes can be exported for reuse in another project.

## 2. Plan a Ply

Open **PlyPlanner** from **Functions**. Its main inputs are the layup surface, placement-area boundaries, optional guide curves, a reference point, a seam, and the ply/laminate nodes.

The available planning methods are `FixedAngle`, `Natural`, `Parallel`, `Slicing`, `FixedAngle_Parallel`, and `Natural_Parallel`. The `Variable` option makes the layup angle vary along the reference curve; enable it and enter a variable-angle function.

Typical steps:

1. Select or create a laminate and ply.
2. Set the layup surface, reference point, boundaries, guide curves, and seam.
3. Choose a planning method and layup angle, enabling variable angle when needed.
4. Click **New Planner** to initialize the planner.
5. Use the right/left compute buttons to generate courses, or use the step buttons to inspect one course at a time.
6. Check reference curves, courses, tows, and errors in the scene tree, 3D view, and Log panel.
7. Use **Modify Ply Params** to change parameters and recompute.

For axisymmetric bodies of revolution such as pressure vessels, the **Functions > Filament Winding** panel provides an alternative winding workflow. See [Filament Winding](winding.en.md).

Boundaries must be closed curves or closed topological boundaries. Guide curves can override the initial reference curve. After planning, use the ply property editor for coverage, steering-radius, placement-angle, and point queries.

## 3. Inspect and Edit Plies

Ply nodes control display for the complete set of tows, including centerlines, boundaries, and Tow meshes. Tow nodes can be edited individually and can partition an area using the centerline, left boundary, or right boundary.

After manual edits, check for short, broken, or overlapping tows, valid steering radii, placement-angle errors, course boundaries, and the gap between adjacent courses.

## 4. Configure the Motion System

Prepare the robot, tool, track, positioner, and workpiece in the scene. Verify parent-child transforms, base frames, flange frames, TCP, and collision geometry. The 0.21.x releases provide URDF generator panels for positioners, tracks, and tools, as well as general model and URDF export.

Use **Workpiece Pose Calibration** for workpiece registration and **TCP Calibration** for tool-center-point calibration. See [Poses and Calibration](../advanced/pose_calibration.en.md) for pose formats, clipboard transfer, and calibration results.

## 5. Simulate and Export

Open **LayupSimulation & PostProcess** from **Functions**:

1. Select the track, robot, positioner, and tool.
2. Add trajectory nodes or use **Auto Select** to select them from the scene tree.
3. Choose a kinematic algorithm and track/positioner strategies, then click **Apply**. Use **Apply to All** to apply settings to all selected trajectories.
4. Set the simulation speed and use **start**, **pause**, **continue**, and **stop**.
5. Select a post-processing script, export path, reference node, and whether to export each ply separately.
6. Click **Export** and validate the program in the target controller or offline simulator.

Exported waypoints include trajectory-boundary markers. Post-processing templates can use them to distinguish courses or path segments. See [Post-processing Customization](../advanced/post_process.en.md) for template details.

## 6. Equipment and Geometry Checks

- **Collision Detect** checks interference between robots, tools, workpieces, and equipment.
- **Convex Decomposition** generates convex parts for supported models to improve collision or physics calculations.
- **Positioner/Track/Tool URDF Generator** creates reusable equipment nodes from visual and collision geometry.
- **Measure** measures geometry in the 3D view.

When an operation fails, inspect the **Log** panel first and verify node types, units, frames, and geometry inputs.

## Related Pages

- [Quick Start](getting_started.en.md)
- [Ply Planner](ply_planner.en.md)
- [Filament Winding](winding.en.md)
- [Ply Planning Parameters](plan_parameters.en.md)
- [Simulation](simulation.en.md)
- [Poses and Calibration](../advanced/pose_calibration.en.md)
- [Post-processing Customization](../advanced/post_process.en.md)
