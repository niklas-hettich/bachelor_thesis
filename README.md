# bachelor_thesis
This repository contains the code for the Bachelor's thesis with the title "Parallel Sentence Mining in Low-Resource Scenarios through Segment-Level  Post-Processing".

## Setup
Before running the scripts, please ensure that you have [Conda](https://docs.conda.io/en/latest/) installed on your system or cluster. 

### Conda environment

To ensure full reproducibility, all necessary dependencies (including deep learning frameworks, NLP libraries, and specific versions) are specified in the `environment.yml` file. 

You can recreate and activate the environment by executing the following commands from the root directory of this repository:

```bash
conda env create -f environment.yml
conda activate bachelor_thesis_env
```


## Pre-execution preparation (execution of PaSeMiLL pipeline)
Please execute the following instructions to prepare the post-processing.  
Note: The shell scripts use SLURM (`sbatch`). Please adjust the `#SBATCH` directives in the `.sh` files according to your cluster's configuration before executing them.  

### Execute PaSeMiLL for reproducing results from Chapter 5.1 and Chapter 5.4
Please follow these steps to execute the PaSeMiLL pipeline:  
- To execute the PaSeMiLL pipeline without CBIE, use the following command:  

```bash
cd shell_scripts
sbatch run_PaSeMiLL_no_CBIE.sh
```

- To execute the PaSeMiLL pipeline with CBIE, use the following command:

```bash
cd shell_scripts
sbatch run_PaSeMiLL_with_CBIE.sh
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

TODO

## Citations and Licences

### Data

The `data/` folder contains the dataset for the Upper Sorbian-German language pair (`hsb-de`), originally introduced in the [Belopsem](https://github.com/shuokabe/Belopsem) repository. 
In accordance with the original repository, this dataset is licensed under the **[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)** license. 

If you use this dataset, please cite the following paper:
```bibtex
@inproceedings{okabe-etal-2025-improving,
    title = "Improving Parallel Sentence Mining for Low-Resource and Endangered Languages",
    author = {Okabe, Shu  and
      H{\"a}mmerl, Katharina  and
      Fraser, Alexander},
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-short.17/",
    doi = "10.18653/v1/2025.acl-short.17",
    pages = "196--205",
    ISBN = "979-8-89176-252-7",
}
```

### Code and Methodology

Please note that the `code/` folder contains code from [PaSeMiLL](https://github.com/shuokabe/PaSeMiLL) with slight adjustments in order to make the usage of the post-processing easier. Please cite usage of this code according to the [PaSeMiLL README](https://github.com/shuokabe/PaSeMiLL/blob/main/README.md) file.


The post-processing segment extraction pipeline is an independent re-implementation based on the [UnsupPSE](https://github.com/hangyav/UnsupPSE) algorithm:

```bibtex
@inproceedings{hangya-fraser-2019-unsupervised,
    title = "Unsupervised Parallel Sentence Extraction with Parallel Segment Detection Helps Machine Translation",
    author = "Hangya, Viktor  and
      Fraser, Alexander",
    editor = "Korhonen, Anna  and
      Traum, David  and
      M{\`a}rquez, Llu{\'i}s",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P19-1118/",
    doi = "10.18653/v1/P19-1118",
    pages = "1224--1234",
    abstract = "Mining parallel sentences from comparable corpora is important. Most previous work relies on supervised systems, which are trained on parallel data, thus their applicability is problematic in low-resource scenarios. Recent developments in building unsupervised bilingual word embeddings made it possible to mine parallel sentences based on cosine similarities of source and target language words. We show that relying only on this information is not enough, since sentences often have similar words but different meanings. We detect continuous parallel segments in sentence pair candidates and rely on them when mining parallel sentences. We show better mining accuracy on three language pairs in a standard shared task on artificial data. We also provide the first experiments showing that parallel sentences mined from real life sources improve unsupervised MT. Our code is available, we hope it will be used to support low-resource MT research."
}
```

### Language Models and Alignment Tools

This repository relies on several external tools and pre-trained language models via the Hugging Face transformers library. Please consider citing the respective authors if you use them:

#### Language Models

- Glot500: Ayyoob Imani, Peiqin Lin, Amir Hossein Kargaran, Silvia Severini, Masoud Jalili Sabet, Nora Kassner, Chunlan Ma, Helmut Schmid, André Martins, François Yvon, and Hinrich Schütze. 2023. Glot500: Scaling Multilingual Corpora and Language Models to 500 Languages. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1082–1117, Toronto, Canada. Association for Computational Linguistics. [Link](https://aclanthology.org/2023.acl-long.61/)

- XLM-R: Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised Cross-lingual Representation Learning at Scale. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 8440–8451, Online. Association for Computational Linguistics. [Link](https://aclanthology.org/2020.acl-main.747/)

#### Word alignment

This repository also relies on the following tools for word alignments. Please consider citing them if you use this pipeline:

- SimAlign: Masoud Jalili Sabet, Philipp Dufter, François Yvon, and Hinrich Schütze. 2020. SimAlign: High Quality Word Alignments Without Parallel Training Data Using Static and Contextualized Embeddings. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 1627–1643, Online. Association for Computational Linguistics. [Link](https://aclanthology.org/2020.findings-emnlp.147/)  

- fast_align: Chris Dyer, Victor Chahuneau, and Noah A. Smith. 2013. A Simple, Fast, and Effective Reparameterization of IBM Model 2. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 644–648, Atlanta, Georgia. Association for Computational Linguistics. [Link](https://aclanthology.org/N13-1073/)  






