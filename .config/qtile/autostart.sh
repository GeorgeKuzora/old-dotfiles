#!/bin/sh
feh --bg-fill /home/georgiy/Pictures/Wallpapers/ign_waifu.png
picom --experimental-backends --vsync --config ~/.config/picom/picom.conf & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

# Language manager fcitx5
fcitx5 -d & disown

# Keyboad layout change with xmodmap
xmodmap ~/.xmodmap & disown

# Yandex disk autostart
yandex-disk start & disown

# Clipboard menu daemon
clipmenud & disown

# Timeshift snapshots daemon
timeshift & disown

nm-applet &

# Startup monitor change
sleep 1
intern=eDP
extern=HDMI-A-0
if xrandr | grep "$extern disconnected"; then
    xrandr --output eDP --mode 1920x1080
else
    xrandr --output HDMI-A-0 --primary --mode 1920x1080 --left-of eDP --mode 1920x1080
fi
