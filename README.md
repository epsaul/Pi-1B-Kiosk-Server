# Pi-1B Kiosk Server

A lightweight kiosk interface for Raspberry Pi 1B. Designed for public-facing terminals such as issue trackers, status boards, or interactive signage. Prioritises resilience, simplicity, and minimal resource usage.

## Overview
- Runs on legacy hardware (Raspberry Pi 1B)
- Boots directly into kiosk mode
- Displays a web-based interface (e.g. DoES Liverpool issue tracker)
- Auto-restarts on crash or power loss
- Minimal setup and maintenance

## Requirements
- Raspberry Pi 1B (or compatible)
- HDMI display
- MicroSD card (8GB+ recommended)
- Internet connection (Wi-Fi or Ethernet)
- Raspberry Pi OS Lite (Debian-based)

## Installation
1. Flash Raspberry Pi OS Lite to SD card using Raspberry Pi Imager  
2. Enable SSH by placing an empty file named `ssh` in the boot partition  
3. Clone this repository:  
   `git clone https://github.com/epsaul/Pi-1B-Kiosk-Server.git`  
   `cd Pi-1B-Kiosk-Server`  
4. Run the setup script:  
   `sudo bash setup/install.sh`  
5. Reboot. The kiosk interface will launch automatically.

## Project Structure
Pi-1B-Kiosk-Server/  
├── README.md  
├── setup/  
│   └── install.sh  
├── kiosk.py  
├── assets/  
│   └── logo.png  
└── .gitignore

## Notes
- Designed for unattended environments  
- Adaptable to other Raspberry Pi models  
- Flask backend serves local interface  
- Systemd manages service lifecycle

## License
MIT License. See `LICENSE` for details.

## Contributing
Pull requests welcome. Fork the repository and submit changes.

## Future Plans
- Serve DoES interface via Flask  
- Expose Pi to public internet via tunneling or port forwarding  
- Secure GitHub API token via `.env`  
- Add HTTPS support (Caddy or self-signed cert)  
- Improve UX clarity for local-only submission
