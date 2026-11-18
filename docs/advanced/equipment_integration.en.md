# Equipment and controller integration

This page covers equipment workflows available in v0.25.0. Course rotation and positioner Lua control are separately marked as develop additions.

## Equipment model editing

The unified tree-based URDF editor handles robots, tracks, positioners and tools. Import an existing URDF, edit joint origins, axes, current values, limits and link geometry, then apply/reload. The model-level base pose defines installation. Choose OPW or the appropriate gantry axis-count solver for the actual robot, then verify axis directions and TCP. The OPW diagram helps inspect dimensions and directions.

Visual and collision geometry are configured separately; mesh export can be enabled separately for each. Supply collision geometry where collision checking is required.

## Machine configuration export

Right-click a simulation group and choose **Export Configuration** to write a `.zmachine` package containing kinematics, installations and frames. Export is lightweight by default and excludes meshes. A robot below a track uses the track flange as its installation parent; user frames below a track or positioner retain moving-parent relationships. Do not bake the current external-axis value into the installation again.

Check axis addresses, limits, base/TCP and frame tables in the receiving controller configuration tool. Exporting a file does not send it to a controller.

## CNC digital twin

Open the CNC digital twin panel, select an idle simulation group and enter a controller `ws://` or `wss://` address. After connecting and receiving axis metadata, map remote axes to local joints, verify units/calibration and start synchronization. Settings belong to the simulation group and persist when the scene is saved.

Duplicate source mappings and incompatible units/calibration are rejected. Disconnection, telemetry older than one second, changed remote axes or a document switch stops synchronization and retains the last valid model position. This mirrors feedback into the model; it does not issue motion commands.

## Postprocessing integration

Jinja and Python postprocessors include Inovance scanner-camera and Nabote robot outputs. The local postprocessor MCP service allows external tools to reuse the panel's export context, including its simulation group, trajectories, reference node and output path. These inputs must still be configured. See [Postprocessing](post_process.md).
