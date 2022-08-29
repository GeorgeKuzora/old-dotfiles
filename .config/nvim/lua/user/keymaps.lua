local g   = vim.g
-- KEYBINDINGS --
g.mapleader = ' '
g.maplocalleader = ' '
vim.keymap.set('i', 'ii', '<ESC>')
-- Better nav for omnicomplete
vim.keymap.set('i', '<C-j>', '<C-n>')
vim.keymap.set('i', '<C-k>', '<C-p>')
-- Use alt + hjkl to resize windows
vim.keymap.set('n', '<M-j>', ':resize -2<CR>')
vim.keymap.set('n', '<M-k>', ':resize +2<CR>')
vim.keymap.set('n', '<M-h>', ':vertical resize -2<CR>')
vim.keymap.set('n', '<M-l>', ':vertical resize +2<CR>')
-- TAB in general mode will move to text buffer
vim.keymap.set('n', '<TAB>', ':bnext<CR>')
vim.keymap.set('n', '<S-TAB>', ':bprevious<CR>')
-- Alternate way to save
vim.keymap.set('n', '<C-s>', ':w<CR>')
-- Alternate way to quit
vim.keymap.set('n', '<C-Q>', ':wq!<CR>')
-- Use control-c instead of escape
vim.keymap.set('n', '<C-c>', '<Esc>')

-- <TAB>: completion.
vim.keymap.set('i', '<Tab>', function()
    return vim.fn.pumvisible() == 1 and '<C-N>' or '<Tab>'
end, {expr = true})

-- Better tabbing
vim.keymap.set('v', '<', '<gv')
vim.keymap.set('v', '>', '>gv')
-- Better window navigation
vim.keymap.set('n', '<C-h>', '<C-w>h')
vim.keymap.set('n', '<C-j>', '<C-w>j')
vim.keymap.set('n', '<C-k>', '<C-w>k')
vim.keymap.set('n', '<C-l>', '<C-w>l')
-- Create empty line without insert mode
vim.keymap.set('n', '<Leader>o', 'o<Esc>')
vim.keymap.set('n', '<Leader>O', 'O<Esc>')
-- escape highlight search
vim.keymap.set('n', '<esc><esc>', ':noh<return><esc>')
-- Breaking undo in insert when delete
vim.keymap.set('i', '<c-u>', '<c-g>u<c-u>')
vim.keymap.set('i', '<c-w>', '<c-g>u<c-w>')
-- Quick registers look
vim.keymap.set('n', '<Leader>,', ':registers<CR>')
-- Quick buffers look
vim.keymap.set('n', '<Leader>.', ':buffers<CR>')
-- Quick buffer delete
vim.keymap.set('n', '<Leader>k', ':bdelete')
-- Nvimtree
vim.keymap.set("n", "<leader>e", ":NvimTreeToggle<cr>")


-- NOT IN USE
--  nnoremap <leader>ff <cmd>Telescope find_files<cr>
--  nnoremap <leader>fg <cmd>Telescope live_grep<cr>
--  nnoremap <leader>fb <cmd>Telescope buffers<cr>
--  nnoremap <leader>fh <cmd>Telescope help_tags<cr>