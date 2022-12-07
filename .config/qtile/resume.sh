#!/bin/bash

# Script that should be used after resume from sleep

# Sometimes after resume Caps -> Ctl binding is lost
# Keyboad layout change with xmodmap
xmodmap ~/.Xmodmap & disown

# Keyboad layout change with setxkbmap
setxkbmap -option 'ctrl:nocaps' &


# After resume laptop is muted unmute laptop
sleep 1
pamixer -u
# Change sound and unmute
#intern=eDP
# extern=HDMI-A-0
# hdmi_sink="alsa_output.pci-0000_04_00.1.hdmi-stereo"
# if xrandr | grep "$extern disconnected"; then
#     xrandr --output eDP --mode 1920x1080
# else
#     xrandr --output HDMI-A-0 --primary --mode 1920x1080 --left-of eDP --mode 1920x1080
#     sleep 1
#     pactl set-default-sink $hdmi_sink
# fi
