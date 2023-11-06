STYLE = {
    'None': 0,
    'Bold': 1,
    'Dark': 2,
    'Italic': 3,
    'Underline': 4,
    'Blink': 5,
    'Negative': 7,
    'Risk': 9
}

COLORS = {
    'Black': 0,
    'Red': 1,
    'Green': 2,
    'Orange': 3,
    'Yellow': 63,
    'Blue': 4,
    'Purple': 5,
    'Cyan': 6,
    'Gray': 7,
    'None': 9
}

COLORS_LIST = [color for color in COLORS.keys()]
COLORS_LIST.remove('Black')
COLORS_LIST.remove('Gray')

RAINBOW = ('Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple')


# {'corner': '', 'line': '', 'column_1': '', 'column_2': '', 'colors': ('', '')}
BOXES = (
    {'corner': '+', 'line': '~', 'column_1': '|',
        'column_2': '|', 'colors': ('Green', 'Cyan')},
    {'corner': 'X', 'line': '=', 'column_1': '\\',
        'column_2': '/', 'colors': ('Green', 'Red')},
    {'corner': '*', 'line': ':', 'column_1': '{',
        'column_2': '}    ', 'colors': ('Red', 'Purple')},
    {'corner': 'x', 'line': 'x', 'column_1': 'X', 'column_2': 'X', 'colors': ('Red', 'None')}
)
