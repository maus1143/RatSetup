import os
import urllib.request
import subprocess

firefox_url = "https://download.mozilla.org/?product=firefox-latest&os=win&lang=en-US"
notepadpp_url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.2/npp.8.5.2.Installer.x64.exe"
vscode_url = "https://update.code.visualstudio.com/latest/win32-x64/stable"
discord_url = "https://dl.discordapp.net/apps/win/1.0.9012/DiscordSetup.exe"
winscp_url = "https://download.winscp.net/WinSCP-5.21.7-Setup.exe"
gimp_url = "https://download.gimp.org/pub/gimp/v2.10/windows/gimp-2.10.34-setup.exe"
sevenzip_url = "https://www.7-zip.org/a/7z1900-x64.exe"

firefox_filename = "firefox_installer.exe"
notepadpp_filename = "notepadpp_installer.exe"
vscode_filename = "vscode_installer.exe"
discord_filename = "discord_installer.exe"
winscp_filename = "winscp_installer.exe"
gimp_filename = "gimp_installer.exe"
sevenzip_filename = "sevenzip_installer.exe"

def download_file(url, filename):
    print(f"Lade {filename} von {url} herunter...")
    urllib.request.urlretrieve(url, filename)
    print(f"{filename} gedownloadet.")

download_file(firefox_url, firefox_filename)
download_file(notepadpp_url, notepadpp_filename)
download_file(vscode_url, vscode_filename)
download_file(discord_url, discord_filename)
download_file(winscp_url, winscp_filename)
download_file(gimp_url, gimp_filename)
download_file(sevenzip_url, sevenzip_filename)

def run_installer(filename):
    print(f"Installiere {filename}...")
    subprocess.run([filename], shell=True)
    print(f"{filename} installiert.")

run_installer(firefox_filename)
run_installer(notepadpp_filename)
run_installer(vscode_filename)
run_installer(discord_filename)
run_installer(winscp_filename)
run_installer(gimp_filename)
run_installer(sevenzip_filename)

print("Alle Installationen abgeschlossen.") #By Mausi Schmausi