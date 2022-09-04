#!/bin/bash
sleep 1
intern=eDP
extern=HDMI-A-0
hdmi_sink="alsa_output.pci-0000_04_00.1.hdmi-stereo"
if xrandr | grep "$extern disconnected"; then
    xrandr --output eDP --mode 1920x1080
else
    xrandr --output HDMI-A-0 --primary --mode 1920x1080 --left-of eDP --mode 1920x1080
    pactl set-default-sink $hdmi_sink
fi
    
    
    
#     xrandr --output "$extern" --off --output "$intern" --auto
# else
#     xrandr --output "$intern" --off --output "$extern" --auto
# fi

# скрипт должен загружаться при включении компьютера и перезаписывать неправильный порядок мониторов
