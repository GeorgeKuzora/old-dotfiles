# Language managment variables /etc/enviroments
typeset -U PATH path
export GTK_IM_MODULE='fcitx'
export QT_IM_MODULE='fcitx'
export SDL_IM_MODULE='fcitx'
export XMODIFIERS='@im=fcitx'

# Clipmenu variables /etc/enviroments
export CM_SELECTIONS='clipboard'
export CM_DEBUG=0
export CM_OUTPUT_CLIP=0
export CM_MAX_CLIPS=10
export CM_LAUNCHER='rofi'

# Добавление директорий в PATH
PATH="$PATH:$HOME/.emacs.d/bin"
PATH="$PATH:$HOME/.local/bin"
PATH="$PATH:$HOME/.local/bin/rofi_scripts"
export PATH

# Look manpage via nvim
export MANPAGER='nvim +Man!'
export MANWIDTH=999

# Default Apps
export EDITOR="nvim" #"emacsclient -c -a 'emacs'"
export READER="atril"
export VISUAL="nvim" #"emacsclient -c -a 'emacs'"
export TERMINAL="alacritty"
export BROWSER="brave"
export VIDEO="mpv"
export IMAGE="qimgv"
# export COLORTERM="truecolor" # alacritty is 256 color terminal
export OPENER="xdg-open"
export PAGER="less"
export WM="qtile"
export SHELL="zsh"
# Home folder control
export XCURSOR_PATH=/usr/share/icons:${XDG_DATA_HOME}/icons
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export SQLITE_HISTORY="$XDG_CACHE_HOME"/sqlite_history
export ERRFILE="$XDG_CACHE_HOME/X11/xsession-errors"
