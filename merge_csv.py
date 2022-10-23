import glob
import os.path

csv_files = glob.glob(os.path.join("~/Project/data/", "*.csv"))
with open("~/Project/data/merged.csv", "w") as fout:
    for f_name in csv_files:
        with open("~/Project/data/{f_name}") as fin:
            fin.next()
            for line in fin:
                fout.write(line)