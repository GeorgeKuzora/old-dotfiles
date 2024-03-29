import os
import subprocess
from libqtile import qtile, bar, layout, widget, hook
from libqtile.lazy import lazy
from libqtile.config import Key, Group, Match, Screen, Click, Drag, ScratchPad
from libqtile.config import DropDown


# MY FUNCTIONS


@lazy.function
def rofi_scripts(qtile):
    subprocess.run("selected=$(ls /home/georgiy/.local/bin/rofi_scripts | \
    rofi -dmenu -p 'Run: ')&&bash \
    /home/georgiy/.local/bin/rofi_scripts/$selected", shell=True)


# KEYMAPPING


mod = "mod4"  # My mod key of choice - windows key
terminal = "alacritty"  # My browser of choice
myBrowser = "brave"  # My browser of choice
myFilebrowser = "pcmanfm"  # My filemanager of choice
myEmacs = "emacsclient -c -n -a 'emacs'"  # My text editor of choice
# myCode = "code" # My text editor of choice
keys = [
    # WINDOW MANAGMENT
    # Switch focus between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to the next window"),
    Key([mod, "shift"],
        "space",
        lazy.layout.previous(),
        desc="Move window focus to the previous window"),

    # Move windows
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Grow windows.
    Key([mod, "control"],
        "h",
        lazy.layout.shrink_main(),
        lazy.layout.decrease_ratio(),
        desc="Grow master window to the left"
        ),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_main(),
        lazy.layout.increase_ratio(),
        desc="Grow master window to the right"
        ),
    Key([mod, "control"],
        "j",
        lazy.layout.grow(),
        desc="Grow window down"),
    Key([mod, "control"],
        "k",
        lazy.layout.shrink(),
        desc="Grow window up"),
    Key([mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod, "shift"],
        "n",
        lazy.layout.reset(),
        desc="Reset all window sizes"),
    Key([mod],
        "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    # Toggle fullscreen and floating
    Key([mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # Increase and decrease number of windows in the master stack (Tile)
    Key([mod, "mod1"],
        "h",
        lazy.layout.increase_nmaster(),
        desc='increase number in master pane (Tile)'
        ),
    Key([mod, "mod1"],
        "l",
        lazy.layout.decrease_nmaster(),
        desc='dencrease number in master pane (Tile)'
        ),
    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Svap and flip columns in column layout
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous\
        layout"),


    # Power managment commands
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'
                                                  )), desc="Shutdown Qtile"),

    # Essenttial apps spawn commands
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="spawn rofi run"),
    Key([mod], "e", lazy.spawn("rofi -show drun"), desc="run apps from rofi"),
    Key([mod], "w", lazy.spawn("rofi -show window -window-format '{w} {c} {t}'\
        -theme ~/.config/rofi/configTall.rasi"), desc="run apps from rofi"),
    Key([mod], "t", rofi_scripts, desc="run scripts from rofi"),
    Key(
        [mod],
        "z",
        lazy.spawn(
            "rofi -show file-browser-extended -file-browser-show-hidden -theme\
                ~/.config/rofi/configTall.rasi -file-browser-cmd 'xdg-open'"
        ),
        desc="Rofi find files",
    ),
    Key([mod], "period", lazy.spawn('rofimoji --skin-tone light --action clipboard --prompt "Emoji:"'), desc="spawn rofi\
        emoji panel"),
    Key([mod, "shift"], "period", lazy.spawn('rofimoji --files mathematical_operators --action clipboard --prompt "Math:"'), desc="spawn rofi\
        math symbols panel"),
    Key([mod], "comma", lazy.spawn("clipmenu -p 'Clipboard:' -theme\
        ~/.config/rofi/configTall.rasi"), desc="spawn clipboard menu"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='My browser'
        ),
    Key([mod], "v",
        lazy.spawn(myFilebrowser),
        desc='My GUI file browser'
        ),
    # Key([mod], "c",
    #     lazy.spawn(myCode),
    #     desc='VScode editor'
    #     ),
    Key([mod], "c",
        lazy.spawn(myEmacs),
        desc='Emacs'
        ),
    Key([mod], "x",
        lazy.spawn("obsidian"),
        desc='My Obsidian'
        ),
    Key([mod], "p",
        lazy.spawn("pavucontrol"),
        desc='Pulse audio control'
        ),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([], "Print",
        lazy.spawn("flameshot gui"),
        desc='Take screenshot'
        ),
    Key(
        [mod],
        "d",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle dropdown terminal",),
    Key(
        [mod],
        "s",
        lazy.group["scratchpad"].dropdown_toggle("nvim"),
        desc="Toggle dropdown Learn-Vim nvim",),

    # Switch focus of monitors
    Key([mod], "slash",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),

    # Floating controls
    Key(
        [mod],
        "bracketleft",
        lazy.group.prev_window(),
        lazy.window.bring_to_front(),
        desc="Cycle previous floating window",
    ),
    Key(
        [mod],
        "bracketright",
        lazy.group.next_window(),
        lazy.window.bring_to_front(),
        desc="Cycle next floating windows",
    ),

    # Volume commands
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 3")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 3")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    # Brithness commands
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 20+"),
        desc='Function Key'
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 20-"),
        desc='Function Key'),

    # Player control
    Key(
        [mod],
        "F6",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key([mod], "F8", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key([mod], "F7", lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause audio"),
    Key([mod], "F5", lazy.spawn("playerctl stop"), desc="Stop audio"),

    # KeyboardLayout contol
    # Key(["control"], "backslash",
    #     lazy.widget["keyboardlayout"].next_keyboard(),
    #     desc="Next keyboard layout."),
]


# GROUPS


groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label="ﴬ", matches=[Match(wm_class="anki"),]),
    Group("6", label="龎", matches=[Match(wm_class="com.github.johnfactotum.Foliate"), Match(wm_class="mcomix"), Match(wm_class="goldendict"),]),
    Group("7", label="", matches=[Match(wm_class="telegram-desktop"),]),
    Group("8", label="", matches=[Match(wm_class="zoom"),]),
    Group("9", label="", matches=[Match(wm_class="applicationsyandex-music-nativefier-f7e7ae"),]),
]
for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            actual_key,
            lazy.group[group.name].toscreen(toggle=True),
            desc="Switch to group"),

        # mod1 + shift + letter of group =
        # switch to & move focused window to group
        Key([mod, "shift"],
            actual_key,
            lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group"),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "control"], actual_key, lazy.window.togroup(group.name),
            desc="move focused window to group"),

        # mod1 + arrow = switch to next/previous group
        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        Key([mod], "grave", lazy.screen.toggle_group(),
            desc="Switch to previous group"),
    ])

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "alacritty --class dropdown",
                # opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "nvim",
                terminal + " -e nvim Documents/Code/Learn-Vim",
                # opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
        ],
    )
)


