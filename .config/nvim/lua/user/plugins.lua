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
	-- use 'shaunsingh/nord.nvim'
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
	use "akinsho/bufferline.nvim"
	-- Nvim-tree file explower
	use "kyazdani42/nvim-tree.lua"
    -- Comments
    use "numToStr/Comment.nvim"
    use "JoosepAlviste/nvim-ts-context-commentstring"
	-- Automatically set up your configuration after cloning packer.nvim
	-- Put this at the end after all plugins
    if PACKER_BOOTSTRAP then
		require("packer").sync()
	end
end)
