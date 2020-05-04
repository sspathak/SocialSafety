# 1. https://www.audiocontentanalysis.org/code/audio-features/spectral-flux-2/
# 2. https://github.com/tyiannak/pyAudioAnalysis/blob/master/pyAudioAnalysis/ShortTermFeatures.py
# pick one from the two above

import numpy as np


def _get_spectral_flux(audio_data):
    # TODO
    # source: link # 1
    def FeatureSpectralFlux(X):
        X = np.reshape(X[:-1], (2, -1)).T
        # difference spectrum (set first diff to zero)
        X = np.c_[X[:, 0], X]
        # X = np.concatenate(X[:,0],X, axis=1)
        afDeltaX = np.diff(X, 1, axis=1)

        # flux
        vsf = np.sqrt((afDeltaX ** 2).sum(axis=0)) / X.shape[0]

        return (vsf)

    # source: link # 2
    def spectral_flux(fft_magnitude, previous_fft_magnitude):
        eps = 0.00000001
        """
        Computes the spectral flux feature of the current frame
        ARGUMENTS:
            fft_magnitude:            the abs(fft) of the current frame
            previous_fft_magnitude:        the abs(fft) of the previous frame
        """
        # compute the spectral flux as the sum of square distances:
        fft_sum = np.sum(fft_magnitude + eps)
        previous_fft_sum = np.sum(previous_fft_magnitude + eps)
        sp_flux = np.sum(
            (fft_magnitude / fft_sum - previous_fft_magnitude /
             previous_fft_sum) ** 2)

        return sp_flux

    spectral_flux = FeatureSpectralFlux(audio_data)
    spectral_flux = np.array([np.mean(i) for i in spectral_flux])
    return spectral_flux[1]


def get_feature_vector(labeled_audio_data):
    audio_data = labeled_audio_data[:-1]
    label = labeled_audio_data[-1]
    spectral_flux = _get_spectral_flux(audio_data)
    return [spectral_flux, label]


# for debugging
if __name__ == "__main__":
    # open csv file
    csvfile = []

    # print spectral flux for each line
    for i in csvfile:
        print("Spectral Flux = " + str(_get_spectral_flux(i)))
