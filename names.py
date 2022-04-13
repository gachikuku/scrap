infile = "names.txt"
outfile = "5.txt"

with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        if len(line)==6:
            fout.write(line)
