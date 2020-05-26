# MUSIC MOOD DETECTION BASED ON AUDIO AND LYRICS WITH DEEP NEURAL NET

## Quick overview
- Predicting mood in music with audio features and lyrics
- Deep learning model

## Notes
- Automatic mood detection is an active field within Music Information Retrieval (MIR)
- This paper: multimodal mood detection (audio features and lyrics) --> deep learning
- Database of 18,000 songs with different arousal/valence values to assess and compare model based on Million Song Dataset (MSD) and Deezer (streaming service akin to Spotify)
- Music mood studies started in early 20th century (seems to suggest Hevner's work might be seminal/start of the field)
- Mentions Besson et al.'s study "_Singing in the brain: Independence of lyrics and tunes_" was the first to show that music mood studies should consider both lyrics and the music itself by showing the modalities were processed differently in the brain
- Earlier approaches:
    - "Signal processing features related to timbre, pitch, and rhythm"
    - "Classical audio features such as Mel-Frequency Cepstral Coefficients as input to a Support Vector Machine"
    - Lyrics-based mood detection mainly based on feature engineering
        - Psycholinguistic emotion lexicon
        - Extraction of "stylistic features from text in an author detection task"
    - Multimodal approaches:
        - Prediction level and feature level fusion
        - Sentence level fusion
- New models appearing with the advances in machine learning --> audio-based deep learning, multimodal deep learning
    - Jeon et al.: "first multimodal deep learning approach using a bimodal convolutional recurrent network with a binary mood representation"
        - However, no comparison to classical approaches and no evaluation of their mid-level fusion vs. late fusion of unimodal models
    - Huang et al.: found early correlations between audio and lyrics, but limited by incomplete dataset
- "To our knowledge, there is no clear answer as to whether feature engineering yields better results than more end-to-end systems for the multimodal task, probably because of the lack of easily accessible large size datasets"
- Mood representation:
    - Monolabel tagging with simple tags, clusters of tags, or continuous representation
        - This study: continuous representation --> Russell's model
            - Chosen due to being fairly exhaustive, a continuous 2D space, and having been validated
            - Due to model choice, mood estimation is defined for this study as a "2D regression problem based on a track’s lyrics and/or audio"
- Research contributions:
    - Comparison of end-to-end lyrics based approaches to classical ones
    - 

### Hypothesis/research question


### Method


### Findings


## Interesting points