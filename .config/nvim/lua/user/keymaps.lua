local g   = vim.g
-- KEYBINDINGS --
g.mapleader = ' '
g.maplocalleader = ' '
vim.keymap.set('i', 'ii', '<ESC>')
-- Better nav for omnicomplete
vim.keymap.set('i', '<C-j>', '<C-n>')
vim.keymap.set('i', '<C-k>', '<C-p>')
-- Use alt + arrows to resize windows
vim.keymap.set('n', '<M-Up>', ':resize -2<CR>')
vim.keymap.set('n', '<M-Down>', ':resize +2<CR>')
vim.keymap.set('n', '<M-Left>', ':vertical resize -2<CR>')
vim.keymap.set('n', '<M-Right>', ':vertical resize +2<CR>')
-- TAB in general mode will move to text buffer
-- vim.keymap.set('n', '<leader>bn', ':bnext<CR>')
-- vim.keymap.set('n', '<leader>bp', ':bprevious<CR>')
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
-- vim.keymap.set('n', '<Leader>bk', ':bdelete<CR>')
-- Quick marks look
vim.keymap.set('n', '<Leader>m', ':marks<CR>')
-- Nvimtree значение по умолчанию
-- vim.keymap.set("n", "<leader>e", ":NvimTreeToggle<CR>")
-- Move text up and down
vim.keymap.set("n", "<M-j>", "<Esc>:m .+1<CR>==")
vim.keymap.set("n", "<M-k>", "<Esc>:m .-2<CR>==")
-- Visual --
-- Move text up and down
vim.keymap.set("v", "<M-j>", ":m .+1<CR>==")
vim.keymap.set("v", "<M-k>", ":m .-2<CR>==")
vim.keymap.set("v", "p", '"_dP')
-- Visual Block --
-- Move text up and down
vim.keymap.set("x", "<M-j>", ":move '>+1<CR>gv-gv")
vim.keymap.set("x", "<M-k>", ":move '<-2<CR>gv-gv")
-- Telescope
--[[ vim.keymap.set("n", "<leader>ff", "<cmd>lua require'telescope.builtin'.find_files(require('telescope.themes').get_dropdown({ previewer = false }))<cr>") ]]
--[[ vim.keymap.set("n", "<leader>fg", "<cmd>Telescope live_grep<cr>") ]]
vim.keymap.set("n", "<leader>fb", "<cmd>Telescope buffers<cr>")
vim.keymap.set("n", "<leader>fh", "<cmd>Telescope help_tags<cr>")
