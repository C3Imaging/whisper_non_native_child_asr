# Codebase
We followed the setup from whisper finetuning event for performing the ASR finetuning experiments with child speech. The training and finetuning details for replicating our experiments can be followed from the following link: https://github.com/huggingface/community-events/tree/main/whisper-fine-tuning-event

We also provide a more comprehensive understanding of the hyperparameter settings and training details for all our experiments on our Hugging Face repository which is accessible at https://huggingface.co/rishabhjain16

A comprehensive detail on the Whisper finetuning event is available on this blog: https://huggingface.co/blog/fine-tune-whisper. The tutorial for the above event can also be found on youtube: https://www.youtube.com/playlist?list=PLo2EIpI_JMQuKpnFm1ntcLKP6gq0l0f1Q. 

The training can also be used in a colab environment using the following link: https://colab.research.google.com/github/sanchit-gandhi/notebooks/blob/main/fine_tune_whisper.ipynb

# Dataset usage

1. If you are preparing your own dataset, please use the utils scripts first to prepare and clean the audio datasets. 

2. Additionally, after using the basic utils scripts to clean and prepare the audio dataset, the dataset can be further converted into Hugging face audio dataset format as follows: https://huggingface.co/docs/datasets/audio_dataset.

