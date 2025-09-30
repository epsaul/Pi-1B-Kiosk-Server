# SSH Setup for Headless Raspberry Pi: EdsPiKiosk

This document records the complete setup for enabling SSH access to a headless Raspberry Pi named EdsPiKiosk, using RSA public key authentication for the user `ed`. The client machine is a Windows laptop running Git Bash (`Ed@Lenovo25`), and the connection is made over a local network.

## System Overview

Client: Ed@Lenovo25 (Windows with Git Bash / MINGW64)  
Server: EdsPiKiosk.local  
User on Pi: ed  
Authentication Method: RSA public key  
Connection Method: SSH over local network  

## Key Generation (on Laptop)

Generate a new RSA key pair using:

ssh-keygen -t rsa -b 4096 -C "epsaul@yahoo.co.uk"

This creates the following files:

- Public key: ~/.ssh/id_rsa.pub  
- Private key: ~/.ssh/id_rsa  
- Fingerprint: SHA256:Uu648f5IIGEjaKfw5fhZUkVpv8ubogcBB/J2Putof1c

## Key Installation (on Raspberry Pi)

Ensure the public key is placed in /home/ed/.ssh/authorized_keys on the Pi. Set the correct permissions:

chmod 700 ~/.ssh  
chmod 600 ~/.ssh/authorized_keys  
chmod 755 ~

To copy the key from the laptop to the Pi:

cat ~/.ssh/id_rsa.pub | ssh ed@EdsPiKiosk.local 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && tee ~/.ssh/authorized_keys > /dev/null && chmod 600 ~/.ssh/authorized_keys'

## Connection Test

To test the SSH connection from the laptop:

ssh -i ~/.ssh/id_rsa ed@EdsPiKiosk.local

A successful login confirms that the key matches, the correct user is used, and the SSH server accepts RSA keys.

## Optional SSH Config Entry

To simplify future connections, add the following to ~/.ssh/config:

Host EdsPiKiosk  
    HostName EdsPiKiosk.local  
    User ed  
    IdentityFile ~/.ssh/id_rsa

Then connect using:

ssh EdsPiKiosk

## Status

SSH access confirmed working as of Tue Sep 30 2025, using RSA key authentication for user `ed`.

## 🗓️ Session Log: Tue Sep 30 2025

SSH access confirmed working for user `ed` on `EdsPiKiosk.local`, using RSA key authentication.  
RSA key fingerprint: `SHA256:Uu648f5IIGEjaKfw5fhZUkVpv8ubogcBB/J2Putof1c`  
SSH config entry added:
Host EdsPiKiosk  
  HostName EdsPiKiosk.local  
  User ed  
  IdentityFile ~/.ssh/id_rsa  

Permissions verified:  
chmod 700 ~/.ssh  
chmod 600 ~/.ssh/authorized_keys  
chmod 755 ~  

Connection tested via:  
ssh ed@EdsPiKiosk.local  

System updated and essential tools installed:  
sudo apt update && sudo apt upgrade -y  
sudo apt install git python3-pip avahi-daemon tmux  

GitHub repo cloned to Pi:  
git clone https://github.com/epsaul/Pi-1B-Kiosk-Server.git ~/PiKiosk  
cd ~/PiKiosk  

Kiosk server concept scaffolded:  
Headless Pi serves a local web form for submitting issues to the DoES Liverpool “Somebody Should” GitHub repo.  
Users connect via their own device on the local network:  
http://EdsPiKiosk.local:8080  
Form accepts issue title and description.  
Pi authenticates using stored GitHub token and posts to the repo.

Token stored securely at:  
/home/ed/.github_token  
chmod 600 ~/.github_token  

Accessed in Python via:  
with open('/home/ed/.github_token') as f:  
  token = f.read().strip()

Planned backend: Python + Flask  
Planned frontend: Simple HTML form rendered via Flask or templated

Optional enhancements:  
– QR code linking to the form  
– Local logging for redundancy  
– Poetic boot logs or status endpoint  
– Dropdowns for labels or categories  
– Autostart via systemd service:  
  sudo systemctl enable kiosk.service  
  sudo systemctl start kiosk.service  

Monitoring & safety notes:  
Safe to open new SSH session or use tmux during installs.  
Avoid conflicting apt or systemctl commands mid-upgrade.  
Use passive tools to monitor:  
htop  
journalctl -u kiosk.service -f  
curl http://EdsPiKiosk.local:8080  
tmux new -s monitor

