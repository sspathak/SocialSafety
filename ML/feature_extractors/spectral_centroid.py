# https://librosa.github.io/librosa/generated/librosa.feature.spectral_centroid.html

import librosa.feature
import numpy as np

def _get_spectral_centroid(audio_data):
    # TODO
    spec_c = librosa.feature.spectral_centroid(audio_data, 44100)
    return spec_c


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    spectral_centroid = _get_spectral_centroid(audio_data)
    spectral_centroid = np.array([np.mean(i) for i in spectral_centroid])
    return [spectral_centroid, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral centroid for each line
    for i in csvfile:
        print("Spectral centroid = " + str(_get_spectral_centroid(i)))
