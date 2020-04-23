# https://librosa.github.io/librosa/generated/librosa.feature.spectral_centroid.html

import librosa.feature


def _get_spectral_centroid(audio_data):
    # TODO
    spec_c = librosa.feature.spectral_centroid(audio_data, 44100)
    return [spec_c]


def get_feature_vector(labeled_audio_data):
    audio_data, label = labeled_audio_data
    spectral_centroid = _get_spectral_centroid(audio_data)
    return [spectral_centroid, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral centroid for each line
    for i in csvfile:
        print("Spectral centroid = " + str(_get_spectral_centroid(i)))
