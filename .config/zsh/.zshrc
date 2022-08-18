#!/bin/sh
export ZDOTDIR=$HOME/.config/zsh

# Lines configured by zsh-newuser-install
HISTFILE=~/.config/zsh/.histfile
HISTSIZE=1000000
SAVEHIST=1000000
setopt autocd
unsetopt beep
bindkey -v
export KEYTIMEOUT=1
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/georgiy/.config/zsh/.zshrc'
# End of lines added by compinstall

# pfetch at the start
pfetch

# From https://github.com/Mach-OS/Machfiles https://www.youtube.com/watch?v=bTLYiNvRIVI

setopt extendedglob nomatch menucomplete
setopt interactive_comments
stty stop undef		# Disable ctrl-s to freeze terminal.
zle_highlight=('paste:none')

# completions
autoload -Uz compinit && compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'

# zstyle ':completion::complete:lsof:*' menu yes select
zmodload zsh/complist

_comp_options+=(globdots)		# Include hidden files.

autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

# Colors
autoload -Uz colors && colors

# Useful Functions
source "$ZDOTDIR/zsh-functions"

# Normal files to source
zsh_add_file "zsh-exports"
# zsh_add_file "zsh-vim-mode"
zsh_add_file "zsh-aliases"
zsh_add_file "zsh-prompt"

# Plugins
zsh_add_plugin "zsh-autosuggestions"
zsh_add_plugin "zsh-syntax-highlighting"

zsh_add_plugin "zsh-history-substring-search"
# Bindkeys for "zsh-history-substring-search"
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

zsh_add_plugin "zsh-auto-notify"
# Auto notify options
AUTO_NOTIFY_IGNORE+=("bashtop")

zsh_add_plugin "zsh-you-should-use"