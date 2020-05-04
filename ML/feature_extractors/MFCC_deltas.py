import python_speech_features
import numpy as np
import librosa
import scipy


def _get_mfcc_delta(audio_data):
    # TODO
    # use python_speech_features.mfcc() or librosa.feature.mfcc()
    mfcc_vec = librosa.feature.mfcc(audio_data[:(len(audio_data)//2)], 44100) # adjust sampling rate
    mfcc_vec = np.array([np.mean(i) for i in mfcc_vec])
    mfcc_vec_2 = librosa.feature.mfcc(audio_data[(len(audio_data)//2):], 44100)
    mfcc_vec_2 = np.array([np.mean(i) for i in mfcc_vec_2])
    mfcc_vec = abs(mfcc_vec_2) - abs(mfcc_vec)

    # mfcc_vec = np.mean(mfcc_vec)
    return mfcc_vec


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    mfcc = _get_mfcc_delta(audio_data)
    return [mfcc, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print mfcc_deltas for each line
    for i in csvfile:
        print("MFCC = " + str(_get_mfcc_delta(i)))
