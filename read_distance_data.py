# I'd like to join tables selectively, putting weight and distance as their own columns for each row of date.
# problems here include different number of rows and different date format in each file. Weight file contains
# a full datetime stamp, where aggregate distance has only the date. The weight file contains fields that I
# don't care about. So.. proposed steps:
#
# Read in Distance
# Change header of second column from "value" to "Distance"
# Store that somewhere
# Read in first two columns of weight
# Rename the second column from "Weight (lb)" to "Weight"
# Split datetime into date and time
# Look for records with multiple dates, selecting only the one with maximum time
# Store this somewhere
# Join the distance and weight tables, creating "0" entries in each direction for unmatched dates
#   IE - When a weight exists for a date but distance does not, create distance "0"
#        In the far more likely scenario that distance exists but weight does not, create weight "0"

import pandas

# practice creating functions with this simple one that announces the status of a loaded DataFrame
def Announce_Loaded_Data_Frame ( Loaded_Name, Loaded_Data_Frame ):
    print('Loaded file for ' + str(Loaded_Name) +
            ' with ' + str(Loaded_Data_Frame.ndim) +
            ' dimensions, ' + str(Loaded_Data_Frame.size) +
            ' elements averaging ' + str(Loaded_Data_Frame[Loaded_Name].mean().round(2)))
    return;

# Let's read in the aggregate distance using Pandas. Documentation for the read_csv is here
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
Distance_Data_Frame = pandas.read_csv('csv-data/aggregates_distance.csv',
        index_col='Date',
        parse_dates=['Date'],
        # It looks like when you rename columns here, you have to use the new name forward and backward
        # I didn't expect that behavior. So, even though the original file says 'date' in the header,
        # we have to switch to using 'Date' throughout.
        names=['Date','Distance'],
        header=0)

Announce_Loaded_Data_Frame("Distance",Distance_Data_Frame)

# Now let's read in the weight
Weight_Data_Frame = pandas.read_csv('csv-data/weight.csv',
        # Just get date and weight, which are the first two columns, index starting at 0.
        usecols=[0,1],
        index_col='Date',
        parse_dates=['Date'],
        header=0,
        names=['Date','Weight'])

Announce_Loaded_Data_Frame("Weight", Weight_Data_Frame)
