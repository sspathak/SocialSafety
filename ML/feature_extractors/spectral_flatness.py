# https://librosa.github.io/librosa/generated/librosa.feature.spectral_flatness.html

import librosa.feature
import numpy as np

def _get_spectral_flatness(audio_data):
    # TODO
    spec_fl = librosa.feature.spectral_flatness(audio_data)
    return spec_fl


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    spectral_flatness = _get_spectral_flatness(audio_data)
    spectral_flatness = np.array([np.mean(i) for i in spectral_flatness])
    return [spectral_flatness, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral flatness for each line
    for i in csvfile:
        print("Spectral flatness = " + str(_get_spectral_flatness(i)))
