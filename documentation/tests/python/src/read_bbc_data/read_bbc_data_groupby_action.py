import plotly.offline as offline
import pandas as pd
import plotly.graph_objs as go


bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

print(bbc_data.head())

time_diff = bbc_data['time_diff'] / 60
participant_id = bbc_data['participant_id']
action_item = bbc_data['action']

data = [dict(
    type='scatter',
    x=time_diff,
    y=participant_id,
    mode='markers',
    transforms=[dict(
      type='groupby',
      groups=action_item,
    )]
)]

layout = go.Layout(
    title='Participant ID and Time Difference Between Clicks',
    xaxis=dict(
        title='Time in minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)
