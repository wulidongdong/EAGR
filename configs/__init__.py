import os
from omegaconf import OmegaConf

configs = [OmegaConf.load('configs/base_config.yaml')]
config = OmegaConf.unsafe_merge(*configs)