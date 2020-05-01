import csv

with open("shopping.csv") as f:
    reader = csv.reader(f)
    next(reader)

    month_conversion = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4,
                        'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9,
                        'Nov': 10, 'Dec': 11}

    data = []
    evidence = []
    labels = []
    for row in reader:
        evidence.append([
            int(row[0]),    # Administrative
            float(row[1]),    # Administrative_Duration
            int(row[2]),    # Informational
            float(row[3]),    # Informational_Duration
            int(row[4]),    # ProductRelated
            float(row[5]),    # ProductRelated_Duration
            float(row[6]),      # BounceRates
            float(row[7]),      # ExitRates
            float(row[8]),      # PageValues
            float(row[9]),      # SpecialDay
            month_conversion[row[10]],    # Month
            int(row[11]),     # OperatingSystems
            int(row[12]),     # Browser
            int(row[13]),     # Region
            int(row[14]),     # TrafficType
            1 if row[15] == 'Returning_Visitor' else 0,     # VisitorType
            1 if row[16] == 'TRUE' else 0       # Weekend
        ])
        labels.append(
            1 if row[17] == "TRUE" else 0
        )

data = (evidence, labels)
print(data[0][3])
print(data[1][3])