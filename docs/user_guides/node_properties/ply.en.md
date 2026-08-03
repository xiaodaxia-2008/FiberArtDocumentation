# Ply Properties

## Basic

### Modify Ply Parameters

### Show Placement Path

### Show Tow Mesh

Use **Show Tow Mesh** to control Tow-mesh display for the whole ply. Disable it to keep only centerlines or boundaries and reduce the display cost of large projects. After reopening a project, check that the visibility state matches the intended inspection view.

## Coverage Analysis

Statistics on the percentage of the placement area covered by the ply, as well as the ply's area, length, etc.

## Steering Radius

Analyzes the steering radius of each prepreg tow, which can be displayed in an "x" style or as a heatmap.

## Placement Angle

Analyzes the error between the placement angle of the prepreg tow and the reference angle, which can be displayed in an "x" style or as a heatmap.

## Click-to-Select Query

Click on the ply with the mouse to query the coordinates of the clicked point, as well as the ply, group, and prepreg tow it belongs to, and information such as steering radius and placement angle.

Usage:

1. Click a point on the ply with the mouse;
2. Click `Pick Point`;
3. Click `Query Point`;

## Trajectory Segments and Export

A planned ply contains multiple courses and trajectory segments. During simulation export, segment starts and ends are marked so post-processors can preserve course boundaries. After changing parameters, visibility, or individual tows, rerun coverage, steering-radius, and placement-angle analyses.
