local colorscheme = "nord"

local status_ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
if not status_ok then
  vim.notify("colorscheme " .. colorscheme .. " not found!")
  return
end

-- -- Colorscheme config in lua
-- vim.g.nord_contrast = false -- Make sidebars and popup menus like nvim-tree and telescope have a different background
-- vim.g.nord_borders = false -- Enable the border between verticaly split windows visable
-- vim.g.nord_disable_background = false -- Disable the setting of background color so that NeoVim can use your terminal background
-- vim.g.nord_cursorline_transparent = false -- Set the cursorline transparent/visible
-- vim.g.nord_enable_sidebar_background = false -- Re-enables the background of the sidebar if you disabled the background of everything
-- vim.g.nord_italic = false -- enables/disables italics
-- vim.g.nord_uniform_diff_background = false -- enables/disables colorful backgrounds when used in diff mode
-- -- Load the colorscheme
-- require('nord').set()