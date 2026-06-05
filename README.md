# FenceGuard

An early warning system for livestock fencing, built to detect predator activity before it becomes a loss.

I keep chickens and Muscovy ducks on a small farm on Gotland, Sweden. Over the years we've had foxes take birds on several occasions, and four years ago a neighbour's dog got into the yard and killed our entire flock while we were out. FenceGuard started as a straightforward question: can I get a warning before that happens, rather than finding out after?

The full vision is a LoRa mesh of sensor nodes with weather integration to filter false alarms from wind and rain. But good engineering means validating assumptions before building on top of them — so this project starts with the actual hard problem: understanding the raw signal.

Can a PIR sensor reliably distinguish real motion events from wind, branches, and other environmental noise? That's what I'm working out first.

---

## Hardware

| Component | Purpose |
|---|---|
| Pycom LoPy4 | Microcontroller |
| HC-SR501 PIR | Motion detection |
| Vibration sensor *(planned)* | Fence contact detection |

The LoPy4 is used here because one was already on the desk from an earlier project. Pycom has since shut down, so future hardware revisions will likely move to a Waveshare ESP32 or similar LoRa-capable board.

## Wiring (HC-SR501 → LoPy4 Expansion Board)

| HC-SR501 | LoPy4 |
|---|---|
| Power | VIN (5V) |
| GND | GND |
| Output | P20 |

> ⚠️ HC-SR501 needs 5–20V supply but outputs 3.3V — safe to connect directly to LoPy4 GPIO.

## HC-SR501 Settings

- **Time Delay**: Counter-clockwise to minimum (~5 sec) during testing
- **Sensitivity**: 3–7m range
- **Trigger jumper**: L = single trigger, H = repeatable trigger

---

## Getting Started

### Requirements

- VS Code + Pymakr extension
- LoPy4 with Expansion Board
- MicroPython firmware (tested on 1.18.3)

### Running

1. Clone the repo and open in VS Code
2. Connect LoPy4 via USB
3. Connect device in Pymakr panel
4. Run in Pymakr terminal:

```python
exec(open('main.py').read())
```

---

## Status

| Step | Status |
|---|---|
| PIR sensor basic read | ✅ Done |
| Timestamped logging | 🔄 In progress |
| Outdoor testing — wind vs. motion | ⏳ Planned |
| Vibration sensor | ⏳ Planned |
| LoRa transmission | ⏳ Planned |

## Structure

```
fenceguard-sensor/
├── boot.py          # Device startup
├── main.py          # PIR read loop
└── pymakr.conf      # Pymakr config
```

---

I'm documenting the whole process as I go — hardware choices, firmware, and data analysis. Follow along if that's your kind of thing.
https://dev.to/emeliefogelstrom/
