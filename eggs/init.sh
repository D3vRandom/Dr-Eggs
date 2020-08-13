#!/bin/bash
apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update -y
apt-get upgrade -y
sudo apt-get install sdcc binutils python python-pip -y
sudo pip install -U pip
sudo pip install -U -I pyusb
sudo pip install -U platformio
pip install -e .