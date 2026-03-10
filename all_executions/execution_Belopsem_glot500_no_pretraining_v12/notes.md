PaSeMiLL id: 5489980
PaSeMiLL filtering threshold: -1.0
PaSeMiLL new: just done for results for v11_no_CBIE

postprocessing v11_no_CBIE (needs to be executed with normal pipeline):
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.40  
ID: 5490792 (deprecated because of hsb sw filtering even though it leads to worse results), 5496309 (err: no gpu), 5496686 (new)
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - including Upper Sorbian stop-word extraction
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.4148430066603235,0.436,0.4251584592881521
Results Test: 0.33736559139784944,0.33466666666666667,0.33601070950468537