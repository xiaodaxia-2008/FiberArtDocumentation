# Post-processing Customization

FiberArt uses Jinja2 templates to convert trajectories into machine programs. Post-processors are normally selected from the Simulation/PostProcess panel. After generation, verify frames, poses, speeds, and I/O commands in the target controller or an offline simulation environment.

## Shipped Templates

The current release includes these commonly used templates:

- `KukaKRLLW`: the Layway KUKA KRL post-processor, with layer, line, and generation-progress tracking;
- `KukaKRLXR`, `KukaKRLSubProg`, and `KRLFS`: KUKA KRL output templates;
- `KukaCNC`: KUKA CNC output template;
- `InovanceScan`: Inovance scanning trajectory output template;
- `ToJson` and `ToPoses`: export trajectories as JSON or pose data for debugging and data exchange.

## Custom Templates

Advanced users can copy an existing template and adapt it to the target controller syntax. Templates receive trajectory, robot/positioner degrees of freedom, tool, and program data. They can also use built-in pose-conversion filters to generate KUKA poses, axis-angle values, or other representations.

At minimum, verify that:

1. The position and pose frames match the machine configuration.
2. The pose format and angle units match the controller requirements.
3. Start, placement, cut, heating, and other I/O commands match the cell signals.
4. Trajectory boundaries, layer numbers, and line numbers are preserved.
5. The generated program has been tested in offline simulation or a controller test environment.

KRL output removes blank lines and redundant whitespace by default and can split output into multiple files when required. Templates can configure the maximum number of lines per file. Never send an unverified program directly to a machine.
