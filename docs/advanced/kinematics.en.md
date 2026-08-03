# Multi-axis Linkage System Kinematics Settings

## Motion System Components

The simulated motion system consists of a track, robot, positioner, tool, and workpiece. Confirm their geometry, parent-child transforms, joint axes, limits, and TCP in the scene tree before selecting them in the simulation panel. When solving fails, first check frame directions, joint limits, and the tool attachment pose.

## Kinematic Algorithms

### OptimizationBased

Optimizes track, robot, and positioner joints together at each trajectory point. It is useful for coordinated multi-axis motion, reducing pose jumps, and redundant systems. It may take longer and the result should be checked against joint limits.

### RuleBased

Computes track and positioner joints using explicit rules, then solves the robot inverse kinematics. It is easier to predict and debug when the equipment process rules are already defined.

## Track Strategies

- `BaseShift`: computes track position from base shifts at the trajectory start and end; configure **Start Base Shift** and **End Base Shift**.
- `Fixed`: uses a fixed joint position.
- `AutoFixed`: automatically finds a fixed position for the current trajectory.
- `ConstantDistance`: keeps the track at a configured distance from the target.
- `ConstantDistanceLinearInterpolation`: satisfies the target distance at both ends and interpolates between them.
- `CustomFunction`: evaluates a custom function for the track joint. The function must return a valid value in the configured frame and units.

## Positioner Strategies

- `Align`: aligns the trajectory direction with a reference direction;
- `AlignLinearInterpolation`: solves the start and end of a course and linearly interpolates between them;
- `AlignCubicInterpolation`: solves the start and end and uses cubic interpolation between them;
- `Fixed`: uses a fixed joint position;
- `AutoFixed`: automatically selects a fixed position suitable for the current course.

**Start Direction** and **End Direction** define the reference directions at the ends of a course. **Normal Weight** controls the contribution of surface normal versus radial direction during alignment.

## Apply and Validate

In **LayupSimulation & PostProcess > Kinematics Setting**, choose the algorithm and strategies and click **Apply**. Use **Apply to All** to apply the settings to all selected trajectories. Re-run simulation and post-processing after changing these settings; do not reuse old kinematic results.

Check the following:

1. Robot, track, and positioner joints stay within their limits.
2. Poses do not jump or wrap unexpectedly around an axis.
3. TCP and workpiece reference frames are correct.
4. Collision checks include the actual tool, workpiece, and equipment collision geometry.
5. The exported program has been validated in offline simulation or at low speed.
