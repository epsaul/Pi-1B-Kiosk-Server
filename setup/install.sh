#!/bin/bash

echo "🚀 Starting kiosk setup..."

# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install required packages
sudo apt install -y \
  xserver-xorg \
  x11-xserver-utils \
  xinit \
  openbox \
  chromium-browser \
  unclutter \
  lightdm

# 3. Create autostart script
mkdir -p ~/.config/openbox
cat <<EOF > ~/.config/openbox/autostart
# Hide mouse cursor after idle
unclutter &

# Launch Chromium in kiosk mode
chromium-browser --noerrdialogs --kiosk http://localhost &

EOF

# 4. Set up .xinitrc to start Openbox
echo "exec openbox-session" > ~/.xinitrc

# 5. Enable auto-login and startx on boot
sudo raspi-config nonint do_boot_behaviour B2  # Console autologin
echo "startx" >> ~/.bash_profile

echo "✅ Kiosk setup complete. Rebooting..."
sudo reboot
