import os

print('[✓] Created By Arafat Mahin')

print('[+] For More Fonts/Colors Visit https://github.com/mahin788')

print('[©] Credit : Termux-Arafat Mahin')

print()

print('[-] Unzipping config')

os.system('unzip config.zip')

os.system('chmod 777 config/*')

print('[~] Installing Modules')

os.system('config/install.sh;rm $HOME/.termux/colors.sh $HOME/.termux/fonts.sh;cp config/* $HOME/.termux')

print('[•] Changing The Colours ')

os.system('$HOME/.termux/colors.sh')

print('[•] Changing The Fonts ')

os.system('$HOME/.termux/fonts.sh')

print('[•] Adding Android Logo ')

os.system('cp config/zshrc /data/data/com.termux/files/usr/etc;cd  /data/data/com.termux/files/usr/etc;rm motd.sh motd')

print('[✓] Successfully Installed Restart Termux App')

