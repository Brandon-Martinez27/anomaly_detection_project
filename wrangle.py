import pandas as pd


def wrangle_logs():
    '''Gets anonymized codeup curriculum log data from a txt file
    and cohort data from a csv, prepared and merges the two. There 
    are two resulting dataframes, one with all known values (df) and 
    another with the cohort id's missing (no_id)'''
    
    #reads the txt file into a df
    df = pd.read_csv('anonymized-curriculum-access.txt', sep=' ', parse_dates=True, names=['date', 'time', 'page', 'user_id', 'cohort_id', 'ip'])
    #reads the csv file into a different df
    cohorts = pd.read_csv('cohorts.csv')

    #adds the date and time columns together into one column
    df['date'] = df['date'].map(str) + ' ' + df['time'].map(str) 
    # drops the time column
    df = df.drop(columns='time')
    # changes the date column to a datetime type
    df['date'] = pd.to_datetime(df.date)
    # sets the index to the datetime
    df = df.set_index('date').sort_index()

    # create a new df that only includes the missing cohort ids
    # from the previous df
    no_id = df[df.cohort_id.isna()]
    # fills those values with 0
    no_id = no_id.fillna(0)

    # resets the index of initial df
    df = df.reset_index()
    # drop the null values used in no_id df
    df = df.dropna()
    # change cohort id to an integet
    df['cohort_id'] = df['cohort_id'].astype('int')
    # merges the cohort and df dataframes together for additional
    # data on cohorts and start/end dates
    df = df.merge(cohorts, how='left', on='cohort_id')
    # change program_id column to integer
    df['program_id'] = df.program_id.astype('int')
    # sets the date to the index once again
    df = df.set_index('date').sort_index()

    # change start and end dates to a datetime type
    df['start_date'] = pd.to_datetime(df.start_date)
    df['end_date'] = pd.to_datetime(df.end_date)
    # dropped all observations with '/' as page. This is the homepage.
    df = df.drop(df[df.page == '/'].index)
    # remove staff from the data
    df = df[df.name != 'Staff']

    # adds column to show how many days the user have been active based on current date
    df['days_active'] = (df.index - df.start_date).dt.days
    # adds column to show how long the programs lasts in days
    df['program_length'] = (df.end_date - df.start_date).dt.days
    # adds column to show how days user accessed the curriculum after graduating
    df['post_access'] = (df.index - df.end_date).dt.days
    
    return df, no_id