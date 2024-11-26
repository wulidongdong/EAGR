# EAGR
Resource for the TMM paper, [Error-Aware Generative Reasoning for Zero-Shot Visual Grounding](link).

## Introduction

We propose an Error-Aware Generative Reasoning (EAGR) method for zero-shot visual grounding. To address the limited adaptability of existing methods, a reasoning chain generator is presented, which prompts LLMs to dynamically generate reasoning chains for specific referring expressions. This generative manner eliminates the reliance on human-written heuristic rules. To mitigate visual perceptual errors of incomplete information, an error-aware mechanism is presented to elicit LLMs to identify these errors and explore correction strategies. Experimental results on four benchmarks show that EAGR outperforms state-of-the-art zero-shot methods by up to 10\% and an average of 7\%.

## Environment

Step1: Create environment and install packages:
conda env create -f EAGR.yml

Step2: Install GLIP
```
git clone https://github.com/sachit-menon/GLIP.git
cd GLIP
python setup.py clean --all build develop --user
pip install yacs
pip install timm
pip install einops
pip install ftfy
pip install dill
pip install omegaconf
pip install backoff
pip install openai
pip install numpy==1.23.5
```

Step 3: Download models: GLIP, MiDaS, and X-VLM
```
wget -P ./pretrained_models/GLIP/checkpoints https://huggingface.co/GLIPModel/GLIP/resolve/main/glip_large_model.pth
wget -P ./pretrained_models/GLIP/configs https://raw.githubusercontent.com/microsoft/GLIP/main/configs/pretrain/glip_Swin_L.yaml
wget -P ./pretrained_models/depth https://github.com/isl-org/MiDaS/releases/download/v3/dpt_large_384.pt
gdown "https://drive.google.com/u/0/uc?id=1bv6_pZOsXW53EhlwU0ZgSk03uzFI61pN" -O ./pretrained_models/xvlm/retrieval_mscoco_checkpoint_9.pth
```

## File Structure

pretrained_models: Store the downloaded pretrained models.
data: Store the data used for testing. The storage of each data set is in a.pth file.
main.ipynb: Code to run EAGR.
vision_models.py, vision_processes.py: API of vision models.
api.key: OpenAI key

## How to run

Step1: put your OpenAI key in api.key.

Step2: Follow the main.ipynb.
