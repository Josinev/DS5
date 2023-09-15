def filter(records):
    """Wanneer cijfer hoger is dan 80.0 dan print name en cijfer student"""
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")