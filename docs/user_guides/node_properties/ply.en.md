# Ply Properties

Find the ply node you want to modify in the scene tree and double-click to open its property panel. The panel contains seven pages: **Parameters and Path**, **Export Ply Shape**, **Coverage Analysis**, **Steering Radius**, **Layup Angle**, **Roller Deformation**, and **Query**.

## Parameters and Path

### Link Path Policy

Selects how the transition path between two adjacent placement paths is generated. Nine strategies are available, see [Path Linking Strategy](../plan_parameters.md#link-path-policy):

- Straight
- StraightJointSpace
- OffsetShortestPathOnLayupSurface
- OffsetProjectedPathOnLayupSurface
- ShortestPathOnEnvelope
- ProjectedPathOnEnvelope
- ReverseCurrentHeadPath
- ReverseNextHeadPath
- ReverseNextHeadPathJointSpaceLink

### Set Envelope

When the linking strategy is set to **ShortestPathOnEnvelope** or **ProjectedPathOnEnvelope**, click `Set Envelope` and pick an envelope node from the scene tree. If the envelope node is modified, you need to set it again.

### Modify More Ply Parameters

Opens the ply's own independent planning parameter editor, see [How to Modify Ply Parameters](../plan_parameters.md#how-to-modify-ply-parameters).

## Export Ply Shape

Click `Export As` to export the ply shape to a file. Supported formats are `gltf(*.gltf)`, `ply(*.ply)`, `stl(*.stl)`, and `Step files (*.step)`.

- Unit: The length unit of the exported file, `M` (meters) or `MM` (millimeters). The unit setting is only meaningful when the export format is step.

## Coverage Analysis

Statistics on the percentage of the placement area covered by the ply, as well as the ply's area, length, etc.

- Sample Points: The number of random sampling points used for statistics within the placement area, range 1000-1000000, step 1000, default 10000.
- Click `Analyze` to output:
    - Layup Percentage: The percentage of the placement area covered by the ply;
    - Area of Surface: The surface area of the placement area;
    - Area of Ply: The total area of all tows in the ply;
    - Length of Ply: The total length of all tows in the ply.

## Steering Radius

Analyzes the steering radius of each prepreg tow, which can be displayed in an "x" (cross) style or as a heatmap.

- Step: The sampling interval along the tow path, default 0.03m.
- Highlight Style:
    - Cross: Marks sample points whose steering radius is below the threshold with an "x";
    - Heat Map: Displays the steering radius on the tow path using heatmap colors.
- Cross Threshold: When the cross style is used, sample points with a steering radius below this value are marked (`< threshold m`);
- Heat Map Lower / Heat Map Upper: Steering radius values mapped to the minimum/maximum heatmap colors;
- Click `Compute` to show the minimum steering radius computed over all tows of the ply in the Min Steering Radius field.

## Layup Angle

Analyzes the error between the placement angle of the prepreg tow and the reference angle, which can be displayed in an "x" style or as a heatmap.

- Step: The sampling interval along the tow path, default 0.03m;
- Highlight Style:
    - Cross: Marks sample points whose angle error exceeds the threshold with an "x";
    - Heat Map: Displays the angle error on the tow path using heatmap colors.
- Cross Threshold: When the cross style is used, sample points with an angle error greater than this value are marked (`> threshold °`), default 5°;
- Heat Map Lower / Heat Map Upper: Angle error values mapped to the minimum/maximum heatmap colors;
- Click `Compute` to show the maximum angle deviation computed over all tows of the ply in the Max Angle Derivation field.

## Roller Deformation

Analyzes the deformation produced when the roller contacts the tow during placement, which can be displayed in an "x" style or as a heatmap.

- Step: The sampling interval along the tow path, default 0.03m;
- Highlight Style:
    - Cross: Marks sample points whose deformation exceeds the threshold with an "x";
    - Heat Map: Displays the deformation on the tow path using heatmap colors.
- Cross Threshold: When the cross style is used, sample points with a deformation greater than this value are marked (`> threshold m`), default 0.005m;
- Heat Map Lower / Heat Map Upper: Deformation values mapped to the minimum/maximum heatmap colors;
- Click `Compute` to show the maximum deformation computed over all tows of the ply in the Max Roller Deformation field.

## Query

Click on the ply with the mouse to query the coordinates of the clicked point, as well as the ply, group, and prepreg tow it belongs to, and information such as steering radius and placement angle.

Usage:

1. Click `Pick Point`, then click a point on the ply in the 3D view. The coordinates are shown in the X, Y, and Z fields.
2. Click `Query` and the query result is displayed in the text box below.

## Display

The display properties of a ply node can be edited in the scene-tree property editor:

- Show Tow Mesh: Controls Tow-mesh display for the whole ply. Disable it to keep only centerlines or boundaries and reduce the display cost of large projects. After reopening a project, check that the visibility state matches the intended inspection view.
- Show Path: Whether to display the placement path.
- Show Direction: Whether to display the movement direction of each point on the path.
- Show Orientation: Whether to display the pose coordinate frame of each point on the path.
- Show Command: Whether to display the commands on the path.
- Show Comment: Whether to display the comments on the path.
- Show Simulation Pose: Whether to display the live pose during simulation.
- Show Simulation Path: Whether to record and display the trajectory during simulation.

A ply node also supports the following actions:

- Modify Parameters: Opens the ply's planning parameter editor.
- Copy: Copies the ply together with all its courses and tows.
- Show Left Boundary / Show Right Boundary: Extracts the left/right boundary of the ply as an independent curve node.
