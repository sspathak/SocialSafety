from .feature_extractors import MFCC
from .feature_extractors import power_spectral_density
from .feature_extractors import spectral_centroid
from .feature_extractors import spectral_flux
from .feature_extractors import spectral_rolloff
import numpy as np

feature_funciton_array = [
    MFCC.get_feature_vector,
    power_spectral_density,
    spectral_centroid,
    spectral_flux,
    spectral_rolloff,
]

# data = csv line
def get_combined_feature_vector(data):
    grand_feature_vector = (np.array([i(data) for i in feature_funciton_array])).flatten
    return grand_feature_vector

if __name__ == "__main__":
    data = [None]
    label = "cough"
    get_combined_feature_vector([data, label])
