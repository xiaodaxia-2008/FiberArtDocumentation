# Post-processing Customization

FiberArt uses templates to convert trajectories into machine programs. Post-processors are normally selected from the Simulation/PostProcess panel. After generation, verify frames, poses, speeds, and I/O commands in the target controller or an offline simulation environment.

## Shipped Templates

The current release includes these commonly used templates:

- `KukaKRLLW`: the Layway KUKA KRL post-processor, with layer, line, and generation-progress tracking;
- `KukaKRLXR` and `KukaKRLFS` generate KUKA KRL output;
- `KukaCNC`: KUKA CNC output template;
- `CNC`, `XDCNC`, and `XDAxisCNC` generate CNC programs with feed-axis output;
- `ToJson` and `ToPoses`: export trajectories as JSON or pose data for debugging and data exchange.

## CNC Feed Axis

The `registers.feed_position` waypoint field stores the cumulative feed command in metres for each course. While any channel is restarting, it increases by the TCP path increment multiplied by the restart speed ratio. The position holds when feeding is idle. `CNC` converts it to millimetres on `E2`. `XDCNC` and `XDAxisCNC` output it on `W`. At the start of each course, these templates emit `G92` to define the current physical position as the new coordinate zero.

`XDCNC` and `XDAxisCNC` use `M101` to start the program, `M102` to close it, `M103` to turn heat and blow on, and `M104` to turn them off. The default cut dwell is one second. Match the controller commands and axis assignments to the machine configuration.

## Custom Templates

Advanced users can copy an existing template and adapt it to the target controller syntax. Templates receive trajectory, robot/positioner degrees of freedom, tool, and program data. They can also use built-in pose-conversion filters to generate KUKA poses, axis-angle values, or other representations.

Manage local scripts in the export area of the **Simulation/PostProcess** panel. See [Simulation and Export](../user_guides/simulation.en.md) for installing, using, and removing online versions.

- **Install**: choose a `.py` or `.jinja` script, copy it into the software post-processor directory, and add it to the combo box; if a script with the same name exists, you are asked to confirm before it is overwritten;
- **Edit**: modify the selected script in the built-in editor; `.jinja` templates come with Jinja syntax highlighting;
- **Delete**: after confirmation, remove the selected script from disk and from the combo box.

At minimum, verify that:

1. The position and pose frames match the machine configuration.
2. The pose format and angle units match the controller requirements.
3. Start, placement, cut, heating, and other I/O commands match the cell signals.
4. Trajectory boundaries, layer numbers, and line numbers are preserved.
5. The generated program has been tested in offline simulation or a controller test environment.

KRL output removes blank lines and redundant whitespace by default and can split output into multiple files when required. Templates can configure the maximum number of lines per file. Never send an unverified program directly to a machine.
