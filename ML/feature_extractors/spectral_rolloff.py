# https://librosa.github.io/librosa/generated/librosa.feature.spectral_rolloff.html

import librosa.feature
import numpy as np

def _get_spectral_rolloff(audio_data):
    # TODO
    spec_roll = librosa.feature.spectral_rolloff(audio_data, 44100)
    return spec_roll


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    spectral_rolloff = _get_spectral_rolloff(audio_data)
    spectral_rolloff = np.array([np.mean(i) for i in spectral_rolloff])
    return [spectral_rolloff, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral rolloff for each line
    for i in csvfile:
        print("Spectral rolloff = " + str(_get_spectral_rolloff(i)))
