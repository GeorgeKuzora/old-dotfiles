local status_ok, configs = pcall(require, "nvim-treesitter.configs")
if not status_ok then
  return
end
configs.setup {
  ensure_installed = "all",
  sync_install = false,
  ignore_install = { "" }, -- List of parsers to ignore installing
  highlight = {
    enable = true, -- false will disable the whole extension
    disable = { "" }, -- list of language that will be disabled
    additional_vim_regex_highlighting = true,
  },
  indent = { enable = true, disable = { "yaml", "python" } },
  rainbow = {
    enable = true,
    -- disable = { "jsx", "cpp" }, list of languages you want to disable the plugin for
    extended_mode = true, -- Also highlight non-bracket delimiters like html tags, boolean or table: lang -> boolean
    max_file_lines = nil, -- Do not enable for files with more than n lines, int
    colors = {'#bf616a',
              '#d08770',
              '#ebcb8b',
              '#a3be8c',
              '#81a1c1',
              '#5e81ac',
              '#b48ead'}, -- table of hex strings
--    termcolors = {'#bf616a',
--              '#d08770',
--              '#ebcb8b',
--              '#a3be8c',
--              '#b48ead'}, -- table of colour name strings
  },
  autopairs = {
	enable = true,
	},
  context_commentstring = {
    enable = true,
    enable_autocmd = false,
  },
}
