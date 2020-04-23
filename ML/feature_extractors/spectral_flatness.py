# https://librosa.github.io/librosa/generated/librosa.feature.spectral_flatness.html

import librosa.feature


def _get_spectral_flatness(audio_data):
    # TODO
    spec_fl = librosa.feature.spectral_flatness(audio_data)
    return [spec_fl]


def get_feature_vector(labeled_audio_data):
    audio_data, label = labeled_audio_data
    spectral_flatness = _get_spectral_flatness(audio_data)
    return [spectral_flatness, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral flatness for each line
    for i in csvfile:
        print("Spectral flatness = " + str(_get_spectral_flatness(i)))
