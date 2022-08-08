"GENERAL SETTINGS FOR NEOVIM

" set nohlsearch                  "Wthout highlight search
set hlsearch                  " With highlight search
set ignorecase                  " Search ignoring case of letters
set incsearch                   " Search incrementaly when you input request
set smartcase                   " Search with ignor case if all small and with case if even one is big

set autoindent                  " auto indention
set smartindent                 " smart indention
set expandtab                   " create spaces from tab
set shiftround                  " When shifting lines, round the indentation to the nearest multiple of shiftwidth.
set shiftwidth=4                " When shifting, indent using four spaces.
set smarttab                    " Insert “tabstop” number of spaces when the “tab” key is pressed.
set tabstop=4                   " Indent using four characters.
set softtabstop=4               " Indent using four spaces.

set display+=lastline           " Always try to show a paragraph’s last line.
set encoding=utf-8              " Use an encoding that supports unicode.
set fileencoding=utf-8                  " The encoding written to file
set nowrap                      " Disable line wrapping
set wrap                      " Enable line wrapping.
set linebreak                 " Avoid wrapping a line in the middle of a word.
set scrolloff=8                 " The number of screen lines to keep above and below the cursor.
set sidescrolloff=5             " The number of screen columns to keep to the left and right of the cursor.
syntax enable                   " Enable syntax highlighting.

set number                      " Show line numbers on the sidebar.
set relativenumber              " Show line number on the current line and relative numbers on all other lines.
set laststatus=2                " Always display the status bar.
set ruler                       " Always show cursor position.
set wildmenu                    " Display command line’s tab complete options as a menu.
set tabpagemax=50               " Maximum number of tab pages that can be opened from the command line.
set noerrorbells                " Disable beep on errors.
set visualbell                  " Flash the screen instead of beeping on errors.
set title                       " Set the window’s title, reflecting the file currently being edited.
" set background=dark             "Use colors that suit a dark background. Do we need it?


set foldmethod=indent           " Fold based on indention levels.
set foldnestmax=3               " Only fold up to three nested levels.
set nofoldenable                "  Disable folding by default.

set autoread                                        " Automatically re-read files if unmodified inside Vim.
set backspace=indent,eol,start                      " Allow backspacing over indention, line breaks and insertion start.
set dir=~/.cache/nvim                               " Directory to store backup files.
set dir=~/.cache/nvim                               " Directory to store swap files.
set undodir=~/.config/nvim/undodir                  " set undofiles dir
set undofile                                        " set undofiles
set confirm                                         " Display a confirmation dialog when closing an unsaved file.
set formatoptions+=j                                " Delete comment characters when joining lines.
set hidden                                          " Hide files in the background instead of closing them.
set history=1000                                    " Increase the undo limit.
set nomodeline                                      " Ignore file’s mode lines; use vimrc configurations instead.
set noswapfile                                      " Disable swap files.
set nrformats-=octal                                " Interpret octal as decimal when incrementing numbers.
set shell                                           " The shell used to execute commands.
" set spell                                         -Enable spellchecking.
set wildignore+=.pyc,.swp                           " Ignore files matching these patterns when opening files based on a glob pattern.

set colorcolumn=80                                  " colored line on 80 charachters
highlight ColorColumn ctermbg=0 guibg=lightgrey     " set colors of colored line

set pumheight=10                        " Makes popup menu smaller
set cmdheight=2                         " More space for displaying messages
set iskeyword+=-                      	" treat dash separated words as a word text object
set mouse=a                             " Enable your mouse
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set t_Co=256                            " Support 256 colors
set conceallevel=0                      " So that I can see `` in markdown files
"set cursorline                           Enable highlighting of the current line
set showtabline=2                       " Always show tabs
set noshowmode                          " We don't need to see things like -- INSERT -- anymore
"set nobackup                             This is recommended by coc
"set nowritebackup                        This is recommended by coc
set formatoptions-=cro                  " Stop newline continution of comments
set clipboard=unnamedplus               " Copy paste between vim and everything else
"set autochdir                           - Your working directory will always be the same as your working directory
au! BufWritePost $MYVIMRC source %      " auto source when writing to init.vm alternatively you can run :source $MYVIMRC

set nocp                    " 'compatible' is not set
filetype plugin on          " plugins are enabled

set grepprg=rg\ --vimgrep\ --smart-case\ --follow

"KEYBINDINGS

inoremap ii <ESC>
let mapleader = " "
"  nnoremap <leader>ff <cmd>Telescope find_files<cr>
"  nnoremap <leader>fg <cmd>Telescope live_grep<cr>
"  nnoremap <leader>fb <cmd>Telescope buffers<cr>
"  nnoremap <leader>fh <cmd>Telescope help_tags<cr>



" Better nav for omnicomplete
inoremap <expr> <c-j> ("\<C-n>")
inoremap <expr> <c-k> ("\<C-p>")

" Use alt + hjkl to resize windows
nnoremap <M-j>    :resize -2<CR>
nnoremap <M-k>    :resize +2<CR>
nnoremap <M-h>    :vertical resize -2<CR>
nnoremap <M-l>    :vertical resize +2<CR>

" I hate escape more than anything else
"inoremap jk <Esc>
"inoremap kj <Esc>

" Easy CAPS
inoremap <c-u> <ESC>viwUi
nnoremap <c-u> viwU<Esc>

" TAB in general mode will move to text buffer
nnoremap <TAB> :bnext<CR>
" SHIFT-TAB will go back
nnoremap <S-TAB> :bprevious<CR>

" Alternate way to save
"nnoremap <C-s> :w<CR>
" Alternate way to quit
"nnoremap <C-Q> :wq!<CR>
" Use control-c instead of escape
nnoremap <C-c> <Esc>
" <TAB>: completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

" Better tabbing
vnoremap < <gv
vnoremap > >gv

" Better window navigation
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <Leader>o o<Esc>^Da
nnoremap <Leader>O O<Esc>^Da

" escape highlight search
nnoremap <esc><esc> :noh<return><esc> 