# KEYS HELP
def unicode_map():
    return None

def show_keys(keys):
    """
    print current keybindings in a pretty way for a rofi/dmenu window.
    """
    key_help = ""
    keys_ignored = (
        "XF86AudioMute",  #
        "XF86AudioLowerVolume",  #
        "XF86AudioRaiseVolume",  #
        "XF86AudioPlay",  #
        "XF86AudioNext",  #
        "XF86AudioPrev",  #
        "XF86AudioStop",
    )
    text_replaced = {
        "mod4": "[S]",  #
        "control": "[Ctl]",  #
        "mod1": "[Alt]",  #
        "shift": "[Shf]",  #
        "twosuperior": "²",  #
        "less": "<",  #
        "ampersand": "&",  #
        "Escape": "Esc",  #
        "Return": "Enter",  #
    }
    for k in keys:
        if k.key in keys_ignored:
            continue

        mods = ""
        key = ""
        desc = k.desc.title()
        for m in k.modifiers:
            if m in text_replaced.keys():
                mods += text_replaced[m] + " + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            if k.key in text_replaced.keys():
                key = text_replaced[k.key]
            else:
                key = k.key.title()
        else:
            key = k.key

        key_line = "{:<25} {}".format(mods + key, desc + "\n")
        key_help += key_line

        # debug_print(key_line)  # debug only

    return key_help


# this must be done AFTER all the keys have been defined
keys.extend(
    [Key([mod], "F1", lazy.spawn("sh -c 'echo \"" + show_keys(keys) + "\" | \
        rofi -theme ~/.config/rofi/configTall.rasi -dmenu -p\
        \"Keys:\" -i'"), desc="Print keyboard bindings")])


# COLOUR SCHEME


