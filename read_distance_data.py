
import pandas

# practice creating functions with this simple one that announces the status of a loaded DataFrame
# we use a string called "Loaded_Name," which actually references several things, including
# 
# 1. The "purpose" of the file (ie, are we getting weight, distance, etc?)
# 2. The name of the column we want (luckily we only have date and this other one to choose from)
# 3. The name of the table, conceptually
#
def Announce_Loaded_Data_Frame ( name ):
    print (
            f"Loaded file for {name.name} with {name.ndim} dimensions and {name.size} averaging {name.mean().round(2)}"
            )

# Let's read in the aggregate distance using Pandas. Documentation for the read_csv is here
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
Distance_Data_Frame = pandas.read_csv('csv-data/aggregates_distance.csv', 
        parse_dates=['Date'],
        # It looks like when you rename columns here, you have to use the new name forward and backward
        # I didn't expect that behavior. So, even though the original file says 'date' in the header,
        # we have to switch to using 'Date' throughout.
        names=['Date','Distance'],
        header=0)

# Fix date combination problems by converting everything to a date instead of a datetime... kind of
Distance_Data_Frame['Date'] = Distance_Data_Frame['Date'].dt.date

#Announce_Loaded_Data_Frame(Distance_Data_Frame["Distance"])

# Now let's read in the weight
Weight_Data_Frame = pandas.read_csv('csv-data/weight.csv',
        # Just get date and weight, which are the first two columns, index starting at 0.
        usecols=[0,1],
        parse_dates=['Date'],
        header=0,
        names=['Date','Weight'])

# Fix date combination problems by converting everything to a date instead of a datetime... kind of
Weight_Data_Frame['Date'] = Weight_Data_Frame['Date'].dt.date

# Join the frames together based on 'Date' column using the union of both
Combined_Data_Frame = pandas.merge(Weight_Data_Frame,Distance_Data_Frame, how='outer', on='Date')

# Sort everything by date
Combined_Data_Frame = Combined_Data_Frame.sort_values('Date',ascending=False)

with pandas.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(Combined_Data_Frame)
