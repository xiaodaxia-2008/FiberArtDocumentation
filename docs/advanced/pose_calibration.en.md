# Poses and Calibration

## Editing Poses

When editing a pose, robot properties, or TCP calibration data, choose the rotation representation from the **Format** list. The available formats are:

- Euler angles: intrinsic or extrinsic XYZ, XZY, YXZ, YZX, ZXY, and ZYX sequences;
- Robot-specific formats: `KukaABC`, `KawasakiOAT`, `MitsubishiABC`, and `FanucWPR`;
- `URAngleAxis` axis-angle representation;
- `Quaternion`, with components ordered as `I, J, K, W`.

Euler angles, robot-specific formats, and axis-angle values use degrees. Quaternions have no angle unit. Switching formats preserves the current pose and redisplays its rotation components.

**Copy** places the pose JSON on the clipboard. **Paste** restores a seven-element pose from the clipboard, which must contain valid pose JSON with position and rotation data.

## Default Pose Format

The default pose format is `EulerIntrinsicXYZ`. To use one representation consistently, set `GUI/DefaultPoseFormat` in the global parameters to one of the format names listed above. Workpiece pose calibration uses this setting when displaying its rotation result. An unset or invalid value falls back to `EulerIntrinsicXYZ`.

## Workpiece Pose Calibration

Open the **Workpiece Pose Calibration** panel and enter the same feature points in two tables: one in the workpiece frame and one in the base frame.

1. The two tables must contain the same number of points.
2. At least three point pairs are required.
3. Use **Add** to add rows, **Remove** to delete selected rows, **Clear** to reset a table, or paste point coordinates from the clipboard.
4. Click **Compute** to calculate the workpiece pose relative to the base frame.

The result contains X, Y, Z translation and rotation components in the configured default pose format. It is also copied to the clipboard as JSON. Quaternion output uses `I, J, K, W`; other formats output three rotation components.

!!! warning "Note"
    Make sure corresponding points in the two tables are entered in the same order, and use meters for point coordinates.

## TCP Calibration

Open the **TCP Calibration** panel and enter at least three different flange poses. Each pose can use any of the formats described above. Click **Compute TCP** to calculate the TCP position in the flange frame. The panel displays X, Y, Z and copies the result JSON to the clipboard.
