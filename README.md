# bachelor_thesis
This repository contains the code for the Bachelor's thesis with the title "Parallel Sentence Mining in Low-Resource Scenarios through Segment-Level  Post-Processing".

## Setup
TODO

### Conda environment
TODO





## Pre-execution preparation (execution of PaSeMiLL pipeline)
Please execute the following instructions to prepare the post-processing.  

### Execute PaSeMiLL for reproducing results from Chapter 5.1 and Chapter 5.4
Please follow these steps to execute the PaSeMiLL pipeline:  
- To execute the PaSeMiLL pipeline without CBIE, use the following command:  

```bash
cd shell_scripts
sbatch run_PaSeMiLL_with_CBIE.sh
```

- To execute the PaSeMiLL pipeline with CBIE, use the following command:

```bash
cd shell_scripts
sbatch run_PaSeMiLL_no_CBIE.sh
```

A folder with the title `results_full_glot500/` will appear, containing the output from the PaSeMiLL pipeline in the `mining/bucc2017/hsb-de/` sub-folder.

### Mean vector generation

Execute the following command to compute the mean vector for each language.

```bash
cd shell_scripts
sbatch run_mean_vector_computation.sh
```

The mean vectors can be found in the `mean_vectors/` folder

### Stop-word generation

The `stop-words/` folder contains the self-generated stop-word list for Upper Sorbian (filename: `hsb_generated_stopwords_final.txt`).
The current version of the post-processing already includes this pre-computed list.  
If you want to execute the script anyways, please execute the following commands:

```bash
cd shell_scripts
sbatch run_hsb_stopword_generation.sh
```

Please note that the resulting list needs to be post-processed manually according to the procedure described in the thesis in order to obtain the list, which is already provided.





## Post-processing execution

The following paragraphs provide the commands necessary to recompute the results, presented in Chapter 5 of the thesis.

### Chapter 5.1: Best-performing post-processing (SimAlign)

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.1.sh
```


### Chapter 5.2: Changing the underlying language model (from Glot500 to XLM-R)


```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.2.sh
```



### Chapter 5.3.1: Algorithm

Itermax:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.3.1_Itermax.sh
```

Match:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.3.1_Match.sh
```

### Chapter 5.3.2: Token granularity

Word level:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.3.2_wordLvl.sh
```

### Chapter 5.5.1: Mean vector subtraction

No mean vector subtraction:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.5.1_no_subtraction.sh
```

### Chapter 5.5.2: Stop-word filtering

No stop-word filtering:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.5.2_no_stopword_filtering.sh
```

Stop-word filtering for the source language (here: Upper Sorbian)

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.5.2_src_stopword_filtering.sh
```

Stop-word filtering for both the source and the target language:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.5.2_src_trg_stopword_filtering.sh
```

### Chapter 5.5.3: Punctuation handling

Exclude punctuation marks in sentences:

```bash
cd shell_scripts
sbatch execute_postprocessing_simalign_chap_5.5.3_excl_punctuation.sh
```


### Post-processing (fast_align)

In order to execute the post-processing using fast_align instead of SimAlign, execute the following steps:

#### Create input

The required input format for the fast_align tool can be created by executing the following commands:

```bash
cd scripts
python fast_align_create_input.py \
  --mapping-train "../all_executions/re-computation_folder/results_full_glot500/mining/bucc2017/hsb-de/glot500.hsb-de.train.sim.pred" \
  --src-train "../data/bucc_style_data/hsb-de/hsb-de.train.hsb" \
  --trg-train "../data/bucc_style_data/hsb-de/hsb-de.train.de" \
  --mapping-test "../all_executions/re-computation_folder/results_full_glot500/mining/bucc2017/hsb-de/glot500.hsb-de.test.sim.pred" \
  --src-test "../data/bucc_style_data/hsb-de/hsb-de.test.hsb" \
  --trg-test "../data/bucc_style_data/hsb-de/hsb-de.test.de" \
  --model-path "cis-lmu/glot500-base" \
  --output "../fast_align_input_output/hsb-de/input_fast_align.txt"
```


#### Execute fast_align

1. Clone [fast_align](https://github.com/clab/fast_align) into the `tools/` folder
2. Compile fast_align according to the [README](https://github.com/clab/fast_align/blob/master/README.md) of the fast_align repository
3. execute fast_align (pass the previously created input file as argument) with the corresponding instructions of fast_align [README](https://github.com/clab/fast_align/blob/master/README.md) file


#### Filter alignment pairs

To filter the output of fast_align, execute the following commands from the root directory of this repository:

```bash
python fast_align_filter_output.py \
  --corpus fast_align_input_output/hsb-de/input_fast_align.txt \
  --alignments fast_align_input_output/hsb-de/forward.align \
  --output fast_align_input_output/hsb-de/output_filtered_src_to_trg.align \
  --threshold 0.01
```

and 

```bash
python fast_align_filter_output.py \
  --corpus fast_align_input_output/hsb-de/input_fast_align.txt \
  --alignments fast_align_input_output/hsb-de/reverse.align \
  --output fast_align_input_output/hsb-de/output_filtered_trg_to_src.align \
  --threshold 0.01
```

The Dice threshold can be changed within the command.


#### Execute post-processing using fast_align

To execute the post-processing with fast_align instead of SimAlign, execute the following steps:

```bash
cd shell_scripts
sbatch execute_postprocessing_fast_align_chap_5.1.sh
```



## Notes
!!! TODO: check if this is okay !!!  
Please note that this repository contains code from [PaSeMiLL](https://github.com/shuokabe/PaSeMiLL) with slight adjustments in order to make the usage of the post-processing easier. The `code/` folder contains this code. 
Furthermore, the `data/` folder contains the data for the Upper Sorbian-German langauge pair, proposed by [Belopsem](https://github.com/shuokabe/Belopsem).
