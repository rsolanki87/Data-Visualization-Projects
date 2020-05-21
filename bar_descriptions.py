import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'awesome-python', 'public-apis']

plot_dicts = [
    {'value': 94426, 'label': 'Description of system-design-primer.'},
    {'value': 82257, 'label': 'Description of awesome-python.'},
    {'value': 81197, 'label': 'Description of public-apis.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')