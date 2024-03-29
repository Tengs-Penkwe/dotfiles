# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

MYTERM = "kitty"

BLACK = '#29414f'
RED = '#ec5f67'
GREEN = '#99c794'
YELLOW = '#fac863'
BLUE = '#6699cc'
MAGENTA = '#c594c5'
CYAN = '#5fb3b3'
WHITE = '#ffffff'

colours = [
    ["#1f2329", "#1f2329"],  # Background
    ["#dcdcdc", "#dcdcdc"],  # Foreground
    ["#535965", "#535965"],  # Grey Colour
    ["#e55561", "#e55561"],
    ["#8ebd6b", "#8ebd6b"],
    ["#e2b86b", "#e2b86b"],
    ["#4fa6ed", "#4fa6ed"],
    ["#bf68d9", "#bf68d9"],
    ["#48b0bd", "#48b0bd"],
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Application menu"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Rofi lunch"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Quit active window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key( [mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"), desc="Decrease the volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"), desc="Increase the volume"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d intel_backlight set 10%+"), desc="Increase the brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d intel_backlight set 10%-"), desc="Decrease the brightness"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": GREEN,
    "border_normal": BLACK
}

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# DEFAULT WIDGET SETTINGS
widget_defaults = dict(
    font="SauceCodePro Nerd Font",
    fontsize=22,
    padding=2,
)
extension_defaults = widget_defaults.copy()

widgets = [
    widget.Sep(
        foreground=colours[0],
        linewidth=4),
    widget.Image(
        filename="~/.config/qtile/run.png",
        mouse_callbacks=({
            "Button1": lambda: qtile.cmd_spawn("rofi -show drun"),
            "Button3": lambda: qtile.cmd_spawn("rofi -show run"),
        }),
        scale=True),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.GroupBox(
        active=colours[4],
        inactive=colours[2],
        other_current_screen_border=colours[5],
        other_screen_border=colours[2],
        this_current_screen_border=colours[7],
        this_screen_border=colours[2],
        urgent_border=colours[3],
        urgent_text=colours[3],
        disable_drag=True,
        highlight_method="text",
        invert_mouse_wheel=True,
        margin=2,
        padding=0,
        rounded=True,
        urgent_alert_method="text"),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.CurrentLayout(
        foreground=colours[7],
        font="SourceCodePro Bold"),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.Systray(
        icon_size=22,
        padding=4),
    widget.Cmus(
        noplay_color=colours[2],
        play_color=colours[1]),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.WindowName(
        max_chars=75),
    widget.Backlight(
        foreground=colours[5],
        foreground_alert=colours[3],
        format="🔆{percent:2.0%}",
        backlight_name="intel_backlight", # ls /sys/class/backlight/
        change_command="brightnessctl -d intel_backlight set {0}%",
        step=10),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.CPU(
        foreground=colours[3],
        format=" {load_percent}%",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(MYTERM + " -e bpytop"),
        },
        update_interval=1.0),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.Memory(
        foreground=colours[4],
        format=" {MemUsed:.0f} MB",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(MYTERM + " -e bpytop"),
        },
        update_interval=1.0),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.Net(
        foreground=colours[6],
        format='🌐{up} {down} ',
        # mouse_callbacks={
        #     "Button1": lambda: qtile.cmd_spawn(MYTERM + " -e bpytop"),
        # },
        #     interface = "enp1s0"),
        update_interval=1.0),
    widget.Wlan(
        foreground=colours[6],
        format='🛜{essid}, {percent:2.0%}',
        update_interval=1.0
        ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.CheckUpdates(
        colour_have_updates=colours[5],
        colour_no_updates=colours[5],
        custom_command="checkupdates",
        # custom_command="dnf updateinfo -q --list",
        display_format="📥 {updates} Updates",
        no_update_string="📦 Up to date!",
        mouse_callbacks=({
            "Button1": lambda: qtile.cmd_spawn(os.path.expanduser(
                "~/.config/scripts/update_system.sh")),
            "Button3": lambda: qtile.cmd_spawn(os.path.expanduser(
                "~/.config/scripts/check_updates.sh")),
        }),
        update_interval=900),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.PulseVolume(
        foreground=colours[6],
        fmt="🔊 {}",
        update_interval=0.1,
        volume_app="pavucontrol",
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        step=5,
        ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.Battery(
        foreground=colours[7],
        format="{char} {percent:2.0%}",
        charge_char="  ",
        discharge_char=" ",
        empty_char="🪫 ",
        full_char="🔋 ",
        unknown_char=" ",
        low_foreground=colours[3],
        low_percentage=0.15,
        show_short_text=False,
        notify_below=15),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10),
    widget.Clock(
        foreground=colours[8],
        format="📅 %a %b %d %I:%M %P  "),
    # widget.StockTicker(
    #     apikey="AESKWL5CJVHHJKR5",
    #     url="https://www.alphavantage.co/query?"),
]

def status_bar(widget_list):
  return bar.Bar(widget_list, 32, opacity=0.9)

screens = [
    Screen(
        top=status_bar(widgets),
        wallpaper="~/Wallpapers/Andromeda Galaxy.jpg",
        wallpaper_mode="stretch",
        ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