# Nord scheme
# colors = [["#2E3440", "#2E3440"],  # 0 Polar Night 1
#           ["#3B4252", "#3B4252"],  # 1 Polar Night 2
#           ["#434C5E", "#434C5E"],  # 2 Polar Night 3
#           ["#4C566A", "#4C566A"],  # 3 Polar Night 4
#           ["#D8DEE9", "#D8DEE9"],  # 4 Snow Storm 1
#           ["#E5E9F0", "#E5E9F0"],  # 5 Snow Storm 2
#           ["#ECEFF4", "#ECEFF4"],  # 6 Snow Storm 3
#           ["#8FBCBB", "#8FBCBB"],  # 7 Frost 1 greenish
#           ["#88C0D0", "#88C0D0"],  # 8 Frost 2 light blue
#           ["#81A1C1", "#81A1C1"],  # 9 Frost 3 blue
#           ["#5E81AC", "#5E81AC"],  # 10 Frost 4 dark blue
#           ["#BF616A", "#BF616A"],  # 11 Aurora 1 red
#           ["#D08770", "#D08770"],  # 12 Aurora 2 orange
#           ["#EBCB8B", "#EBCB8B"],  # 13 Aurora 3 yellow
#           ["#A3BE8C", "#A3BE8C"],  # 14 Aurora 4 green
#           ["#B48EAD", "#B48EAD"],  # 15 Aurora 5 purpur
#           ["#3B4252", "#4C566A"],  # 16 Polar Night 2-4 gradient
#           ["#2E3440", "#4C566A"],  # 17 Polar Night 1-4 gradient
#           ["#00000000", "#00000000"]]  # 18 Transparent

# Catppuccin Machiatto
colors = [["#1e2030", "#1e2030"],  # 0 Mantle
          ["#24273a", "#24273a"],  # 1 Base
          ["#363a4f", "#363a4f"],  # 2 Surface0
          ["#494d64", "#494d64"],  # 3 Surface1
          ["#a5adcb", "#a5adcb"],  # 4 Subtext0
          ["#b8c0e0", "#b8c0e0"],  # 5 Subtext1
          # ["#f0c6c6", "#f0c6c6"],  # 6 Flamingo
          ["#cad3f5", "#cad3f5"],  # 6 Text
          ["#8bd5ca", "#8bd5ca"],  # 7 Teal
          ["#91d7e3", "#91d7e3"],  # 8 Sky
          ["#8aadf4", "#8aadf4"],  # 9 Blue
          ["#7dc4e4", "#7dc4e4"],  # 10 Sapphire
          ["#ed8796", "#ed8796"],  # 11 red
          ["#f5a97f", "#f5a97f"],  # 12 peach
          ["#eed49f", "#eed49f"],  # 13 yellow
          ["#a6da95", "#a6da95"],  # 14 green
          ["#c6a0f6", "#c6a0f6"],  # 15 mauve
          ["#24273a", "#363a4f"],  # 16 Base-Surface0 gradient
          ["#1e2030", "#363a4f"],  # 17 Mantle-Surface0 gradient
          ["#00000000", "#00000000"]]  # 18 Transparent

# LAYOUTS


layout_theme = {"border_width": 2,
                "margin": 0,
                "border_focus": colors[13][0],
                "border_normal": colors[2][0]
                }

layouts = [
    layout.MonadTall(**layout_theme, new_client_position='top'),
    layout.Columns(**layout_theme,
                   num_columns=2,
                   border_focus_stack=colors[11][0],
                   border_on_single=colors[13][0]),
    layout.Tile(**layout_theme, shift_windows=True),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(**layout_theme, num_stacks=2,),
    # layout.RatioTile(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

floating_layout = layout.Floating(**layout_theme, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='pavucontrol'),  # pavucontrol
    Match(wm_class='qalculate-gtk'), # qalculate
    Match(wm_class='gnome-calculator'), # calculator
    Match(wm_class='solanum'), # solanum

    Match(wm_class='org.gnome.Characters'),  # Characters
    Match(title='Confirm File Replacing'),  # File replace pcmanfm
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])


# WIDGETS


widget_defaults = dict(
                    font='JetBrainsMono Nerd Font Bold',
                    fontsize=14,
                    padding=2,
                    )

bar_height = 24


# SCREENS


