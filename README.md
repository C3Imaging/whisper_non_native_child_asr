# Experimental analysis on finetuning large scale supervision to improve the Non-Native English Child speech recognition.

## Abstract

Modern End-to-End Automatic Speech Recognition (ASR) systems struggle recognizing children's speech due to limited child training data and high acoustic variability of child speech, particularly in low-resource languages. This study focuses on improving the performance of ASR on non-native English child speech datasets publicly available for research. We evaluate the performance of the large-scale Whisper models trained with 680,000 hours of adult speech data on child speech. We also perform multiple finetuning experiments using different child speech datasets combinations to study their effect on ASR performance for non-native English child speech recognition. Our approach outperformed previously reported State-Of-The-Art (SOTA) results on the same datasets.

## Table of Results with Checkpoints

### Table 3: WER for Whisper Original and Finetuned Models over different child speech datasets used in the paper.

**NOTE1:** Model IDs are links to the corresponding models on either OpenAI's HuggingFace page (Group A) or our HuggingFace page (Groups B-F). All of the models are openly available.<br /><br />
**NOTE2:** A Tensorboard page of all the training and evaluation metrics for each model can be found under the "Training metrics" tab after clicking on a model link.<br /><br />
**DISCLAIMER:** The child audio datasets used in this paper are subject to licensing agreements, therefore we cannot make them publicly available. For researchers wishing to recreate our experiments, please purchase the licenses required for the original datasets from the publishers and upon providing proof of license, we can share our preprocessed versions.

