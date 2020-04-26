from praatio import tgio
import os
import scipy.io.wavfile
import numpy as np

csv_folder="CSVs"
critical_labels = ['cough', 'speech', 'silence']

def print_stats(duration_mp):

    duration_ls = [(y, x) for (x, y) in duration_mp.items()]

    duration_ls.sort()

    duration_ls.reverse()

    for labelStat in duration_ls:
        print("Label " + labelStat[1] + " ; Total duration: " + str(round(labelStat[0], 2)) + " seconds")

def save_data(lab, dat):
    csv_file_path = os.path.join(csv_folder, lab + ".csv")

    # print("saving")
    dat.append(critical_labels.index(lab))
    # print(dat)
    # print(str(dat)[1:-1])

    dt = np.array([dat])

    # print(dt)

    with open(csv_file_path, 'ab') as fil:
    #     fil.write(str(dat)[1:-1]+f",{lab}\n")
        np.savetxt(fil, dt, delimiter=",")
    # print("Appended to file")




def main():

    original_folder = "flusense_data"
    wav_folder = "FluSense_audio"

    files = os.listdir(original_folder)

    duration_mp = {}
    data_map = {}
    # critical_labels = ['cough', 'speech', 'silence']
    critical_labels = ['cough']

    cough_data = []
    speech_data = []
    silence_data = []
    etc_data = []
    count = 0

    for file in files:
        # if count < 3:
        #     count += 1
        #     continue
        if not file.endswith('.TextGrid'):
            continue

        wav_file_path = os.path.join(wav_folder, str(file)[:-8] + "wav")


        full_path = os.path.join(original_folder, file)

        try:

            fs, wav_file_data = scipy.io.wavfile.read(wav_file_path)
            try:
                wav_file_data = wav_file_data[:, 0]
            except IndexError:
                # print(wav_file_data)
                print("INDEX ERROR_____________________________________________________")
                pass
        except FileNotFoundError:
            continue

        print()
        print("                                                     " + str(count))
        count += 1
        print("file = " + str(wav_file_path))
        print(f"fs = {fs}       wav list length = {len(wav_file_data)}")
        # print(f"list = {wav_file_data}")

        tg = tgio.openTextgrid(full_path)

        t_name = tg.tierNameList[0]

        entryList = tg.tierDict[t_name].entryList


        for entry in entryList:


            lab = entry.label
            start_ts = int(entry.start * 44100)
            end_ts = int(entry.end * 44100)
            # print(entry)
            print(f"TIME    :label = {entry.label}\t start = {entry.start}\t end = {entry.end}")
            print(f"TS      :label = {entry.label}\t start = {start_ts}\t end = {end_ts}")
            # print("     file = " + str(file)[:-8])

            if lab not in critical_labels:
                continue
            if lab not in duration_mp:
                duration_mp[lab] = 0.0

            if lab not in data_map:
                data_map[lab] = []

            duration_mp[lab] += (entry.end - entry.start)
            # print(wav_file_data)
            data_map[lab].extend(wav_file_data[start_ts:end_ts])

        for (lbl, dat) in data_map.items():

            while len(data_map[lbl]) > 8001:
                # print("CONTINUE?", end="")
                # input()
                save_data(lbl, data_map[lbl][:8001])
                data_map[lbl] = data_map[lbl][8001:]
            print()

        # input("PROCEED?")

    print_stats(duration_mp)
    print(data_map)

    # for (lbl, dat) in data_map.items():




if __name__ == "__main__":
    main()