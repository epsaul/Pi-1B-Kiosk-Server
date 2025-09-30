from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Register font
pdf.add_font('NotoSans', '', '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf', uni=True)
pdf.set_font('NotoSans', '', 12)

# Title
pdf.set_font('NotoSans', '', 16)
pdf.cell(0, 10, 'SSH Setup for Headless Raspberry Pi: EdsPiKiosk', ln=True)
pdf.ln(5)

pdf.set_font('NotoSans', '', 12)

content = '''
System Overview:
- Client (Laptop): Ed@Lenovo25 (Windows with Git Bash / MINGW64)
- Server (Raspberry Pi): EdsPiKiosk.local
- User on Pi: ed
- Authentication Method: RSA public key
- Connection Method: SSH over local network

Key Generation (on Laptop):
- Command: ssh-keygen -t rsa -b 4096 -C "epsaul@yahoo.co.uk"
- Public key location: ~/.ssh/id_rsa.pub
- Private key location: ~/.ssh/id_rsa
- Fingerprint: SHA256:Uu648f5IIGEjaKfw5fhZUkVpv8ubogcBB/J2Putof1c

Key Installation (on Raspberry Pi):
- Public key must be placed in: /home/ed/.ssh/authorized_keys
- Permissions:
  chmod 700 ~/.ssh
  chmod 600 ~/.ssh/authorized_keys
  chmod 755 ~
- Re-copy command from laptop:
  cat ~/.ssh/id_rsa.pub | ssh ed@EdsPiKiosk.local 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && tee ~/.ssh/authorized_keys > /dev/null && chmod 600 ~/.ssh/authorized_keys'

Connection Test:
- Command: ssh -i ~/.ssh/id_rsa ed@EdsPiKiosk.local
- Successful login confirms key match, correct user, and SSH server acceptance

Optional SSH Config Entry:
- Add to ~/.ssh/config:
  Host EdsPiKiosk
      HostName EdsPiKiosk.local
      User ed
      IdentityFile ~/.ssh/id_rsa
- Connect with: ssh EdsPiKiosk
'''

for line in content.strip().split('\n'):
    pdf.multi_cell(0, 10, line)

output_path = '/mnt/data/EdsPiKiosk_SSH_Setup.pdf'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
pdf.output(output_path)

