# Simulation

Open **LayupSimulation & PostProcess** from **Functions** on the main menu. The panel is scrollable and contains a motion-system section, a trajectory-node list, and two tabs: **Simulation and Export** and **Kinematics Setting**.

## Motion System

The **Motion System** section at the top specifies the equipment used by the simulation:

- **Track**: select a linear track node;
- **Robot**: select a robot node;
- **Positioner**: select a positioner node;
- **Tool**: select a tool or placement-head node.

Each device has **Select** and **Clear** buttons. Select a node of the corresponding type in the scene tree before clicking **Select**; its node path is then shown in the read-only field. The positioner and track tabs in the kinematics settings are disabled when the corresponding device is not set. When the panel opens, it automatically tries to find the first available track, robot, tool, positioner, and trajectory node in the scene tree.

## Trajectory Nodes

The trajectory-node list is below the motion-system section:

- **Add Traj Node**: add the currently selected trajectory node from the scene tree;
- **Delete Traj Node**: remove the current list item;
- **Clear**: clear the trajectory-node list;
- **Auto Select**: automatically select the first available device and trajectory node from the scene tree.

The list can contain multiple trajectory nodes. Selecting an item displays that trajectory and loads its saved kinematics parameters; sibling trajectories are hidden when the current item changes. At least one valid trajectory node is required before simulation or export.

## Simulation and Export

### Simulation Controls

In the **Simulation and Export** tab:

- **Speed**: simulation speed ratio from 1% to 2000%, with a default of 100%;
- **Default**: restore 100% speed;
- **Max**: set the speed to 2000%;
- The playback buttons are **start**, **pause**, **continue**, and **stop**; the progress bar shows simulation progress.

Click **start** to run the simulation using the selected trajectories, devices, and kinematics settings. If no trajectory is selected, the simulation does not start. Use **continue** after pausing and **stop** to terminate the current simulation.

### Post-processing and Export

The export area on the same tab contains:

- **Post Script**: select an installed `.py` post-processing script or `.jinja` template;
- **Install**: choose a `.py` or `.jinja` post-processing script, copy it into the software post-processor directory, and add it to the combo box; an existing file with the same name is overwritten;
- **Export Path**: enter the program output path, or click **Select** to open a save-file dialog; changing the post script or trajectory list updates the default filename from the trajectory names and script suffix;
- **Reference**: set the coordinate frame used by the exported program. It defaults to the scene root and therefore the world frame;
- **Reset**: restore the world reference frame;
- **Select**: set the currently selected scene-tree node as the reference node;
- **Export**: solve the kinematics for the trajectories in the list and invoke the selected post-processor.

During export, waypoint poses are transformed into the reference-node frame. If a robot has a TCP, the TCP information is included in the export data. The first and last waypoints of each trajectory receive trajectory-start and trajectory-end markers so templates can identify trajectory segments. Verify the devices, trajectories, reference node, post script, and export path before exporting.

## Kinematics Setting

In the **Kinematics Setting** tab, choose a **Kinematic Algorithm**:

- **OptimizationBased**: use an optimization model to calculate the track, robot, and positioner motion together;
- **RuleBased**: calculate external-axis positions from the track and positioner rules, then solve the robot joints.

Click **Apply** to save the current settings to the current trajectory. Click **Apply to All** to save them to every trajectory in the list. Switching trajectories loads that trajectory's own kinematics parameters.

### Track

After a track is selected, the **Track** tab becomes available. Under the rule-based algorithm, its strategies are:

- **BaseShift**: calculate track positions from the start and end base shifts;
- **Fixed**: use a fixed position;
- **AutoFixed**: calculate a fixed position automatically;
- **ConstantDistance**: keep a fixed base-to-target distance;
- **ConstantDistanceLinearInterpolation**: satisfy the distance at the endpoints and interpolate linearly between them;
- **CustomFunction**: click **Click to Edit** to edit a custom function for calculating track positions.

Depending on the strategy, the enabled fields are **Fixed Position**, **Start Base Shift**, **End Base Shift**, **Base To Target**, or **Custom Function**. Fields that do not apply to the selected strategy are disabled.

### Positioner

After a positioner is selected, the **Positioner** tab becomes available. Under the rule-based algorithm, its strategies are:

- **Align**: align the trajectory direction with the reference direction;
- **AlignLinearInterpolation**: solve alignment at the start and end of a course and linearly interpolate intermediate points;
- **AlignCubicInterpolation**: solve alignment at the start and end of a course and use cubic interpolation for intermediate points;
- **Fixed**: use a fixed position;
- **AutoFixed**: automatically calculate a suitable fixed position for the current trajectory.

The tab contains **Fixed Position**, **Start Direction**, **End Direction**, and **Normal Weight**. **Fixed Position** is enabled for **Fixed**; the direction and normal-weight fields are enabled for the other strategies.

See [Multi-axis Linkage System Kinematics Settings](../advanced/kinematics.en.md) for the strategy details.

## Recommended Order

1. Prepare the robot, tool, track, positioner, and trajectory nodes in the scene tree.
2. Select the devices in **Motion System**, or click **Auto Select**.
3. Add the trajectories to the trajectory-node list.
4. Choose the algorithm and strategies in **Kinematics Setting**, then click **Apply** or **Apply to All**.
5. Set the speed in **Simulation and Export** and click **start** to inspect the motion.
6. Select the post script, export path, and reference node, then click **Export**.
7. Validate frames, poses, joint limits, speeds, and I/O commands in offline simulation or a controller test environment.
