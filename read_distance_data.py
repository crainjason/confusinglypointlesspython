# Imports two CSV files, merges them, and prints outpoot as pruf.

# Everyone wants me to import as pd. Fuck that. I'm my own man.
import pandas

# announce loaded files using schmancy f strings
def Announce_Loaded_Data_Frame ( name ):
    print (
            f"Loaded file for {name.name} with {name.ndim} dimensions and {name.size} records averaging {name.mean().round(2)}"
            )

# Let's read in the aggregate distance using Pandas. Documentation for the read_csv is here
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# Purposefully not setting an index_col to I can observe how things work.
Distance_Data_Frame = pandas.read_csv('csv-data/aggregates_distance.csv', 
        parse_dates=['Date'],
        names=['Date','Distance'],
        header=0)

# Fix date combination problems by converting everything to a date instead of a datetime... kind of
Distance_Data_Frame['Date'] = Distance_Data_Frame['Date'].dt.date

# Accounce that everything is going OK
Announce_Loaded_Data_Frame(Distance_Data_Frame["Distance"])

# Now let's read in the weight
Weight_Data_Frame = pandas.read_csv('csv-data/weight.csv',
        # Just get date and weight, which are the first two columns, index starting at 0.
        usecols=[0,1],
        parse_dates=['Date'],
        header=0,
        names=['Date','Weight'])

# Fix date combination problems by converting everything to a date instead of a datetime... kind of
Weight_Data_Frame['Date'] = Weight_Data_Frame['Date'].dt.date

# Announce again
Announce_Loaded_Data_Frame(Weight_Data_Frame["Weight"])

# Join the frames together based on 'Date' column using the union of both
Combined_Data_Frame = pandas.merge(Weight_Data_Frame,Distance_Data_Frame, how='outer', on='Date')
print("Frames merged")

# Sort everything by date
Combined_Data_Frame = Combined_Data_Frame.sort_values('Date',ascending=False)
print("Values sorted")

with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    print(Combined_Data_Frame)
