import python_speech_features
import numpy as np
import librosa
import scipy


def _get_mfcc(audio_data):
    # TODO
    # use python_speech_features.mfcc() or librosa.feature.mfcc()
    mfcc_vec = librosa.feature.mfcc(audio_data, 44100) # adjust sampling rate
    return [mfcc_vec]


def get_feature_vector(labeled_audio_data):
    audio_data, label = labeled_audio_data
    mfcc = _get_mfcc(audio_data)
    return [mfcc, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print mfcc for each line
    for i in csvfile:
        print("MFCC = " + str(_get_mfcc(i)))
