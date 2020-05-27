# Music mood classification model based on arousal-valence values

## Quick overview
- Short conference paper (4 pages)
- Arousal-valence model for classifying music mood
- 10 subjects
- 460 song clips tagged with a mood and a point in the arousal-valence plane
- _k_-means clustering of tags using the points


## Notes
The paper is about a proposed model for music mood classification. It very briefly goes through a number of emotion models that can be relevant for music classification:
- Hevner: investigation of the affective values of music features (mode, tempo, pitch, rhythm, harmony, and melody)
    - Categorization of 67 adjectives into 8 groups of similar emotional states
    - Comparison of musical characteristics in 8 affective states --> will need to read the original paper, but sounds like she considered the weight/influence of each mentioned feature to each of the 8 groups made from the adjectives
- Russell: circumplex model of emotion based on arranging 28 adjectives along arousal and valence axes
- Thayer: model in two-dimensional space with axis from low to high energy and low to high stress
    - Depression, anxiety, contentment, and exuberance all in different corners
- Models all dimensional as opposed to categorical --> dimensional models more common for emotion

### Hypothesis/research question
- Music can be recommended to listeners based on a number of features (genre, similar artists, looking at the songs that users with similar tastes listen to, etc.)
- Mood/emotion can also be used for classifying and recommending music
    - If a mood-based recommendation scheme is to perform better, it is necessary to have a well-defined music mood model
        - The paper proposes using the arousal/valence model as the foundation for classification

### Method
- Arousal/valence data collected from 10 participants
- 446 music clips
- Participants added a mood tag and chose a point in the AV plane after listening to a song --> 4460 tags and point values
- Data includes a mix of genres
- Data cleanup: reduction of number of unique tags --> 32 most frequent tags used --> divided into 8 groups based on usage and meaning (tag with highest frequency used as definition for each group)
- AV values clustered into 8 groups according to their mood tags

### Findings
- Clusters 3, 4, 5, 6 (all categories with high numbers of "I don't know" tags) tend to be along the axes --> suggests that music with moods that people feel less certain about corresponds to neutral arousal and/or valence, while more "clear" moods correspond to  high/low values for the axes
- Suggests way to express a mood on the plane of Russell's model using probability distributions of moods (using the moods defined in the paper)

## Interesting points

- Biggest point of interest imo in this article is the different emotion models mentioned --> the next articles I will be going through are the ones describing the specific models to see what could actually be done with them in our project
    - Hevner's model could potentially be used to see if adjective tags correspond to her findings on the relationship between musical features and the emotional states she uses
    - Thayer: sad music, upbeat music, lyrical content corresponding to moods (happy, sad, angry, anxious?)
- Another one is _k_-means to cluster moods into regions on Russell's circumplex model --> clustering for our labels to uncover patterns/relationships between emotions and music features?