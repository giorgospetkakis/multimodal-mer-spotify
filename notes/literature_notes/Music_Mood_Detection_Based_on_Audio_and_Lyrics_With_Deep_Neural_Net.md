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
    - Evaluation of mid-level fusion
    - Evidence that "arousal is highly correlated to the audio source, whereas valence requires both modalities to be predicted significantly better"
    - Comparison to classical feature engineering models
- 

### Hypothesis/research question
- Will a multimodal model perform better than unimodal ones? Deep learning vs. classical approaches?

### Method
- First unimodal models for each aspect --> later combined into multimodal network
    - Model: optimal weighted average of predictions from the unimodal models:
        - Audio: "an SVM on top of MFCCs, spectral flux, rolloff and centroid"
            - Mel-spectrogram as input run through convolutional neural network
        - Lyrics: "an SVM on top of basic, linguistic and stylistic features (n-grams, lexicon-based features, etc.)"
            - Word embedding as input tested on several architectures (convolutional and recurrent NNs, bag-of-words)
        - Fusion model: fully connected layers removed from unimodal architectures; two fully connected layers and outputs concatenated
- Mood-related tags chosen from last.fm for songs that exists in MSD
- Werriner et al.'s dataset that places 14k words in the arousal-valence space --> used to embed tags into the space --> normalized
- Training on 60%, validation on 20%, testing on 20%

### Findings
- Unimodal models:
    - "Lyrics and audio achieve relatively similar performance on valence detection" for both classical and deep learning approaches
    - Audio outpredicts lyrics for arousal prediction --> aligns with knowledge that arousal is tied to rhythm and energy (audio features), whereas valence can be explained by both audio and lyrics
        - Earlier evidence aligns with findings that happy/sad emotions can be defined by differences in arousal and calm/angry ones by differences in valence
    - Deep learning approaches outperform classical ones on audio-based prediction
    - Classical lyrics-based approaches are better than deep learning ones (in particular for valence)
- Late fusion:
    - Arousal: "the fusion of the modalities does not significantly improve arousal detection performance compared to audio-based models" for neither classical nor deep learning approaches
        - No added value of including lyrics along with audio in deep learning models
    - Valence: both modalities are useful for valence detection in both types of approaches
        - Audio and lyrics are complementary for overall better model performance for valence detection
- Bimodal approaches:
    - Arousal detection by deep learning better than for late fusion
    - "Late fusion for valence detection yields better results for classical systems"
    - Mid-level fusion: improvement in valence detection --> might indicate earlier correlations between the two modalities
        - Model does not seem to be able to reveal new correlations for arousal detection
        - "This performing fusion, along with more accurately predicted valence thanks to audio, is sufficient for achieving similar performance to classical approaches, without the use of any external data designed by experts"
            - Weighted mean between CA and DL useful

