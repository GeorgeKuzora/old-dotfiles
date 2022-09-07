local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath("data") .. "/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
	PACKER_BOOTSTRAP = fn.system({
		"git",
		"clone",
		"--depth",
		"1",
		"https://github.com/wbthomason/packer.nvim",
		install_path,
	})
	print("Installing packer close and reopen Neovim...")
	vim.cmd([[packadd packer.nvim]])
end

-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerSync
  augroup end
]])

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
	return
end

-- Have packer use a popup window
packer.init({
	display = {
		open_fn = function()
			return require("packer.util").float({ border = "rounded" })
		end,
	},
})

-- PLUGINS --
-- Install your plugins here
return packer.startup(function(use)
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    -- Possible dependenses for other plugins
    use 'nvim-lua/popup.nvim' -- An implementation of ht Popup API vim in Neovim
    use 'nvim-lua/plenary.nvim' -- Useful lua fenctions used by lots of plugins
	use "kyazdani42/nvim-web-devicons" -- Required by lualine
	use "moll/vim-bbye" -- Required by Bufferline config

    -- Nord theme
    use 'arcticicestudio/nord-vim'

    -- Treesitter
    use {
    	"nvim-treesitter/nvim-treesitter",
    	run = ":TSUpdate",
    	}
    use "p00f/nvim-ts-rainbow"

    -- Status line
    use {
    'nvim-lualine/lualine.nvim',
    requires = { 'kyazdani42/nvim-web-devicons', opt = true }
    }

    -- Autopairs
    use "windwp/nvim-autopairs"

	-- Buffer line
	-- use "akinsho/bufferline.nvim"

	-- Nvim-tree file explower
	use "kyazdani42/nvim-tree.lua"

    -- Comments
    use "numToStr/Comment.nvim"
    use "JoosepAlviste/nvim-ts-context-commentstring"

    -- Terminal
    use "akinsho/toggleterm.nvim"

    -- Project
    use "ahmedkhalf/project.nvim"

    --Impatient
    use 'lewis6991/impatient.nvim'

    -- Indent line
    use "lukas-reineke/indent-blankline.nvim"

    -- Alpha greetter
    use 'goolord/alpha-nvim'
    use "antoinemadec/FixCursorHold.nvim" -- This is needed to fix lsp doc highlight

    -- Whichkey
    use "folke/which-key.nvim"

    -- cmp plugins
    use "hrsh7th/nvim-cmp" -- The completion plugin
    use "hrsh7th/cmp-buffer" -- buffer completions
    use "hrsh7th/cmp-path" -- path completions
    use "hrsh7th/cmp-cmdline" -- cmdline completions
    use "saadparwaiz1/cmp_luasnip" -- snippet completions
    use "hrsh7th/cmp-nvim-lsp"
    use "hrsh7th/cmp-nvim-lua"

    -- snippets
    use "L3MON4D3/LuaSnip" --snippet engine
    use "rafamadriz/friendly-snippets" -- a bunch of snippets to use

    -- LSP
    use "neovim/nvim-lspconfig" -- enable LSP
    use "williamboman/nvim-lsp-installer" -- simple to use language server installer
    use "jose-elias-alvarez/null-ls.nvim" -- for formatters and linters

    -- Telescope
    use "nvim-telescope/telescope.nvim"
    use 'nvim-telescope/telescope-media-files.nvim'

    -- Git
    use "lewis6991/gitsigns.nvim"

	-- Automatically set up your configuration after cloning packer.nvim
	-- Put this at the end after all plugins
    if PACKER_BOOTSTRAP then
		require("packer").sync()
	end
end)
