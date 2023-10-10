import pandas as pd
#You have been given a file about hotel bookings, you can find these data in the file
#‘hotelBookings.xlsx’. These data contain the number of bookings of the hotel ‘Resort Hotel’,
#which is spread over different countries. This file contains a lot of errors, and needs to be
#cleaned. For this exercise, you need to read the Excel file, analyse the data, find as many
#mistakes as possible and correct them. In particular:
#1. Read the excel file using the pandas library
#2. Inspect the data and find as many mistakes you can.
#3. Clean the data, which decisions did you make to solve the errors?


import numpy as np
#Lijstje van fouten
#lead_time outlier
#arrival_date_month een aantal keer geen maand 
#stay_in_week_nights integers
#adults aantal adults 
#children aantal children
#country moet een string van 3 letters zijn.


#arrival_date_month een aantal keer geen maand
data = pd.read_excel('hotelBookings.xlsx')
def maakmaand(data):
    """Functie die De legen vlekken van de maanden opvult"""
    data.iloc[:847,4] = 'July'
    data.iloc[847:,4] = 'August'
    return data

#stay in week nights
def alsdaggeenintegerdrop(data):
    """Functie die afdwingt dat de nachten hele getallen zijn en anders een rij dropt"""
    data = data.drop(data.index[data['stays_in_week_nights'] == 4.3])
    data = data.reset_index(drop=True)
    return data

#adults aantal adults
def volwasseneonreeel(data):
    """Een onreeel aantal volwassenen wordt gedropt."""
    data = data.drop(data.index[data['adults'] >= (data.iloc[:,9].mean() * 2)])
    data = data.reset_index(drop=True)   
    return data

#adults aantal adults
def kinderenonreeel(data):
    """Een onreel aantal kinderen wordt gedropt"""
    data = data.drop(data.index[data['children'] >= (data.iloc[:,10].mean() * 2)])
    data = data.reset_index(drop=True)
    return data

#country moet een string van 3 letters zijn.
def landisstring(data):
    """Een landcode moet bestaan uit een string van 3 letters anders gedropt"""
    lst = data.iloc[:,13].unique().tolist()
    lst.remove(2)
    lst.remove(3)
    lst.remove(np.nan)

    data = data.drop(data.index[data['country'].isin(lst) == False])
    data = data.reset_index(drop=True)
    return data

#opschonen data hotelbookings
def opschonenhotelbookings(data):
    """Een functie die alle opschoon functiets uitvoert."""
    data = maakmaand(data)
    data = alsdaggeenintegerdrop(data)
    data = volwasseneonreeel(data)
    data = kinderenonreeel(data)
    data = landisstring(data)

    return data
print(opschonenhotelbookings(data))
