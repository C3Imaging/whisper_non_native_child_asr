# Experimental analysis on finetuning large scale supervision to improve the Non-Native English Child speech recognition.

## Abstract

Modern End-to-End Automatic Speech Recognition (ASR) systems struggle recognizing children's speech due to limited child training data and high acoustic variability of child speech, particularly in low-resource languages. This study focuses on improving the performance of ASR on non-native English child speech datasets publicly available for research. We evaluate the performance of the large-scale Whisper models trained with 680,000 hours of adult speech data on child speech. We also perform multiple finetuning experiments using different child speech datasets combinations to study their effect on ASR performance for non-native English child speech recognition. Our approach outperformed previously reported State-Of-The-Art (SOTA) results on the same datasets.

## Table of Results with Checkpoints

### Table 3: WER for Whisper Original and Finetuned Models over different child speech datasets used in the paper.

| **Model ID**   | **Whisper Pretraining Model** | **MyST_test** | **PF_br_test** | **CMU_test** | **PF_sw_test** | **PF_ge_test** | **PF_it_test** | **SO_test** | **Dev_clean** |
| :---    | :------ | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| **Group A: No-Finetuning:** |
| **1** | Tiny | 40.09 | 159.57 | 24.62 | 55.32 | 103.68 | 70.57 | 64.83 | 10.85 |
| **2** | Tiny.en | 33.02 | 47.11 | 16.25 | 45.23 | 89.8 | 47.22 | 51.28 | 8.62 |
| **3** | Base | 32.14 | 100.07 | 16.65 | 53.88 | 126.84 | 50.29 | 60.39 | 8.14 |
| **4** | Base.en | 29.15 | 45.7 | 15.01 | 37.29 | 93.77 | 46.84 | 38.47 | 7.18 |
| **5** | Small | 26.22 | 111.75 | 9.3 | 60.81 | 86.72 | 44.09 | 36.19 | 6.43 |
| **6** | Small.en | 26.72 | 39.0 | 8.64 | 32.26 | **71.04** | 33.38 | **30.33** | 6.06 |
| **7** | **Medium** | **25.11** | 80.97 | **7.48** | 35.07 | 105.82 | **45.65** | 37.0 | **5.58** |
| **8** | **Medium.en** | 28.06 | **35.25** | **7.17** | **27.91**  | **80.4** | **25.94** | **25.29** | 6.2 |
| **9** | Large | 25.24 | 84.52 | 7.56 | 33.09 | 79.14 | 51.82 | 37.25 | 5.53 |
| **10** | **Large-V2** | **25.0** | 73.68 | **6.86** | **29.99** | **77.56** | **34.97** | **29.39** | **5.4** |
| **Group B: MyST_train Finetuning:** |
| **11** | Medium | **11.66** | 19.76 | 9.43 | 34.18 | **62.4** | 24.53 | 24.89 | 5.62 |
| **12** | Medium.en | 11.81 | 17.83 | **9.13** | **23.63** | 76.84 | 19.99 | 25.45 | 6.48 |
| **13** | Large-V2 | 12.28 | **10.88** | 9.8 | 25.56 | 65.58 | **23.48** | **25.05** | **4.82** |
| **Group C: MyST_train + CMU_train Finetuning:** |
| **14** | Medium | 12.14 | 41.83 | 4.46 | 158.75 | 113.07 | 125.05 | 33.24 | 6.1 |

