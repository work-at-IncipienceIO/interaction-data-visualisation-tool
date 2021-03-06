# HISTOGRAM - Clicks Per Min

import plotly.graph_objs as go
import plotly.offline as offline

import pandas as pd
import sys

# Gets the first sys arg from app.py. Tells script where the input file is.
df = pd.read_csv(sys.argv[1])

# Get data we want to measure with histogram
trace_all = go.Histogram(x=df['clicks_per_minute'],
                         opacity=0.75,
                         name='Participants')

# DATA to be plotted
data = [trace_all]

# LAYOUT to be used
layout = go.Layout(
    title=sys.argv[2] + ' - Histogram of Total Clicks Per Minute',
    xaxis=dict(
        title='Clicks Per Minute'
    ),
    yaxis=dict(
        title='Participant Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)

# Rename plot
filename = sys.argv[2] + '_histogram_clicks_per_minute.html'

# Sets filepath for plot to be saved to
file_path = 'static/output//' + sys.argv[2] + '/stats//' + filename

# TEMPLATE - Plot saved in template folder to be displayed on web
offline.plot({'data': data, 'layout': layout}, validate=False,
             filename='templates//idvt_data_histogram_clicks_per_minute.html', auto_open=False)

# STATIC - Plot saved in static to be retrieved later
offline.plot({'data': data, 'layout': layout}, validate=False, filename=file_path,
             auto_open=False)
