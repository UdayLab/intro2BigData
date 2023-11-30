def fixFile(file):
    fileData = {}
    fl = ""
    with open(file, "r") as f:
        fl = f.readline()
        for line in f:
            line = line.strip().split(",")
            tid = line[0]
            info = line[2]
            if info == "":
                continue
            if tid not in fileData:
                fileData[tid] = [info]
            else:
                fileData[tid].append(info)

    key = list(fileData.keys())
    val = list(fileData.values())

    zipped = sorted(zip(key, val), key=lambda x: x[0])

    with open("Formatted_" + file, "w") as f:
        for k, v in zipped:
            for i in v:
                f.write(i + "\t")
            f.write("\n")


fixFile("OnlineRetail.csv")