import feature_extractors.MFCC
import feature_extractors.power_spectral_density
import feature_extractors.spectral_centroid
import feature_extractors.spectral_flux
import feature_extractors.spectral_rolloff
import feature_extractors.spectral_flatness
import feature_extractors.MFCC_deltas
# from .feature_extractors import MFCC
# from .feature_extractors import power_spectral_density
# from .feature_extractors import spectral_centroid
# from .feature_extractors import spectral_flux
# from .feature_extractors import spectral_rolloff
# from .feature_extractors import spectral_flatness
import numpy as np

feature_funciton_array = [
    feature_extractors.MFCC.get_feature_vector,
    feature_extractors.power_spectral_density.get_feature_vector,
    feature_extractors.spectral_centroid.get_feature_vector,
    feature_extractors.spectral_flux.get_feature_vector,
    feature_extractors.spectral_rolloff.get_feature_vector,
    feature_extractors.spectral_flatness.get_feature_vector,
    # feature_extractors.MFCC_deltas.get_feature_vector,
]

# data = csv line with label at the end
def get_combined_feature_vector(data):
    grand_feature_vector = [val for sublist in [i(data.astype(float))[0].ravel() for i in feature_funciton_array] for val in sublist]
    return grand_feature_vector

if __name__ == "__main__":
    data = [None]
    label = "cough"
    get_combined_feature_vector([data, label])
