**Convolution neural network**
* CNN is *feedforward* neural network wich use *filters(or kernel)* optimization for data learning.
* Deep learning concept for *computer vision* and *image processing*
* *Filter* is small matrix of weight.
* *Convolution* is process when filter is slide on image by pixel. 
* *Shift invariant*/*space invariant* - if object on image shifted, after reprocessing and *sign map* will be shifted
* CNNs use relatively *little pre-processing compared* to other image classification algorithms. This means that the network learns to optimize the filters (or kernels) *through automated learning*, whereas in traditional algorithms these filters are hand-engineered

**Сonvolution layer**
*Input* convolution layer processing (clear image):
```
(number of inputs) × (input height) × (input width) × (input channels)
```
*Output*/*feature map* of convolution layer :
```
(number of inputs) × (feature map height) × (feature map width) × (feature map channels).
```

**Convolution layer** 
*Local/global pooling layer* is reduce the dimensions of data by combining the outputs of neuron clusters at one layer into a single neuron in the next layer.
*Max pooling* uses the maximum value of each local cluster of neurons in the feature map, while *average pooling* takes the average value
Generally use *ReLu* activation function

**Fully connected layers**
Like classic *MLP*
The flattened matrix goes through a fully connected layer to *classify the images*
Generally use *softmax*


**Deconvolution**
Is reverse of convolution neural nerwork princip
```
[x] -> |xx|
       |xx|
```
# LeNet vs AlexNet

![Reference](img\alexnet.png)

# QUESTION FOR KARL:
1) alwayse softmax/logsoftmax (difference) in out;