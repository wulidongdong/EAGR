# EAGR
Resource for the TMM paper, Error-Aware Generative Reasoning for Zero-Shot Visual Grounding.

## Introduction

We propose an Error-Aware Generative Reasoning (EAGR) method for zero-shot visual grounding. This method prompts LLMs to generate visual grounding reasoning chains. To mitigate visual perceptual errors of incomplete information, this method incorporates an error-aware mechanism that elicits LLMs to identify these errors and explore potential correction strategies, thus avoiding cascading errors.

## Environment

### Step 1: Create an environment and install packages
```
conda env create -f EAGR.yml
```

### Step 2: Install GLIP and MiDas
```
git clone https://github.com/isl-org/MiDaS.git
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

### Step 3: Download models (GLIP, MiDaS, and X-VLM)
```
wget -P ./pretrained_models/GLIP/checkpoints https://huggingface.co/GLIPModel/GLIP/resolve/main/glip_large_model.pth
wget -P ./pretrained_models/GLIP/configs https://raw.githubusercontent.com/microsoft/GLIP/main/configs/pretrain/glip_Swin_L.yaml
wget -P ./pretrained_models/depth https://github.com/isl-org/MiDaS/releases/download/v3/dpt_large_384.pt
gdown "https://drive.google.com/u/0/uc?id=1bv6_pZOsXW53EhlwU0ZgSk03uzFI61pN" -O ./pretrained_models/xvlm/retrieval_mscoco_checkpoint_9.pth
```

### Step 4: Download images
We create sub-test sets sampled from the RefCOCO, RefCOCO+, and RefCOCOg datasets, with their annotations stored in the `./data` folder. The data originates from https://github.com/lichengunc/refer. Please refer to that repository to download COCO images and place them in the `./data/images` folder.

## File Structure

- pretrained_models: Store the downloaded pretrained models.
- data: Store the data used for testing. The storage of each data set is in a.pth file.
- configs: config file.
- base_models, vision_models.py, vision_processes.py: API of vision models.
- prompts: prompts.
- useful_lists, utils.py: util functions.
- main.ipynb: Code to run EAGR.
- api.key: OpenAI key

## How to run

Step 1: put your OpenAI key in api.key.

Step 2: Follow the main.ipynb.

## Citation
If you find this resource helpful, please cite our paper and share our work. Thank you.
```bibtex
@article{tmm/Bu2024/scenetext,
  author={Yuqi Bu and Xin Wu and Yi Cai and Qiong Liu and Tao Wang and Qingbao Huang},
  title={Error-Aware Generative Reasoning for Zero-Shot Visual Grounding},
  journal={{IEEE} Transactions on Multimedia},
  year={2024},
}
```

## Acknowledgment
We sincerely thank the authors of [ViperGPT](https://github.com/cvlab-columbia/viper) and [RefCOCO](https://github.com/lichengunc/refer) for kindly sharing their datasets and code.
