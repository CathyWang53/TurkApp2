import csv
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

patterns = [
["d like", "d love", "d really like"],
["looking for","look for","look to", "looking to"],
["I like", "I really like", "I love", "I really love","I prefer","like to"],
["what","which","where"],
["I'm "],
["let's "]

["can we", "can I"],
["can you find","can you please find","could you find"],
["can you give"],
["can you help","could you help"],
["can you put"],
["can you purchase"],
["can you recommend","could you recommend"],
["can you show"],
["can you","could you"]

["want"],
                   
["help"],
["find"],
["show ", "play ", "put on", "give"],
["list"],
["are there", "is there", "do you have"],
["something"]
]

counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

with open('results/ver1_5.csv', mode='r', encoding = "ISO-8859-1") as csv_file_r:
    with open('results/count.csv','w') as csv_file_w:
        csv_reader = csv.DictReader(csv_file_r)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                row['beginning'] = "random"
                line_count += 1

                # write the first row of result
                fieldnames = list(row.keys())
                csv_writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
                csv_writer.writeheader()

            #print(row)
            # categorize the beginning of each sentence
            row["beginning"] = "others"
            for i in range(12):
                for item in patterns[i]:
                    if item in row["text"]:
                        counts[i]+=1     # count each category
                        row["beginning"] = item
                        break

                else:
                    # Continue if the inner loop wasn't broken.
                    continue
                # Inner loop was broken, break the outer.
                break
            else:
                counts[-1]+=1 #others+1

            csv_writer.writerow(row)
            line_count += 1
        print(f'Processed {line_count} lines.')

outF = open("counts.txt", "w")
for item in counts:
  # write line to output file
  outF.write(str(item))
  outF.write("\n")
outF.close()
