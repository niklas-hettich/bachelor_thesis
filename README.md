# bachelor_thesis
This repository contains the code for the Bachelor's thesis with the title "Parallel Sentence Mining in Low-Resource Scenarios through Segment-Level  Post-Processing".

## Setup

TODO

### Conda environment

TODO

## Pre-execution preparation (execution of PaSeMiLL pipeline)

Please execute the following instructions to prepare the post-processing.

### Execute PaSeMiLL for reproducing results from Chapter 5.1

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

### Best-performing post-processing (SimAlign)

TODO

```bash
cd shell_scripts
sbatch run_postprocessing_simalign.sh
```

### Other configurations post-processing (SimAlign)

TODO

### Post-processing (fast_align)

TODO  
TODO: add the notes.md file for the steps required to prepare fast_align (5 steps) --> should I include fast_align and compile it already?



## Notes
!!! TODO: check if this is okay !!!  
Please note that this repository contains code from [PaSeMiLL](https://github.com/shuokabe/PaSeMiLL) with slight adjustments in order to make the usage of the post-processing easier. The `code/` folder contains this code. 
Furthermore, the `data/` folder contains the data for the Upper Sorbian-German langauge pair, proposed by [Belopsem](https://github.com/shuokabe/Belopsem).
