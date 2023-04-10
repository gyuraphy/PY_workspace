import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r", encoding="utf-8") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r", encoding="utf-8") as inFpB:
        with open("C:/CookAnalysis/CSV/singer165.csv", "w", newline='', encoding="utf-8") as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                if int(row_list[-2]) >= 165 :
                    csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                if int(row_list[-2]) >= 165:
                    csvWriter.writerow(row_list)

print('Save. OK~')