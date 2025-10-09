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

Next steps: clone Gerald’s working branch, configure systemd service, embed kiosk logic.
