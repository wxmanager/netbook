# Netbook User interface

This will be a stripped down user interface for netbook and other low powered computers, This will strip down most features to keep the essentials only

## Todo

- [x] Port Atomizer to its simplest form
- [x] Create a light web browser for the user interface
- [ ] (W.I.P) Develop a basic file manager

## Required Packages

- PyQt5 - Avaliable on Pip or your own linux package manager
- QtWebEngineWidgets - Also Avaliable on pip or linux package manager
- termQt - Not avaliable on pip but you can download the package [here](https://github.com/TerryGeng/termqt/releases/download/0.1/termqt-0.1-py3-none-any.whl)
### ARM install guide

For ARM7 and ARM8 Users id recommend any debian based distro, I've tested this on Debian Bullseye ARM7, hopefully it should apply to ARM8 users

you need to install the following packages if you will be cloning from git! Please keep in mind APT is your best option as of right now because pip doesn't seem to work on ARM

PyQT5:
`sudo apt install python3-pyqt5`

QtWebEngineWidgets:
`sudo apt-get install python3-pyqt5.qtwebengine`
