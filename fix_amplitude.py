import numpy as np
import ast
import random

file_path = "./CSVs/cough-data-speech-2.csv"

save_path = "./CSVs/cough-data-speech-2.csv"

# with open(file_path, "rb") as fil:
val = np.loadtxt(file_path, delimiter=",")
input(val)
# for i in val:
#     i[0] = i[1]
# val = val.tolist()
# np.savetxt(save_path, val, delimiter=",", newline="\n")
# val = np.abs(val)
# print(np.mean(val))


# with open(file_path,'r') as fil:
#     for j in range(200 * 1):
#         fil.readline()
#     # input(len(fil.readlines()))
#     # dat = fil.readline()
#     with open(save_path,'w') as wfil:
#         for i in range(200):
#             # if i % 50 == 0:
#             #     fil.readlines(50)
#             #     print(i)
#             wfil.writelines(fil.readline())
print("done")