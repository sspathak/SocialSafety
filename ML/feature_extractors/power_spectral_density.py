# https://scipy-lectures.org/intro/scipy/auto_examples/plot_spectrogram.html

import scipy
import scipy.signal
import numpy as np


def _get_psd(audio_data):
    _, psd = scipy.signal.welch(audio_data)
    return psd


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    PSD = _get_psd(audio_data)
    PSD = np.array([np.mean(i) for i in PSD])
    PSD = np.argmax(PSD)
    return [PSD, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print psd for each line
    for i in csvfile:
        print("PSD = " + str(_get_psd(i)))
