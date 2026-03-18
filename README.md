# Going UI Skill

Claude Code skill for **Going Library** — an industrial HMI/SCADA UI framework built on C# .NET 8.0 with SkiaSharp rendering.

## What It Does

- **Generate .gud files** — UI design files (JSON) with 40+ industrial controls (GoButton, GoLamp, GoDataGrid, GoSlider, etc.)
- **Write C# code** — Event binding, OnUpdate data synchronization, page/window lifecycle
- **Handle communications** — Modbus RTU/TCP, MQTT, LS Electric CNet, Mitsubishi MC PLC
- **Deploy to devices** — Build and deploy to Raspberry Pi touch panels via LauncherTouch MCP

## Installation

```
/plugin install going-ui@marketplace
```

## Trigger Keywords

`Going`, `GoButton`, `GoLamp`, `GoSlider`, `GoInput`, `GoValue`, `GoDesign`, `.gud`, `Modbus`, `MasterRTU`, `SlaveRTU`, `MQTT`, `HMI`, `SCADA`, `PLC`, `LauncherTouch`, `gtcli`

## NuGet Packages

| Package | Description |
|---------|-------------|
| [Going.Basis](https://www.nuget.org/packages/Going.Basis) | Communications & utilities (Modbus, MQTT, CNet, MC) |
| [Going.UI](https://www.nuget.org/packages/Going.UI) | Platform-independent UI core (controls, themes, design) |
| [Going.UI.OpenTK](https://www.nuget.org/packages/Going.UI.OpenTK) | OpenTK adapter (embedded/Raspberry Pi) |
| [Going.UI.Forms](https://www.nuget.org/packages/Going.UI.Forms) | WinForms adapter |

## Skill Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Entry point — workflow, rules, file reference table |
| `ui-json-quick.md` | Single-file .gud generation guide (all controls) |
| `ui-json.md` | Detailed .gud structure, enums, themes |
| `ui-image-to-gud.md` | 6-step image-to-.gud conversion procedure |
| `ui-code.md` | C# code patterns, Designer.cs rules |
| `basis.md` | Communication patterns (Modbus, MQTT, CNet, MC) |
| `ui-mcp.md` | Device deployment via gtcli CLI |
| `api/` | 21 HTML API reference files |

## License

MIT
