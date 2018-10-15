import csv, os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))\

with open('average.csv','w') as csv_file_W:
    w = csv.writer(csv_file_W)
    w.writerow(('version','queryName','category','answer amount','average score','not bad ratio'))

    with open('calAverage.csv') as csv_file_R:
        csv_reader = csv.reader(csv_file_R, delimiter=',')
        line_count = 0
        for rowR in csv_reader:
            # print(rowR)
            if line_count == 0:
                print(f'Column names are {", ".join(rowR)}')
                line_count += 1
            else:
                if line_count == 1:
                    category = rowR[2]
                    version = rowR[0]
                    queryName = rowR[1]
                    sum=int(rowR[3])
                    count=1
                    if int(rowR[3]) != 0:
                        X0count=1
                    else:
                        X0count=0
                if rowR[1] == queryName:
                    # print(rowR[3])
                    # print(int(rowR[3]))
                    sum = sum + int(rowR[3])
                    count=count+1
                    if int(rowR[3]) != 0:
                        X0count += 1
                else: #new category
                    print(version)
                    print(queryName)
                    print(category)
                    print(sum) #output finishes
                    print(count)
                    print(sum/count)
                    w.writerow((version,queryName,category,count,sum/count,X0count/count))
                    sum=int(rowR[3])
                    count=1
                    category=rowR[2]
                    version = rowR[0]
                    queryName = rowR[1]
                    if int(rowR[3]) != 0:
                        X0count=1
                    else:
                        X0count=0
                line_count += 1
        csv_file_W.close()
