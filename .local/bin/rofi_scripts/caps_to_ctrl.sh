#!/usr/bin/env sh

# Keyboad layout change with xmodmap
xmodmap ~/.Xmodmap & disown

# Keyboad layout change with setxkbmap
# setxkbmap -option 'ctrl:nocaps' &