screens = [
     Screen(
         top=bar.Bar(
            [
                widget.Spacer(
                    length=6,
                ),
                widget.Image(
                    filename='~/.config/qtile/icons/nord_python.png',
                    margin_x=0,
                    margin_y=3,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        os.path.expanduser('~/.config/rofi/powermenu.sh'))},
                ),
                widget.Spacer(
                    length=6,
                    ),
                widget.GroupBox(
                                font="JetBrainsMono Nerd Font",
                                fontsize=16,
                                spacing=2,
                                margin_y=3,
                                margin_x=0,
                                padding_y=5,
                                padding_x=2,
                                borderwidth=2,
                                active=colors[6],
                                inactive=colors[9],
                                rounded=False,
                                highlight_color=colors[3],
                                highlight_method="line",
                                this_current_screen_border=colors[13],
                                this_screen_border=colors[9],
                                other_current_screen_border=colors[13],
                                other_screen_border=colors[9],
                                # foreground=colors[16],
                                # background=colors[16],
                                hide_unused=False,
                ),
                widget.Spacer(
                    length=3,
                    ),
                widget.CurrentLayoutIcon(
                    fmt='{}',
                    foreground=colors[6],
                    scale=0.7,
                    padding=0,
                ),
                widget.Spacer(
                    length=3,
                    ),
                widget.CurrentLayout(
                    fmt='{}',
                    foreground=colors[6],
                    font='JetBrainsMono Nerd Font Bold',
                    fontsize=14,
                    padding=0,
                ),
                widget.Spacer(
                    length=12,
                    ),
                widget.Prompt(
                    foreground=colors[6],
                    **widget_defaults,
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': (colors[6]),
                    },
                    name_transform=lambda name: name.upper(),
                    **widget_defaults,
                 ),
                widget.WindowName(
                    fmt='{}',
                    foreground=colors[6],
                    # max_chars=100,
                    width=800,
                    for_current_screen=True,
                    format='{name}{state}',
                    **widget_defaults,
                    ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=20,
                    padding=5
                    ),
                widget.Spacer(
                    length=15,
                    ),
                widget.NetGraph(
                          interface="wlan0",
                          border_color=colors[4],
                          border_width=2,
                          fill_color=colors[4],
                          graph_color=colors[4],
                          line_width=1,
                          start_pos='bottom',
                          margin_x=0,
                          type='line'),
                widget.Spacer(
                    length=15,
                    ),
                # widget.TextBox(
                #         text='',
                #         font="JetBrainsMono Nerd Font",
                #         foreground=colors[11],
                #         padding=0,
                #         fontsize=16
                #         ),
                # widget.Pomodoro(
                #         color_active=colors[14],
                #         color_break=colors[13],
                #         color_inactive=colors[6],
                #         fmt='{}',
                #         prefix_inactive='Pomodoro',
                #         prefix_paused='Pause'
                #         ),
                # widget.KeyboardLayout(
                #     configured_keyboards=['us', 'ru'],
                #     display_map={'us': 'fcitx', 'ru': 'ru'},
                #     fmt='{}',
                #     option='ctrl:nocaps',
                #     foreground=colors[6],
                #     **widget_defaults,
                #     ),
                # widget.Spacer(
                #     length=13,
                #     ),
                widget.TextBox(
                        text='',
                        font="JetBrainsMono Nerd Font",
                        foreground=colors[15],
                        padding=0,
                        fontsize=16
                        ),
                widget.Memory(
                         foreground=colors[15],
                         mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                            terminal + ' -e bashtop')},
                         fmt='{}',
                         format='{MemUsed:.1f}{mm}',
                         measure_mem='G',
                         **widget_defaults
                         ),
                widget.Spacer(
                    length=13,
                    ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMono Nerd Font",
                    foreground=colors[9],
                    padding=0,
                    fontsize=16
                    ),
                widget.CPU(
                        foreground=colors[9],
                        threshold=90,
                        fmt='{}',
                        format='{freq_current}GHz {load_percent}%',
                        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                            terminal + ' -e bashtop')},
                        **widget_defaults
                        ),
                widget.Spacer(
                    length=13,
                    ),
                widget.Battery(
                    format="{char}",
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    unknown_char="",
                    empty_char="",
                    show_short_text=False,
                    foreground=colors[14],
                    fontsize=16,
                    padding=0,
                    font="JetBrainsMono Nerd Font",
                ),
                widget.Battery(
                    format="{percent:2.0%}",
                    show_short_text=False,
                    foreground=colors[14],
                    **widget_defaults
                ),
                widget.Spacer(
                    length=13,
                    ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMono Nerd Font",
                    foreground=colors[13],
                    padding=0,
                    fontsize=16
                    ),
                widget.Clock(
                            fmt='{}',
                            format='%d-%m %a %H:%M',
                            foreground=colors[13],
                            **widget_defaults
                            ),
                widget.Spacer(
                    length=4,
                    ),
            ],
            size=bar_height,  # height in px
            background=colors[17],  # background color
            border_color=colors[3][0],
            border_width=[0, 0, 0, 0],
            margin=0,  # [4, 4, 0, 4],
            opacity=1,
         ), ),
 ]


# MOUSE


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type List
# main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"


# HOOKS


@hook.subscribe.startup_once
def autostart():
    start = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([start])

@hook.subscribe.resume
def wakeup():
    resume = os.path.expanduser('~/.config/qtile/resume.sh')
    subprocess.call([resume])

@hook.subscribe.screens_reconfigured # screen_change
def screen_connect():
    connect = os.path.expanduser('~/.config/qtile/screen_change.sh')
    subprocess.call([connect])
