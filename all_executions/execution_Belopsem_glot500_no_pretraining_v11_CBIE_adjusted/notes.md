PaSeMiLL id: 5485524
PaSeMiLL filtering threshold: -1.0
PaSeMiLL new: executed pipeline with cbie_transformation.py call instead of own implementation

postprocessing v1:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.35  
ID: 5486133 (failed due to Node failure), 5486308 (failed due to time limit --> train file generated), 5486530
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - including Upper Sorbian stop-word extraction
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v46 of CBIE_v5 (best runs so far) to see the impact of the changes  --> hopefully no impact
    - new: 
        - test with hyperparameters
Results Train: 0.658458244111349,0.615,0.6359875904860393

postprocessing v2:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.40  
ID: 5486544  
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
        - test new hyperparameters
Results Train: 0.7738896366083445,0.575,0.6597819850831899

postprocessing v3:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.25  
- filtering-threshold: 0.35  
ID: 5486545  
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
        - test new hyperparameters
Results Train: 0.7198538367844093,0.591,0.6490939044481054

postprocessing v4:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.40
- segment-threshold: 0.2  
- filtering-threshold: 0.35  
ID: 5487381  
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
        - test new hyperparameters
Results Train: 

postprocessing v5:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.20  
- filtering-threshold: 0.425  
ID: 5487392
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
        - test new hyperparameters
Results Train: 0.8148148148148148,0.528,0.6407766990291262

postprocessing v6 (waiting for execution):
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.45  
ID: 5487393
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
        - test new hyperparameters
Results Train: 0.8504504504504504,0.472,0.6070739549839228

**postprocessing v7: --> deprecated, now best: v11_de_sw_filter**
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5487394
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
        - test new hyperparameters
Results Train: 0.7362637362637363,0.603,0.663001649257834

postprocessing v8:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.25  
- filtering-threshold: 0.40  
ID: 5487512  
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
        - test new hyperparameters
Results Train: 0.814540059347181,0.549,0.6559139784946237

postprocessing v9 (not yet executed):
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.45
- segment-threshold: 0.2  
- filtering-threshold: 0.35  
ID: 5487873  
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
        - test new hyperparameters
Results Train: 0.658458244111349,0.615,0.6359875904860393  

postprocessing v10:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.41  
ID: 5487878  
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
        - test new hyperparameters
Results Train: 0.791023842917251,0.564,0.658493870402802  

postprocessing v11:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.39  
ID: 
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
        - test new hyperparameters
Results Train: 


--------


**postprocessing v11_de_sw_filter:**
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488661  
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.7859078590785907,0.58,0.667433831990794  

postprocessing v11_hsb_sw_filter:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488662  
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including Upper Sorbian stop-word extraction
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.8536585365853658,0.455,0.5936073059360731  

postprocessing v11_Itermax:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488663 (deprecated because of hsb sw filtering even though it leads to worse results), 5496303 (new)
notes:  
    - SimALign method: Itermax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.762532981530343,0.578,0.6575654152445961 (updated)

postprocessing v11_Match:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488664 (timeout), 5490757 (timeout), 5494165 (error: no GPU), 5496667 (new)
notes:  
    - SimALign method: Match  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.7905511811023622,0.502,0.6140672782874618 (updated)

postprocessing v11_no_CBIE:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5489980 (id of PaSeMiLL) --> see new folder execution_Belopsem_glot500_no_pretraining_v12
notes: 5490792 (deprecated because of hsb sw filtering even though it leads to worse results), 5496309 (err: no gpu), 5496686 (new)
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 

postprocessing v11_no_mean_subtraction:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488665 (deprecated because of hsb sw filtering even though it leads to worse results), 5496304 (err: no gpu), 5496683 (old hyperparameters), 5500077 (hyper parameter tuning)
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - new: 
        - see title of this section
Results Train: 0.09508974929535677,0.641,0.16561167807776772 (updated)

postprocessing v11_de_mean_subtraction:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5500260 (err: no gpu), 5500581
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - new: 
        - no HSB mean subtraction
Results Train: 

postprocessing v11_hsb_mean_subtraction:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5500261 (err: no gpu), 5500582
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - new: 
        - no DE mean subtraction
Results Train: 

postprocessing v11_no_sw_filter:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488666  
notes:  
    - SimALign method: Argmax  
    - nltk  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - new: 
        - see title of this section
Results Train: 

postprocessing v11_zero_punctuation:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5488667 (deprecated because of hsb sw filtering even though it leads to worse results), 5496305 (err: no gpu), 5496684 (new)
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended.py  
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - see title of this section
Results Train: 0.9492957746478873,0.337,0.49741697416974173 (updated)

postprocessing v11_word_instead_of_bpe:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5494240 (err: no gpu), 5496680 (new)
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended_de_sw_filter.py with "word" instead of "bpe" for SimAlign --> change that back when execution has finished
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences
    - compare with v1 (or v5_CBIE: v46 --> best run)
    - new: 
        - changed "bpe" to "word" for SimAlign initialization
Results Train: 

postprocessing v11_XLMR:
hyperparameter values:  
- window size: 7  
- min-segment-length: 0.35
- segment-threshold: 0.2  
- filtering-threshold: 0.38  
ID: 5496712 (err: wrong path) , 5499243 (err: wrong path), 5500599
notes:  
    - SimALign method: Argmax  
    - nltk  
    - including German stop-word extraction  
    - called unsuppse_simalign_fix_embeddings_extended_de_sw_filter_XLMR.py
    - created new mean vectors with XLMR instead of Glot500
    - Mean subtracting := subtract the mean vector for each language --> implemented this in the transfer_tknembedding_to_word_level_embedding() method
    - mean vector is calculated on all train data sentences    
    - new: 
        - changed Glot500 to XLMR
        - also for mean vector computation
Results Train: 