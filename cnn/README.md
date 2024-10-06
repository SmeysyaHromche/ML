# Convolution neural network
* CNN is *feedforward* neural network wich use *filters(or kernel)* optimization for data learning.
* Deep learning concept for *computer vision* and *image processing*
* *Filter* is small matrix of weight.
* *Convolution* is process when filter is slide on image by pixel. 
* *Shift invariant*/*space invariant* - if object on image shifted, after reprocessing and *sign map* will be shifted
* CNNs use relatively *little pre-processing compared* to other image classification algorithms. This means that the network learns to optimize the filters (or kernels) *through automated learning*, whereas in traditional algorithms these filters are hand-engineered

### Image
To exploit the two-dimensional structure of image data to create inductive biases, we can use four interrelated concepts: *hierarchy, locality, equivariance, and invariance*
1 point : destruct image
2 point : find edge on local part of image
3 point in loop : climb the hierarchy for build and find more complex structures by past detected edges

## Сonvolution layer
*Input* convolution layer processing (clear image):
```
(number of inputs) × (input height) × (input width) × (input channels)
```
*Output*/*feature map* of convolution layer :
```
(number of inputs) × (feature map height) × (feature map width) × (feature map channels/count).
```
First point of filter/kernel is find pattern of detection feater in image edge provided for him by convolution.
Demensial of filter based on input obeject demesial size. For example for gray-scale image we can use 1-layer filter, for RGB 3-d-layer filter. In case where exist N-d-layer, ever chanel of input will be process byappropriated chanel of filter. After all feater map will be union to one feater map of filter.
Common output of convolution layer is N-d-array of feater maps, where ever d is output of one filter.

### Pooling
Pooling is process when we try extract infromation from featere map.In this part final point is equariances and invariances
*Equariance* is be sure that if arget object in image will move , *neaural network can detect it on ather position*. For it will be use *AVG pooling*, when we extract averege information about feature map.
*Invariance* is be sure that our neaural network *dont fixed on location, but on existing features*. For it will be use *MAX pooling*, when we extract maximum of information.
*Local/global pooling layer* is reduce the dimensions of data by combining the outputs of neuron clusters at one layer into a single neuron in the next layer. Provides us with invariative, nn *dont fixed on location, but on existing features*.

### Fully connected layers**
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
