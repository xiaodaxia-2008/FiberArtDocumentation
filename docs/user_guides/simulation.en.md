# Simulation

From **Functions** on the main menu bar, select **LayupSimulation & PostProcess** to open the simulation and post-processing panel.

## Settings

- Track: Set the robot linear track of the motion system.
- Robot: Set the robot of the motion system.
- Positioner: Set the positioner of the motion system.
- Tool: Set the placement head or tool used by the motion system.
- Ply Group: Set the ply group to be simulated.
- Ply: Select the current ply; some operations target a single ply rather than the entire ply group.
- Trajectory Nodes: Add or remove trajectory nodes to simulate.
- Auto-select: Automatically select the track, robot, positioner, and ply group from the scene tree.
  
## Simulation

Used to control simulation start, pause, resume, and stop, as well as to set the simulation speed.
You can choose to simulate a single ply or the entire ply group at once.

## Post-process

Used to select post-processing scripts, output NC programs, etc.

- Post-processor: Select a system-preset post-processor, install one, or choose a post-processor you wrote yourself. Post-processor names must be unique.
- Export Path: Set the export path for the programs.
- Reference Node: Set the coordinate reference frame in the program, usually world coordinates, the workpiece, or the tool center of the positioner.
- Export Each Ply Individually: If checked, each ply is exported as an individual file; otherwise, the entire ply group is exported as one file.
- Reference nodes can be reset to world coordinates or set to a selected scene node. Recheck exported coordinates after changing the reference node.

## Kinematics Settings

Set the algorithm used to calculate the inverse kinematics of the motion system:
- Optimized Linkage: Builds an optimization model to automatically calculate the inverse kinematics for the track, robot, and positioner at each point.
- Rule-based Linkage: Calculates the positions of the track and positioner based on given rules, and then determines the robot's joint positions.

For more detailed information on this section, see [Multi-axis Linkage System Kinematics Settings](../advanced/kinematics.en.md). Click **Apply** after changing the settings, or **Apply to All** to apply them to all selected trajectories.
  
## Positioner

Under the rule-based linkage algorithm, this is used to set the strategy for calculating the positioner's position.

- Strategy: The strategy for calculating the positioner's position:
    - Align: Rotates the positioner so that the trajectory point's orientation aligns with the reference direction.
    - Align-Linear Interpolation: Uses the alignment strategy to solve the positioner position only at the start and end points of a set of placement trajectories, with linear interpolation for intermediate points.
    - Align-Cubic Interpolation: Uses the alignment strategy to solve the positioner position only at the start and end points of a set of placement trajectories, with cubic polynomial interpolation for intermediate points.
    - Fixed: The positioner is fixed at a given position.
    - Auto-Fixed: Automatically calculates a suitable fixed position for the positioner within a set of placement trajectories; linear interpolation is used between adjacent sets.
- Fixed Position: The fixed joint position of the positioner when using the Fixed strategy.
- Start Direction: The reference direction at the start of a set of placement trajectories, usually rotating the Z-direction along the positioner's rotation axis by the given angle. Linear interpolation is used for the reference direction between the start and end points.
- End Direction: The reference direction at the end of a set of placement trajectories, usually rotating the Z-direction along the positioner's rotation axis by the given angle.
- Normal Weight: Defines how the orientation is calculated when aligning the trajectory point's orientation with the reference direction. It is a weighted calculation using the point's normal and the radial direction from the rotation axis to the point (similar to bicycle wheel spokes). This defines the weight of the normal.

## Export Validation

Exported waypoints include trajectory-start and trajectory-end markers, allowing post-processors to identify path segments. After generating KRL, G-code, or another machine program, validate frames, poses, joint limits, speeds, and I/O commands in offline simulation or a controller test environment.
