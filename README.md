# Pi-1B Kiosk Server

A lightweight kiosk interface designed to run on a Raspberry Pi 1B. This project powers a simple, resilient display system for public-facing terminals—ideal for issue tracking, status boards, or interactive signage.

---

## 🚀 Features

- Runs on legacy hardware (Raspberry Pi 1B)
- Boots directly into kiosk mode
- Displays a web-based interface (e.g. DoES Liverpool issue tracker)
- Auto-restarts on crash or power loss
- Minimal setup and maintenance

---

## 🧰 Requirements

- Raspberry Pi 1B (or compatible)
- HDMI display
- MicroSD card (8GB+ recommended)
- Internet connection (Wi-Fi or Ethernet)
- Raspberry Pi OS Lite (Debian-based)

---

## 🛠️ Setup Instructions

1. **Flash Raspberry Pi OS Lite** to your SD card using [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. **Enable SSH** by placing an empty `ssh` file in the boot partition
3. **Clone this repo**:
   ```bash
   git clone https://github.com/epsaul/Pi-1B-Kiosk-Server.git
   cd Pi-1B-Kiosk-Server
