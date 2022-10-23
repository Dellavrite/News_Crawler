import glob
import os.path

csv_files = glob.glob(os.path.join("*.csv"))
print(csv_files)
with open("merged.csv", "w") as f_out:
    for f_name in csv_files:
        with open(f"{f_name}") as fin:
            fin.readline()
            for line in fin:
                f_out.write(line)
        os.remove(f"{f_name}")
