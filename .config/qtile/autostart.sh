#!/bin/bash
# Wallpaper set via script
bash /home/georgiy/.local/bin/rofi_scripts/wallpaper_set & disown
#feh --no-fehbg --bg-fill "/home/georgiy/Pictures/Wallpapers/nord-wallpapers/undefined - Imgur.jpg"
# Enable picom compositor
picom --experimental-backends --vsync --config ~/.config/picom/picom.conf & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

# start polkit agent from GNOME
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown 

# Language manager fcitx5
fcitx5 -d & disown

# Keyboad layout change with xmodmap
# xmodmap ~/.Xmodmap & disown

# Keyboad layout change with setxkbmap
# setxkbmap -option 'grp:shifts_toggle' -layout us,ru
# setxkbmap -option 'ctrl:nocaps' &

# Yandex disk autostart
yandex-disk start & disown

# Syncthing synchronisation
syncthing & disown

# Clipboard menu daemon
clipmenud & disown

# Swiching audio devices after connect
pactl load-module module-switch-on-connect & disown

# Network manager applet
nm-applet & disown

# Volume manager applet
pasystray & disown

# Notifications
dunst & disown

# player contol
playerctld daemon & disown

# Emacs server daemon
bash /home/georgiy/.local/bin/rofi_scripts/emacs_daemon & disown

# Unclutter - hide cursor
unclutter & disown

# Startup monitor change
sleep 1
#intern=eDP
extern=HDMI-A-0
hdmi_sink="alsa_output.pci-0000_04_00.1.hdmi-stereo"
if xrandr | grep "$extern disconnected"; then
    xrandr --output eDP --mode 1920x1080
else
    xrandr --output HDMI-A-0 --primary --mode 1920x1080 --left-of eDP --mode 1920x1080
    sleep 1
    pactl set-default-sink $hdmi_sink
fi
