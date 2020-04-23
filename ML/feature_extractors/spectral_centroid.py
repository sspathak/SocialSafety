import librosa.feature


def _get_spectral_centroid(audio_data):
    # TODO
    # use librosa.feature.spectral_centroid()
    return [None]


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
