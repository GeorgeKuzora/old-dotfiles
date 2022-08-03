import os
import subprocess
from libqtile import qtile, bar, layout, widget, hook
from libqtile.lazy import lazy
from libqtile.config import Key, Group, Match, Screen, Click, Drag
from libqtile.command import lazy

# KEYMAPPING

mod = "mod4" # My mod key of choice - windows key
terminal = "alacritty" # My browser of choice
myBrowser = "brave" # My browser of choice
myFilebrowser = "pcmanfm" # My filemanager of choice
myCode = 'code' # My text editor of choice

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
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

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        # lazy.layout.grow_left(),
        # desc="Grow window to the left"
        ),
    Key([mod, "control"],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        # lazy.layout.grow_right(),
        # desc="Grow window to the right"
        ),
    # Key([mod, "control"],
    #     "j",
    #     lazy.layout.grow_down(),
    #     desc="Grow window down"),
    # Key([mod, "control"],
    #     "k",
    #     lazy.layout.grow_up(),
    #     desc="Grow window up"),
    Key([mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod],
        "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
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

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
   
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    
    # Power managment commands
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')), desc="Shutdown Qtile"),
    
    
    # Essenttial apps spawn commands
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod], "period", lazy.spawn("rofi -show emoji"), desc="spawn rofi emoji panel"),
    Key([mod], "comma", lazy.spawn("clipmenu"), desc="spawn clipboard menu"),
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
    Key([mod], "c",
        lazy.spawn(myCode),
        desc='My code editor'
        ),
    Key([mod], "o",
        lazy.spawn("obsidian"),
        desc='My Obsidian'
        ),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([], "Print",
        lazy.spawn("flameshot gui"),
        desc='Take screenshot'
        ),

    # Switch focus of monitors
    Key([mod], "slash",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),

    # Volume commands
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    # Brithness commands
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 20+"),
        desc='Function Key'
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 20-"),
        desc='Function Key'),
]

# GROUPS

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "control"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# COLOUR SCHEME
# Gruvbox like scheme
# colors = [["#282828", "#282828"],#0 Very Dark
#           ["#32302f", "#32302f"],#1 Dark
#           ["#ebdbb2", "#ebdbb2"],#2 Pale yellow
#           ["#ff6c6b", "#ff6c6b"],#3 Rose
#           ["#b8bb26", "#b8bb26"],#4 green-yellow
#           ["#fabd2f", "#fabd2f"],#5 oranje
#           ["#b16286", "#b16286"],#6 magnete
#           ["#458588", "#458588"],#7 blue-green
#           ["#3c3836", "#3c3836"],#8 dark brown
#           ["#00000000", "#00000000"]]#9
# Nord scheme
colors = [["#2E3440", "#2E3440"],#0 Polar Night 1
          ["#3B4252", "#3B4252"],#1 Polar Night 2
          ["#434C5E", "#434C5E"],#2 Polar Night 3
          ["#4C566A", "#4C566A"],#3 Polar Night 4
          ["#D8DEE9", "#D8DEE9"],#4 Snow Storm 1
          ["#E5E9F0", "#E5E9F0"],#5 Snow Storm 2
          ["#ECEFF4", "#ECEFF4"],#6 Snow Storm 3
          ["#8FBCBB", "#8FBCBB"],#7 Frost 1 greenish
          ["#88C0D0", "#88C0D0"],#8 Frost 2 light blue
          ["#81A1C1", "#81A1C1"],#9 Frost 3 blue
          ["#5E81AC", "#5E81AC"],#10 Frost 4 dark blue
          ["#BF616A", "#BF616A"],#11 Aurora 1 red
          ["#D08770", "#D08770"],#12 Aurora 2 orange
          ["#EBCB8B", "#EBCB8B"],#13 Aurora 3 yellow
          ["#A3BE8C", "#A3BE8C"],#14 Aurora 4 green
          ["#B48EAD", "#B48EAD"],#15 Aurora 5 purpur
          ["#00000000", "#00000000"]]#16 Transparent
# LAYOUTS

layout_theme = {"border_width": 2,
                "margin": [4, 2, 0, 4],
                "border_focus": colors[7][0], #2 Pale yellow
                "border_normal": colors[2][0] #7 blue-green
                }
MonadTall_theme = {"border_width": 2,
                   "margin": 4,
                   "border_focus": colors[7][0], #2 Pale yellow
                   "border_normal": colors[2][0] #7 blue-green
                   }

