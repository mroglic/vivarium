from bokeh.plotting import figure, show
from bokeh.io import output_file

# Create a new plot with responsive sizing_mode
p = figure(sizing_mode="stretch_both")

# Add glyphs
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

# Save and show
output_file("fullscreen.html")
show(p)