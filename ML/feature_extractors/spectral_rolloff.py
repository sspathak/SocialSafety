# https://librosa.github.io/librosa/generated/librosa.feature.spectral_rolloff.html

import librosa.feature


def _get_spectral_rolloff(audio_data):
    # TODO
    spec_roll = librosa.feature.spectral_rolloff(audio_data, 44100)
    return [spec_roll]


def get_feature_vector(labeled_audio_data):
    audio_data, label = labeled_audio_data
    spectral_rolloff = _get_spectral_rolloff(audio_data)
    return [spectral_rolloff, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral rolloff for each line
    for i in csvfile:
        print("Spectral rolloff = " + str(_get_spectral_rolloff(i)))
