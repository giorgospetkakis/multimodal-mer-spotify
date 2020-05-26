# CREATING A SIMPLIFIED MUSIC MOOD CLASSIFICATION GROUND-TRUTH SET

## Notes


### Hypothesis/research question
- Ground-truth set needed to evaluate mood-based music information retrieval systems

### Method
- USPOP audio tracks
- last.fm tags
- Top 100 tags for each USPOP song in the last.fm database
- POS tagger to select adjectives
- 19 most popular adjectives deemed related to music mood chosen
- Songs with at least one of the tags were given 19-dimensional binary vector indicating which adjectives they were tagged with
- Songs clustered with _k_-means with 3 clusters
- Percentage of tracks with a given adjective in each cluster calculated

### Findings
- 3 obtained mood clusters as simplified ground-truth set (aggressive-angry, calm-mellow, and upbeat-happy as top results in each cluster)

## Potential usefulness