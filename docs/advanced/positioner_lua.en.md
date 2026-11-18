# Custom positioner angles with Lua

!!! note "Availability"
    Added on develop after v0.25.0; not included in the v0.25.0 installer.

1. Open the **Simulation/PostProcess** panel and select the simulation group.
2. Select **RuleBased** as the system IK algorithm.
3. In the **Positioner** tab, select **CustomFunction**.
4. Click **Edit Custom Function**, enter a Lua script, then click **OK**.
5. Recompute the trajectory and inspect the simulation.

The script must return a function accepting `(pose, qseed)`. `pose` is the
target TCP pose in the workpiece coordinate system. `qseed` is a Vector
containing only positioner joints: the initial system seed for the first
point and the previous function result for subsequent points. Vector indices
start at 1. Return a one-element Vector in radians. Translations use meters.

For example, hold the positioner at 30 degrees:

```lua
return function(pose, qseed)
    return Vector.from(math.rad(30))
end
```

To retain the initial angle throughout the path:

```lua
return function(pose, qseed)
    return qseed
end
```

Scripts are saved with the trajectory's solver parameters. Syntax errors,
runtime errors, nil results, incorrect vector sizes and nonfinite joint values
fail trajectory solving. The existing robot IK compensates for the selected
positioner angle. The workpiece must be attached below the positioner in the
scene hierarchy. As with the existing external-axis strategies, the script is
used by the RuleBased algorithm; OptimizationBased solves axes independently.
When **Prefer waypoint joints** is enabled, valid supplied waypoint joints
retain their existing priority.

## Rounded-end paths and 180-degree flips

At an end pole the surface normal can become parallel to the positioner axis.
Its transverse projection vanishes and reverses after the pole, so Align can
request a sudden 180-degree rotation. Lowering normal weight alone does not
remove a pole where the radial component also vanishes.

Use known axial coordinates to define a transition region and compute a smooth
angle through it. Axial position alone cannot distinguish the outgoing and
return legs: use transverse position, previous angle, or explicit script state
as well. Unwrap the angle relative to qseed instead of switching between +pi
and -pi. Merely holding the last angle at the pole can postpone the jump.

The callback has no path lookahead, time or arc-length argument. Any state in a
Lua closure is local to one solving invocation and is recreated on the next
solve. Choose a sufficiently long transition and inspect robot reachability,
collisions and positioner speed/acceleration. The script defines angles, not
a guaranteed motion-time profile. The axis, pole location and transition range
must match the actual workpiece coordinate system.
