-- Config was built using the following config:
-- https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/nvim/init.lua


-- Declaring local variables to reduce amount of typing
local g   = vim.g
local o   = vim.o
local opt = vim.opt
local A   = vim.api

-- GENERAL SETTINGS --
-- highlihting
opt.hlsearch = true         -- With highlight search
opt.ignorecase = true       -- Search ignoring case of letters
opt.smartcase = true        -- Search with ignor case if all small and with case if even one is big
opt.incsearch = true        -- Search incrementaly when you input request
-- indentation
opt.autoindent = true       -- auto indention
opt.smartindent = true      -- smart indention
opt.expandtab = true        -- create spaces from tab
opt.shiftround = true       -- When shifting lines, round the indentation to the nearest multiple of shiftwidth.
opt.shiftwidth = 4          -- When shifting, indent using four spaces.
opt.smarttab = true         -- Insert “tabstop” number of spaces when the “tab” key is pressed.
opt.tabstop = 4             -- Indent using four characters.
opt.softtabstop = 4         -- Indent using four spaces.
-- lines
opt.display = 'lastline'    -- Always try to show a paragraph’s last line.
opt.encoding = 'utf-8'      -- Use an encoding that supports unicode.
opt.fileencoding = 'utf-8'  -- The encoding written to file
opt.wrap = true             -- Enable line wrapping.
opt.linebreak = true        -- Avoid wrapping a line in the middle of a word.
opt.scrolloff = 8           -- The number of screen lines to keep above and below the cursor.
opt.sidescrolloff = 5       -- The number of screen columns to keep to the left and right of the cursor.
opt.syntax = 'enable'       -- Enable syntax higlihting
-- display
opt.number = true           -- Show line numbers on the sidebar.
opt.relativenumber = true   -- Show line number on the current line and relative numbers on all other lines.
opt.laststatus = 2          -- Always display the status bar.
opt.ruler = true            -- Always show cursor position.
opt.wildmenu = true         -- Display command line’s tab complete options as a menu.
opt.tabpagemax = 50         -- Maximum number of tab pages that can be opened from the command line.
opt.errorbells = false      -- Disable beep on errors.
opt.visualbell = true       -- Flash the screen instead of beeping on errors.
opt.title = true            -- set the window’s title, reflecting the file currently being edited.
-- opt.background = dark       -- Use colors that suit a dark background. Do we need it?

-- folding
opt.foldmethod = 'indent'   -- Fold based on indention levels.
opt.foldnestmax = 3         -- Only fold up to three nested levels.
opt.foldenable = false      -- Enable folding by default.
-- undoing
opt.autoread = true            -- Automatically re-read files if unmodified inside Vim.
opt.backspace = {'indent', 'eol', 'start'}  -- Allow backspacing over indention, line breaks and insertion start.
opt.dir = '~/.cache/nvim '  -- Directory to store backup files.
opt.undodir = '~/.cache/nvim/undodir'   -- Set undofiles dir
opt.undofile = true         -- Set undofiles
o.swapfile = false          -- Set swapfile
opt.confirm = true          -- Display a confirmation dialog when closing an unsaved file.
opt.formatoptions:append('j')   -- Delete comment characters when joining lines.
opt.hidden = true           -- Hide files in the background instead of closing them.
opt.history = 1000          -- Increase the undo limit.
opt.modeline = false        -- Ignore file’s mode lines; use vimrc configurations instead.
opt.swapfile = false        -- Disable swap files.
opt.nrformats:remove('octal')   -- Interpret octal as decimal when incrementing numbers.
opt.shell = '/usr/bin/zsh'
-- opt.spell = true            --Enable spellchecking.
opt.wildignore = {'.pyc', '.swp'}   -- Ignore files matching these patterns when opening files based on a glob pattern.
-- Colored colum
opt.colorcolumn = '80'      -- colored line on 80 charachters
vim.cmd[[highlight ColorColumn ctermbg=0 guibg=lightgrey]]  -- Set colors of colored line

-- windows
opt.pumheight = 10          -- Makes popup menu smaller
opt.cmdheight = 2           -- More space for displaying messages
opt.iskeyword:append('-')   -- treat dash separated words as a word text object
opt.mouse = 'a'             -- Enable your mouse
opt.splitbelow = true       -- Horizontal splits will automatically be below
opt.splitright =true        -- Vertical splits will automatically be to the right
opt.termguicolors = false   -- Support true colors
opt.conceallevel = 0        -- So that I can see `` in markdown files
--opt.cursorline = true        -- Enable highlighting of the current line
opt.showtabline = 2         -- Always show tabs
-- opt.noshowmode = true       -- We don't need to see things like -- INSERT -- anymore
o.backup = false            -- This is recommended by coc
o.writebackup = false       -- This is recommended by coc
opt.formatoptions:remove('cro') -- Stop newline continution of comments
-- automation
opt.clipboard = {'unnamedplus', 'unnamed'}  -- Copy paste between vim and everything else
opt.autochdir = false       -- Your working directory will always be the same as your working directory
vim.cmd [[au! BufWritePost $MYVIMRC source %]]  -- auto source when writing to init.vm alternatively you can run :source $MYVIMRC
opt.cp = false              -- 'compatible' is not set
vim.cmd [[filetype plugin indent on]]   -- plugins are enabled
vim.cmd [[set grepprg=rg\ --vimgrep\ --smart-case\ --follow]]   -- Better grep command

-- KEYBINDINGS --
g.mapleader = ' '
g.maplocalleader = ' '
vim.keymap.set('i', 'ii', '<ESC>')

vim.cmd [[
" Better nav for omnicomplete
inoremap <expr> <c-j> ("\<C-n>")
inoremap <expr> <c-k> ("\<C-p>")

" Use alt + hjkl to resize windows
nnoremap <M-j>    :resize -2<CR>
nnoremap <M-k>    :resize +2<CR>
nnoremap <M-h>    :vertical resize -2<CR>
nnoremap <M-l>    :vertical resize +2<CR>



" TAB in general mode will move to text buffer
nnoremap <TAB> :bnext<CR>
" SHIFT-TAB will go back
nnoremap <S-TAB> :bprevious<CR>

" Alternate way to save
nnoremap <C-s> :w<CR>
" Alternate way to quit
nnoremap <C-Q> :wq!<CR>
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

" Breaking undo in insert when delete
inoremap <c-u> <c-g>u<c-u>
inoremap <c-w> <c-g>u<c-w>
]]
--  nnoremap <leader>ff <cmd>Telescope find_files<cr>
--  nnoremap <leader>fg <cmd>Telescope live_grep<cr>
--  nnoremap <leader>fb <cmd>Telescope buffers<cr>
--  nnoremap <leader>fh <cmd>Telescope help_tags<cr>