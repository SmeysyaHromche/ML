import torch.nn as nn
from torchvision import datasets
from typing import List
def decode_activation(act_f_str:str):
            if act_f_str == 'identity':
                return nn.Identity()
            elif act_f_str == 'silu':
                return nn.SiLU()
            elif act_f_str == 'sig':
                  return nn.Sigmoid()
            else:
                return nn.ReLU()
            
def decode_dataset(name:str):
    if name == 'mnist':
        return datasets.MNIST
    elif name == 'cifar10':
        return datasets.CIFAR10
    elif name == 'imgnet':
        return datasets.ImageNet
    else:
        raise Exception(f'Unknow dataset with name {name}') 