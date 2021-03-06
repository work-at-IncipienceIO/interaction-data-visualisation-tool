# PRE PROCESSES DATA to make sure visualisations can be made

import pandas as pd
import numpy as np
import sys

# Gets the first sys arg from app.py. Tells script where the input file is.
idvt_data = pd.read_csv(sys.argv[1])

# Replace all inf, NAN values
idvt_data = idvt_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

# if dataframe doesnt have these columns will create them
if not {'time_diff', 'participant_id', 'action_item'}.issubset(idvt_data.columns):

    # sorts data by participant_id and timestamp
    idvt_data = idvt_data.sort_values(['participant_id', 'timestamp'], ascending=True)

    # ACTION_ITEM is created by concatenating two columns
    idvt_data['action_item'] = idvt_data[['action', 'item']].apply(lambda x: ' '.join(x), axis=1)

    # get all unique participants
    participant_unique = np.unique(idvt_data['participant_id'])

    # Lists to contain data for new columns
    time_min = []
    time_diff = []

    # Loops over each participants and gets their first timestamp
    for i in participant_unique:

        x = idvt_data.loc[idvt_data.participant_id == i, :]

        x = x.sort_values(['timestamp'], ascending=True)

        min_time = x['timestamp'].iloc[0]

        for row in x['timestamp']:
            time_min.append(min_time)

    # MIN_TIME columns is created using time-min list
    idvt_data['min_time'] = time_min

    # TIME_DIFF created by looping over each row and subtracting 'min_time' from 'timestamp'
    for row in idvt_data['participant_id']:

        # change 'min_time' and 'timestamp' to datetime
        df = idvt_data[['timestamp', 'min_time']].astype('datetime64[ns]')

        # create new column with time_diff in seconds
        idvt_data['time_diff'] = df['timestamp'].subtract(df['min_time']).dt.total_seconds()

    # convert seconds into integers
    idvt_data['time_diff'] = idvt_data['time_diff'].astype(int)

    # save new dataframe to input filepath. It uses same name so will overwrite uploaded file
    idvt_data.to_csv(sys.argv[2])

else:
    # even if has columsn will turn 'time_diff' to numeric
    pd.to_numeric(idvt_data['time_diff'])

    # saves file to input filepath.
    idvt_data.to_csv(sys.argv[2])
