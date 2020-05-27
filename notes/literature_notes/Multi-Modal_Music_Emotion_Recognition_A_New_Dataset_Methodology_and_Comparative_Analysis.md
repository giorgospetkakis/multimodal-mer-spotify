# Multi-Modal Music Emotion Recognition: A New Dataset, Methodology and Comparative Analysis

## Notes
- Need for better music prediction/retrieval systems
    - Usually based on psychological/social features (e.g. mood/emotion)
    - Current music classification systems have a lot of room for improvement
- Challenges: people experience and describe emotions differently, lack of good audio emotion datasets
- Categorical and dimensional emotion models (this paper: categorical (MIREX))
    - Categorical: four basic emotions (happiness, sadness, anger, joy)
        - Hevner's adjective circle
        - MIREX mood classification task (five emotion groups) --> this one not supported by pscyhological models
    - Dimensional: multiple axes to map emotions
        - Arousal-valence (Russell)
        - Energy-stress (Thayer)
        - Sometimes dominance
- A handful of earlier works have combined audio and lyrics with varying levels of success, but this is (to the authors' best knowledge) the first study to include MIDI

### Hypothesis/research question
- Multimodal approach will solve the glass ceiling effect of only using audio features for classification --> this study uses lyrics and MIDI + melodic features from audio

### Method
- Study features individually and combined
- Evaluation "with several supervised learning and feature selection strategies" (the best one being SVM)
- MIREX used due to being considered a standard within the field
- AllMusic database used for tags by professionals
- Songs clustered according to significance 
- Songs were nearly balanced across clusters (18-23%)
- Three datasets: audio only, audio-lyrics (not included), and multimodal (MIDI, lyrics, and audio)
- Classification performed
- Feature selection and ranking employed to reduce number of features + improve results
- "After feature ranking, the optimal number of features was determined experimentally by evaluating results after adding one feature at a time, according to the obtained ranking"
- Feature selection and classification results both validated with repeated stratified 10-fold cross validation (20 repetitions), reporting the average obtained accuracy

### Findings
- Audio only dataset: best results with SVM classifiers and feature selection
    - Melodic features better than standard audio features, but not enough on their own
- Multimodal dataset: combination of standard and melodic audio features = better results
    - SA better for arousal, MIDI better for valence
- Confusion matrix: cluster 4 performs significantly worse than other clusters; all other clusters are around same performance level
- Multimodality seems to improve performance, but no lyrical features were selected for the model due to low performance

## Interesting points
- Seems that semantic information is potentially a good field to explore for lyrical features as opposed to more technical ones --> word embeddings