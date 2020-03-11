
inputFile = "E96_decade_resistors.txt"
outputFile = "ResistorResults.txt"
ratio_upper = 0.51
ratio_lower = 0.5

R = []
results = [["Ratios","R1","R2"]]

f = open(inputFile, "r")
for r in f:
    try:
        R.append(int(r))
    except ValueError:
        pass

f.close()

for r1 in R:
    for r2 in R:
        ratio = r2 / (r1 + r2)
        if ratio_lower < ratio and ratio < ratio_upper:
            results.append([ratio,r1,r2])

f = open(outputFile, "w")

for result in results:
    output = f'{result[0]}\t{result[1]}\t{result[2]}\n'
    f.write(output)

f.close()
