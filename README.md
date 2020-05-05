# SocialSafety
Link to presentation: https://docs.google.com/presentation/d/1O4N225_Tz3dYs8fuonMF-9DhR1rRk9kmNqhO2ElCn3A/edit?usp=sharing

Bluetooth demo: Bluetooth-demo.mp4, https://drive.google.com/open?id=1wXD-x5E5XanVUXH3AVs836xIp1keX1SB

Cough detection demo: Cough-detection-demo-final.mp4, https://drive.google.com/open?id=1d4dhCYmLRG932eNaItdDp-m-dor0LsiS


# Cough detection
The Python script receives data from an android phone through the MyActivities app. It passes the data to a Random Forest classifier which predicts if the audio slice has cough present in it.
The Random Forest classifier was trained partially on the dataset mentioned at the end of this document. The rest of the data was collected by us.

Links to youtube videos used in demo:
1. Steve Jobs speech - https://youtu.be/UF8uR6Z6KLc?t=510
2. Cough sample audio - https://www.youtube.com/watch?v=Qp09X74kjBc

# Features
We extracted the following features to generate the feature vector for each audio slice.

1. MFCCs
2. Power Spectral Density
3. Spectral Flux
4. Spectral rolloff
5. Spectral Flatness


# Labels

The avialable labels are:

1. cough
2. sneeze
3. sniffle
4. throat-clearing
5. speech
6. etc (i.e everything else)

# Credit for dataset goes to:
    https://github.com/Forsad/FluSense-data
    @article{10.1145/3381014,
    author = {Al Hossain, Forsad and Lover, Andrew A. and Corey, George A. and Reich, Nicholas G. and Rahman, Tauhidur},
    title = {FluSense: A Contactless Syndromic Surveillance Platform for Influenza-Like Illness in Hospital Waiting Areas},
    year = {2020},
    issue_date = {March 2020},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {4},
    number = {1},
    url = {https://doi.org/10.1145/3381014},
    doi = {10.1145/3381014},
    journal = {Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.},
    month = mar,
    articleno = {Article 1},
    numpages = {28},
    keywords = {Contactless Sensing, Crowd Behavior Mining, Edge Computing, Influenza Surveillance}
    }


