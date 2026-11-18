# Rotating courses around a part axis

!!! note "Availability"
    Added on the develop branch after v0.25.0; not included in the v0.25.0 installer.

Use **Rotate to Generate Courses** in a Course node's context menu to create
rotated copies in the same ply. Each copy contains all tows from the source
course. The original course is retained.

1. Plan and inspect the source course.
2. Create a line segment node along the part's rotation axis.
3. Right-click the source course and select **Rotate to Generate Courses**.
4. Select the line segment in the scene tree and click **Set** beside
   **Rotation Axis**. The segment's start-to-end direction defines positive
   rotation by the right-hand rule.
5. Check **Layup Mesh**. The dialog normally selects the source ply's mesh
   ancestor. For a detached ply, select its actual mesh instance and click Set.
6. Choose a distribution and adjust the sweep and surface tolerance.
7. Click **Preview** to inspect temporary results, or **Generate** to insert
   independent courses immediately after the source. Undo removes the entire
   generated batch; Redo restores it.

The dialog remains open while selecting scene nodes. Closing it or changing
parameters removes its preview. Generation always recalculates from current
source geometry and current node poses.

## Distribution

- **By Total Count** includes the original course in the specified total.
  A full turn divides the circle equally without duplicating the original at
  360 degrees. For example, 12 total courses produce 11 new courses spaced by
  30 degrees. A partial sweep includes its endpoint.
- **By Angle Step** generates complete steps within the sweep. It does not
  add a shorter final step when the sweep is not divisible by the step.
- A negative sweep reverses the rotation direction. At most 1000 courses,
  including the original, are allowed in a batch.

## Geometry and subsequent simulation

The segment's origin and direction are read in world coordinates, then
transformed into the selected mesh instance's local coordinate system.
All tow centerlines, left/right boundaries and the course reference path are
rotated in that system and projected back to the original mesh. The selected
mesh must be the ply's actual mesh, and the course and mesh display frames
must agree.

The generated data preserves tow ordering, indices, material dimensions,
clipping intervals and minimum-length/gap settings. New Course and Tow nodes
are created from this data; display nodes are not cloned. Changing a generated
tow does not change its source or other copies. Generated courses use the
existing trajectory, simulation and postprocessing workflow.

Surface tolerance bounds the projection checks at path vertices and adaptive
midpoint samples. It is not a continuous clearance or overlap guarantee.
The existing mesh query uses single precision. Projection failures or
collapsed paths reject the batch before it is inserted. On a bullet-shaped
part, inspect spacing and overlap near the tip: equal angular spacing does
not provide constant surface spacing or automatically trim overlapping tows.
