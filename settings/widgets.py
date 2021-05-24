from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='white', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=1, padding=5)


def icon(fg='white', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=60,
        padding=-11
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Mononoki Nerd Font',
            fontsize=14,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color5'],
        colour_have_updates=colors['white'],
        colour_no_updates=colors['white'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color4', 'color5'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='wlp2s0'),

    powerline('color3', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),    

    powerline('color2', 'color3'),

    icon(bg="color2", fontsize=25, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('color1', 'color2'),
 
    widget.Battery(**base(bg='color1'), format='{char} {percent:2.0%} {hour:d}:{min:02d}'),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'Mononoki Nerd Font',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