layouts = [
    layout.MonadTall(**MonadTall_theme,),
    layout.Stack(**layout_theme, num_stacks=2,),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(**layout_theme, border_focus_stack='#d75f5f'),
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
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

# WIDGETS

widget_defaults = dict(
                    font='JetBrainsMono Nerd Font Bold',
                    fontsize=14,
                    # padding=2,
                    # background=colors[2]
                    )

extension_defaults = widget_defaults.copy()
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    foreground=colors[2],
    background=colors[0],
    fmt='Vol:{} ',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
wid_font = 13
# SCREENS

screens = [
     Screen(
         top=bar.Bar(
            [   
                widget.Sep(padding=10,
                           linewidth=0,
                           foreground=colors[1],
                           background=colors[1]),
                widget.TextBox(
                    text='❆',
                    font="Font Awesome 6 Free",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))},
                    background=colors[1],
                    foreground=colors[6],
                    padding=4,
                    fontsize=28,
                ),
                # widget.Image(filename='~/.config/qtile/icons/python-white.png',
                #             margin=0,
                #             background=colors[5],
                #             foreground=colors[5],
                #             mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))}
                #              ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[2],
                    foreground=colors[1],
                    padding=0,
                    fontsize=30,
                ),
                widget.Sep(padding=8,
                           linewidth=0,
                           background=colors[2],
                           foreground=colors[2],), 
                widget.GroupBox(
                                font="JetBrainsMonoMedium Nerd Font Mono", # "Font Awesome 6 Free",
                                fontsize=14,
                                spacing=8,
                                margin_y=3,
                                margin_x=0,
                                padding_y=5,
                                padding_x=1,
                                borderwidth=1,
                                active=colors[6],
                                inactive=colors[9],
                                rounded=False,
                                highlight_color=colors[3],
                                highlight_method="line",
                                this_current_screen_border=colors[9],
                                this_screen_border=colors[13],
                                other_current_screen_border=colors[9],
                                other_screen_border=colors[13],
                                foreground=colors[2],
                                background=colors[2],
                ),
                widget.TextBox(
                        text = '',
                        font="JetBrainsMonoMedium Nerd Font Mono",
                        background=colors[3],
                        foreground=colors[2],
                        padding=0,
                        fontsize=30,
                        ),
                widget.CurrentLayout(
                    fmt=' {}',
                    foreground=colors[6],
                    background=colors[3],
                    padding=5,
                    fontsize=wid_font,
                ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[10],
                    foreground=colors[3],
                    padding=0,
                    fontsize=30,
                ),    
                widget.Prompt(fontsize=wid_font,),
                widget.Chord(
                    fontsize=wid_font,
                    chords_colors={
                        'launch': (colors[6]),
                    },
                    name_transform=lambda name: name.upper(),
                 ),
                widget.WindowName(
                    foreground=colors[6],
                    fmt='{}',
                    background=colors[10],
                    padding=8,
                    max_chars=100,
                    width=665,
                    fontsize=wid_font,
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=0,
                    foreground=colors[10],
                    background=colors[10]
                ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[9],
                    foreground=colors[10],
                    padding=0,
                    fontsize=37
                ),
                widget.Spacer(
                    background=colors[9]
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[9],
                    background=colors[9]
                ),
                # widget.Net(
                #          interface = "wlan0",
                #          format = 'Net: {down} ↓↑ {up}',
                #          foreground = colors[2],
                #          background = colors[0],
                #         ),
                widget.Systray(
                    # icon_size = 20,
                    foreground=colors[0],
                    background=colors[9],
                    fontsize=wid_font,
                    padding=8
                    ),
                widget.CPU(
                        foreground = colors[0],
                        background=colors[9],
                        fontsize=wid_font,
                        threshold = 90,
                        fmt = '{}',
                        padding = 5,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                        ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[9],
                    foreground=colors[8],
                    padding=0,
                    fontsize=37
                    ),
                widget.Memory(
                        foreground = colors[0],
                        background = colors[8],
                        fontsize=wid_font,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                        fmt = 'Mem:{}',
                        format='{MemUsed:.1f}{mm}',
                        measure_mem='G',
                        ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[8],
                    foreground=colors[7],
                    padding=0,
                    fontsize=30
                ),
                widget.Volume(
                    foreground=colors[0],
                    background=colors[7],
                    fontsize=wid_font,
                    fmt='Vol:{} ',
                    padding=5,
                    mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[7],
                    foreground=colors[4],
                    padding=0,
                    fontsize=30
                    ),
                widget.Battery(
                     foreground=colors[0],
                     background=colors[4],
                     fontsize=wid_font,
                     format='{percent:2.0%}',
                     padding=2
                        ),
                widget.TextBox(
                    text='',
                    font="JetBrainsMonoMedium Nerd Font Mono",
                    background=colors[4],
                    foreground=colors[6],
                    padding=0,
                    fontsize=30
                ),
                widget.Clock(format='%d-%m %a %H:%M',
                             foreground=colors[0],
                             background=colors[6],
                             fontsize=wid_font,
                             padding=2,
                             ),
                widget.Sep(padding=10,
                           linewidth=0,
                           foreground=colors[6],
                           background=colors[6]),
            ],
            28,  # height in px
            background=colors[0],  # background color
            margin=[4, 4, 0, 4],
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
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
widget_defaults = dict(
        font='Cascadia Code',
        fontsize=13,
        padding=3
)

# HOOKS

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])