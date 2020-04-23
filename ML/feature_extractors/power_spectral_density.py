import scipy
import scipy.signal


def _get_psd(audio_data):
    _, psd = scipy.signal.welch(audio_data)
    return [psd]


def get_feature_vector(labeled_audio_data):
    audio_data, label = labeled_audio_data
    PSD = _get_psd(audio_data)
    return [PSD, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print psd for each line
    for i in csvfile:
        print("PSD = " + str(_get_psd(i)))
