#!/bin/sh
intern=eDP
extern=HDMI-A-0

sleep 1

if xrandr | grep "$extern disconnected"; then
    autorandr autorandr --load docked --force
else
    autorandr autorandr --load mobile
fi
    
    
    
#     xrandr --output "$extern" --off --output "$intern" --auto
# else
#     xrandr --output "$intern" --off --output "$extern" --auto
# fi

# скрипт должен загружаться при включении компьютера и перезаписывать неправильный порядок мониторов