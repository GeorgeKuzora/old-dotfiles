#!/bin/bash

# devices
laptop_sink="alsa_output.pci-0000_04_00.6.analog-stereo"
jbl_sink="bluez_output.88_D0_39_10_4A_0B.1"
hdmi_sink="alsa_output.pci-0000_04_00.1.hdmi-stereo"
headphones_off="Missing device address argument"

curr_device="$(pactl get-default-sink)"
headphones_stat="$(bluetoothctl info)"

# intern=eDP
extern=HDMI-A-0
# check if headphones connected
if [ "$headphones_stat" = "$headphones_off" ]
then
# if headphones isn't connected switch either HDMI or laptop
    if xrandr | grep "$extern disconnected"; then
        # xrandr --output eDP --mode 1920x1080
        pactl set-default-sink $laptop_sink
        notify-send --icon=computer-laptop "Switched to laptop" "☕<fe0f>🎶" &
    else
        # xrandr --output HDMI-A-0 --primary --mode 1920x1080 --left-of eDP --mode 1920x1080
        pactl set-default-sink $hdmi_sink
        notify-send --icon=audio-speakers "Switched to HDMI" "☕<fe0f>🎶" &
    fi
# if headphones connected
else
# if headphones connected change sink to headphones
    notify-send --icon=audio-headphones "Switched to headphones" "☕<fe0f>🎶"
    pactl set-default-sink $jbl_sink
fi

# Set unmute for every thing
pamixer -u
