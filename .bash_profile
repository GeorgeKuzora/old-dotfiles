#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
# Language managment variables
typeset -U PATH path
export GTK_IM_MODULE='fcitx'
export QT_IM_MODULE='fcitx'
export SDL_IM_MODULE='fcitx'
export XMODIFIERS='@im=fcitx'

# Clipmenu variables
export CM_SELECTIONS='clipboard'
export CM_DEBUG=0
export CM_OUTPUT_CLIP=0
export CM_MAX_CLIPS=10
export CM_LAUNCHER='rofi'

# Default Apps
export EDITOR="emacsclient -c -a 'emacs'"
export READER="zathura"
export VISUAL="emacsclient -c -a 'emacs'"
export TERMINAL="alacritty"
export BROWSER="brave"
export VIDEO="mpv"
export IMAGE="qimgv"
# export COLORTERM="truecolor" # alacritty is 256 color terminal
export OPENER="xdg-open"
export PAGER="less"
export WM="qtile"
# history file location
export HISTFILE="${XDG_STATE_HOME}"/bash/history
# Добавление директорий в PATH
PATH="$PATH:$HOME/.local/bin"
export PATH
source /home/georgiy/.config/broot/launcher/bash/br

export XCURSOR_PATH=/usr/share/icons:${XDG_DATA_HOME}/icons
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export SQLITE_HISTORY="$XDG_CACHE_HOME"/sqlite_history
export ERRFILE="$XDG_CACHE_HOME/X11/xsession-errors"
