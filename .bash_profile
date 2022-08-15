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
export EDITOR="nvim"
export READER="zathura"
export VISUAL="nvim"
export TERMINAL="alacritty"
export BROWSER="brave"
export VIDEO="mpv"
export IMAGE="nsxiv"
# export COLORTERM="truecolor" # alacritty is 256 color terminal
export OPENER="xdg-open"
export PAGER="less"
export WM="qtile"


# Добавление директорий в PATH
PATH="$PATH:$HOME/.local/bin"
export PATH