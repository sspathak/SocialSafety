file_path = "cough-data-cough-0.csv"

save_path = "./CSVs/cough-data-cough-1.csv"

with open(file_path,'r') as fil:
    fil.readlines(500)
    # input(len(fil.readlines()))
    # dat = fil.readline()
    with open(save_path,'w') as wfil:
        for i in range(1000):
            if i % 50 == 0:
                fil.readlines(50)
                print(i)
            wfil.writelines(fil.readline())
print("done")