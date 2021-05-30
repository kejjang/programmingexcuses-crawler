import glob

rootpath = "./data"
lines = []

for file in glob.glob(f"{rootpath}/*.txt"):
    with open(file) as fh:
        line = fh.readline()
        lines += [line]

lines.sort(key=lambda line: line.lower())

for line in lines:
    print(line)
