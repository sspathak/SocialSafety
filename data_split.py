file_path = "./CSVs/cough-data-throatclearing-1.csv"

save_path = "./CSVs/cough-data-throatclearing-3.csv"

with open(file_path,'r') as fil:
    for j in range(200 * 1):
        fil.readline()
    # input(len(fil.readlines()))
    # dat = fil.readline()
    with open(save_path,'w') as wfil:
        for i in range(200):
            # if i % 50 == 0:
            #     fil.readlines(50)
            #     print(i)
            wfil.writelines(fil.readline())
print("done")