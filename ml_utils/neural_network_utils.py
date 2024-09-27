import torch.nn as nn
from typing import List
def activation_decode(act_f_str:str):
            if act_f_str == 'identity':
                return nn.Identity()
            elif act_f_str == 'sig':
                return nn.SiLU()
            else:
                return nn.ReLU()