def average(records):
    """ bereken het gemiddelde door alle recods bij elkaar op te tellen en te delen door het totaal"""
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)

    print(f"Average Grade: {average}")
    print("--------------------")