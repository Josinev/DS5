import pandas as pd
#You have been given a file about hotel bookings, you can find these data in the file
#‘hotelBookings.xlsx’. These data contain the number of bookings of the hotel ‘Resort Hotel’,
#which is spread over different countries. This file contains a lot of errors, and needs to be
#cleaned. For this exercise, you need to read the Excel file, analyse the data, find as many
#mistakes as possible and correct them. In particular:
#1. Read the excel file using the pandas library
#2. Inspect the data and find as many mistakes you can.
#3. Clean the data, which decisions did you make to solve the errors?

data = pd.read_excel('hotelBookings.xlsx')
import numpy as np
#Lijstje van fouten
#lead_time outlier
#arrival_date_month een aantal keer geen maand 
#stay_in_week_nights integers
#adults aantal adults 
#children aantal children
#country moet een string van 3 letters zijn.

data.fillna(np.NaN)

for i in range(len(data)):
    if data.iloc[i,5] <= 31 and data.iloc[i,5] <= 31:
        if data.iloc[i,4] == np.NaN():
            print(i)