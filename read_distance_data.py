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

# Let's read in the aggregate distance 
distance = pandas.read_csv('csv-data/aggregates_distance.csv', 
        index_col='Date', 
        parse_dates=['Date'],
        # It looks like when you rename them here, you have to use the new name in the rest of the arguments. I didn't
        # expect that behavior.
        names=['Date','Distance'],
        # Required to have header=0 because we're renaming
        header=0)
print('loaded aggregate distance, here is a sample')
print(distance)

# Now let's read in the weight
weight = pandas.read_csv('csv-data/weight.csv',
        # Just get date and weight
        usecols=[0,1],
        index_col='Date',
        parse_dates=['Date'],
        header=0,
        names=['Date','Weight'])
print('loaded weight, here is a sample')
print(weight)