| **Model ID**   | **Whisper Pretraining Model** | **MyST_test** | **PF_br_test** | **CMU_test** | **PF_sw_test** | **PF_ge_test** | **PF_it_test** | **SO_test** | **Dev_clean** |
| :---    | :------ | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| **<ins>Group A:</ins> No-Finetuning:** |
| [**1**](https://huggingface.co/openai/whisper-tiny) | Tiny | 40.09 | 159.57 | 24.62 | 55.32 | 103.68 | 70.57 | 64.83 | 10.85 |
| [**2**](https://huggingface.co/openai/whisper-tiny.en) | Tiny.en | 33.02 | 47.11 | 16.25 | 45.23 | 89.8 | 47.22 | 51.28 | 8.62 |
| [**3**](https://huggingface.co/openai/whisper-base) | Base | 32.14 | 100.07 | 16.65 | 53.88 | 126.84 | 50.29 | 60.39 | 8.14 |
| [**4**](https://huggingface.co/openai/whisper-base.en) | Base.en | 29.15 | 45.7 | 15.01 | 37.29 | 93.77 | 46.84 | 38.47 | 7.18 |
| [**5**](https://huggingface.co/openai/whisper-small) | Small | 26.22 | 111.75 | 9.3 | 60.81 | 86.72 | 44.09 | 36.19 | 6.43 |
| [**6**](https://huggingface.co/openai/whisper-small.en) | Small.en | 26.72 | 39.0 | 8.64 | 32.26 | **71.04** | 33.38 | 30.33 | 6.06 |
| [**7**](https://huggingface.co/openai/whisper-medium) | **Medium** | **25.11** | 80.97 | **7.48** | 35.07 | 105.82 | **45.65** | 37.0 | **5.58** |
| [**8**](https://huggingface.co/openai/whisper-medium.en) | **Medium.en** | 28.06 | **35.25** | **7.17** | **27.91**  | **80.4** | **25.94** | **25.29** | 6.2 |
| [**9**](https://huggingface.co/openai/whisper-large) | Large | 25.24 | 84.52 | 7.56 | 33.09 | 79.14 | 51.82 | 37.25 | 5.53 |
| [**10**](https://huggingface.co/openai/whisper-large-v2) | **Large-V2** | **25.0** | 73.68 | **6.86** | **29.99** | **77.56** | **34.97** | **29.39** | **5.4** |
| **<ins>Group B:</ins> MyST_train Finetuning:** |
| [**11**](https://huggingface.co/rishabhjain16/whisper_medium_to_myst55h) | Medium | **11.66** | 19.76 | 9.43 | 34.18 | **62.4** | 24.53 | 24.89 | 5.62 |
| [**12**](https://huggingface.co/rishabhjain16/whisper_medium_en_to_myst55h) | Medium.en | 11.81 | 17.83 | **9.13** | **23.63** | 76.84 | 19.99 | 25.45 | 6.48 |
| [**13**](https://huggingface.co/rishabhjain16/whisper_large_v2_to_myst55h) | Large-V2 | 12.28 | **10.88** | 9.8 | 25.56 | 65.58 | **23.48** | **25.05** | **4.82** |
| **<ins>Group C:</ins> MyST_train + CMU_train Finetuning:** |
| [**14**](https://huggingface.co/rishabhjain16/whisper_medium_to_myst_cmu) | Medium | 12.14 | 41.83 | 4.46 | 158.75 | 113.07 | 125.05 | 33.24 | 6.1 |
| [**15**](https://huggingface.co/rishabhjain16/whisper_medium_en_to_myst_cmu) | Medium.en | **12.10** | 31.29 | 2.27 | 138.95 | 125.37 | 77.38 | 33.32 | 6.13 |
| [**16**](https://huggingface.co/rishabhjain16/whisper_large_v2_to_myst_cmu) | Large-V2 | 12.37 | **23.62** | **2.32** | 184.24 | 211.01 | 180.79 | 48.34 | **4.81** |
| **<ins>Group D:</ins> MyST_train + CMU_train + PF_br_train Finetuning:** |
| [**17**](https://huggingface.co/rishabhjain16/whisper_medium_to_myst_cmu_pf) | Medium | 11.72 | 3.11 | 2.36 | 23.94 | 86.13 | 16.72 | 27.88 | 5.62 |
| [**18**](https://huggingface.co/rishabhjain16/whisper_medium_en_to_myst_cmu_pf) | Medium.en | **11.71** | 3.02 | 2.23 | 21.65 | **68.1** | **15.87** | **26.43** | 5.57 |
| [**19**](https://huggingface.co/rishabhjain16/whisper_large_v2_to_myst_cmu_pf) | Large-V2 | 12.37 | **3.1** | **1.86** | 43.34 | 71.18 | 56.29 | 32.99 | **4.75** |
| **<ins>Group E:</ins> MyST_train + CMU_train + PF_br_train + Others_train_50 Finetuning:** |
| [**20**](https://huggingface.co/rishabhjain16/whisper_medium_to_myst_cmu_pf_ot50) | Medium | 12.75 | 3.11 | **1.98** | **8.99** | 36.67 | **5.14** | **16.09** | 6.09 |
| [**21**](https://huggingface.co/rishabhjain16/whisper_medium_en_to_myst_cmu_pf_ot50) | Medium.en | 12.35 | 3.42 | 2.06 | 9.04 | 35.92 | 5.84 | 17.55 | 5.28 |
| [**22**](https://huggingface.co/rishabhjain16/whisper_large_v2_to_myst_cmu_pf_ot50) | Large-V2 | **11.73** | **3.13** | 2.56 | 9.67 | **35.05** | 5.51 | 15.83 | **4.69** |
| **<ins>Group F:</ins> MyST_train + CMU_train + PF_br_train + Others_train_100 Finetuning:** |
| [**23**](https://huggingface.co/rishabhjain16/whisper_medium_to_myst_cmu_pf_ot100) | Medium | 12.55 | 3.09 | 1.96 | **7.66** | 34.77 | **4.11** | **14.31** | 6.06 |
| [**24**](https://huggingface.co/rishabhjain16/whisper_medium_en_to_myst_cmu_pf_ot100) | Medium.en | 11.88 | 3.28 | 1.98 | 8.16 | 34.99 | 4.65 | 15.87 | 5.15 |
| [**25**](https://huggingface.co/rishabhjain16/whisper_large_v2_to_myst_cmu_pf_ot100) | Large-V2 | **11.62** | **2.84** | **1.75** | 8.36 | **34.26** | 4.4 | 14.52 | **4.53** |


**Training Hyperparameters:** (common used for all finetuning experiments)
- Learning Rate: 1e-05
- Optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- Learning rate scheduler type: Linear
- Learning rate scheduler warmup steps: 500
- Training steps: 4000
