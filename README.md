# Experimental analysis on finetuning large scale supervision to improve the Non-Native English Child speech recognition.

## Abstract

Modern End-to-End Automatic Speech Recognition (ASR) systems struggle recognizing children's speech due to limited child training data and high acoustic variability of child speech, particularly in low-resource languages. This study focuses on improving the performance of ASR on non-native English child speech datasets publicly available for research. We evaluate the performance of the large-scale Whisper models trained with 680,000 hours of adult speech data on child speech. We also perform multiple finetuning experiments using different child speech datasets combinations to study their effect on ASR performance for non-native English child speech recognition. Our approach outperformed previously reported State-Of-The-Art (SOTA) results on the same datasets.

## Table of Results with Checkpoints

### Table 3: WER for Whisper Original and Finetuned Models over different child speech datasets used in the paper.

| **Model ID**   | **Whisper Pretraining Model** | **MyST_test** | **PF_br_test** | **CMU_test** | **PF_sw_test** | **PF_ge_test** | **PF_it_test** | **SO_test** | **Dev_clean** |
| :---    | :------ | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| **Group A: No-Finetuning:** |
| **1** | Tiny | 
40.09 
	

159.57 
	

24.62 
	

55.32 
	

103.68 
	

70.57 
	

64.83 
	

10.85 
