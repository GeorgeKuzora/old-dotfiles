#!/bin/sh
filepath="/home/georgiy/Documents/Code/Learn-Vim/$(ls /home/georgiy/Documents/Code/Learn-Vim | fzf -e -i --cycle)"
nvim $filepath
