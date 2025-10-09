## thoughts/2025-10-10-jessie-lite-revival.md

### Jessie Lite Revival – Milestone Log

- Selected **Jessie Lite (2017-03-02)** for full legacy fidelity on Pi 1B, honoring ARMv6 compatibility and kiosk simplicity.
- Verified SHA256 hash of downloaded image:
  `AA30736371AB6688AF8091F8B61E0CEB1237FA0117B788341711848011E94052`
- Flashed `.img` to 16GB SD card using Raspberry Pi Imager, skipping customisation settings to preserve legacy integrity.
- Mounted boot partition post-flash; created blank `ssh` file to enable remote access.
- Attempted hostname override via boot partition (`hostname` file), but Jessie Lite required manual edit:
  - `/etc/hostname` → `does-kiosk`
  - `/etc/hosts` → `127.0.1.1 does-kiosk`
- Rebooted and confirmed hostname change.
- Discussed IPv4 and IPv6 support:
  - DHCP confirmed active; static IP optional.
  - IPv6 supported at kernel level; link-local address observed.
- Logged in with default credentials (`pi / raspberry`) and confirmed successful boot.

Next steps: clone Gerald’s working branch, configure systemd service, embed kiosk logic, and begin poetic milestone logging.


# Thoughts.md

## 2025-10-01 · Systemd Handover

The Flask server is now managed by systemd.  
Manual invocation retired.  
Boot logs confirm clean initialisation.  
A quiet architectural signature replaces the old ritual.

## 2025-10-01 · Network Migration

The Pi has joined the DoES network.  
SSH and IP reconfigured.  
Connection confirmed via 192.168.1.102.  
The kiosk now listens from new ground.

## 2025-10-02 · SSH Reset

Connection reset by peer.  
No crash, no panic—just the laptop hibernating.  
The Pi held steady.  
Session restored without incident.

## 2025-10-02 · Shutdown Ritual

Pi powered down for transport.  
Systemd closed services cleanly.  
Awaiting reawakening at DoES.

## 2025-10-03 · README Refactor

## 2025-10-03 · Bauhaus Shift

## 2025-10-04 · Gerald Reconstructed

### System
- Raspberry Pi 1B
- Node.js v11.15.0
- npm v6.7.0
- Express v4.17.1
- Axios v0.21.1
- dotenv v17.2.2

### Process
1. Installed Node and npm via `n 11.15.0`
2. Scoped Express install to backend folder
3. Downgraded Axios to CommonJS-compatible version
4. Launched backend with `node server.js`

### Output
Starting Gerald's backend...  
Token loaded: ghp_rN0x21...  
Server running at http://localhost:3000

### Architecture
- Front end: Static HTML/CSS/JS interface
- Backend: RESTful Node server
- Flow: Client → Server → GitHub API

### Ethos
“They do not preach that their God will rouse them a little before the nuts work loose.”  
— Kipling, *The Sons of Martha*

### Function
Gerald listens. Gerald speaks. Gerald serves.  
Ed maintains. Ed reflects. Ed documents.
