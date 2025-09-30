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
   ```
4. **Run the setup script**:
   ```bash
   sudo bash setup/install.sh
   ```
5. **Reboot** and the kiosk interface should launch automatically

---

## 📁 Project Structure

```
Pi-1B-Kiosk-Server/
├── README.md
├── setup/
│   └── install.sh
├── src/
│   └── kiosk.py
├── assets/
│   └── logo.png
└── .gitignore
```

---

## 🧠 Notes

- Designed for simplicity and reliability
- Ideal for unattended environments
- Can be adapted for other Raspberry Pi models

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🤝 Contributing

Pull requests welcome! If you have ideas for improvements or want to adapt this for other use cases, feel free to fork and submit changes.

#Future Plans:
# 🌐 Serving the DoES Interface from a Raspberry Pi 1B

## ✅ Goal

Deploy the `index.html` from [DoES_Somebody_should_interface](https://github.com/epsaul/DoES_Somebody_should_interface) on a Raspberry Pi 1B as a public-facing mini website that allows anyone to submit GitHub issues—even from outside the local network.

---

## 🧱 What’s Already in Place

- Static front-end: `index.html`, `style.css`, `script.js`
- Flask backend (from Pi kiosk project) that can post issues to GitHub
- Raspberry Pi 1B running a local server

---

## 🌍 Making It Public

### 1. **Expose the Pi to the Internet**
- Set up **port forwarding** on your router (e.g., forward port 80 or 443 to the Pi)
- Or use a tunneling service:
  - [ngrok](https://ngrok.com/)
  - [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
  - [localtunnel](https://github.com/localtunnel/localtunnel)

### 2. **Serve the Static Site**
- Use Flask’s `send_from_directory()` to serve static files
- Or use a lightweight web server:
  - **Nginx** (robust, configurable)
  - **Caddy** (auto HTTPS, minimal setup)

### 3. **Enable HTTPS**
- Use **Caddy** for automatic HTTPS via Let’s Encrypt
- Or configure **Nginx** with a free SSL certificate
- Or use **ngrok**, which provides HTTPS out of the box

### 4. **Secure the GitHub API Token**
- Store token in `.env` (never expose to frontend)
- Validate and sanitize form inputs before submitting to GitHub

---

## 🧠 Performance Considerations

- Pi 1B is capable for light traffic and form submissions
- For heavier use:
  - Serve static site via GitHub Pages or Netlify
  - Keep Pi as backend-only API endpoint

---

## 🧼 UX Considerations

- Add a **“Local Only”** or **“Secure Submission”** banner
- Explain clearly:
  > “This kiosk runs locally and does not transmit sensitive data. Submissions are sent securely to GitHub via API.”
- Link to the GitHub repo for transparency

---

## 🧪 Optional: Serve HTTPS Locally

Generate a self-signed cert and run Flask with:
```python
app.run(ssl_context=('cert.pem', 'key.pem'))
