# Reccurent neural networks
Recurrent neural networks (RNNs) are a class of artificial neural networks for sequential data processing. Unlike feedforward neural networks, which process data in a single pass, RNNs *process data across multiple time steps*, making them well-adapted for modelling and processing text, speech, and time series.

Grow block of RNN is *recurrent unit*. This unit maintains a *hidden state* wich we can represent as memmory about past state of input data. After processing input data in loop, network change state based on correlation between past time data and presents.
Basci RNN have porblem *vanishing gradient* where loss memmory about longtime input data, it solved by *LSTM*.

Using: in audo/speech processing/recognizing, time data processing (economics) atd.

### Formal definition
```
Function f_o is function of tipe (x_t, h_t, y_t) -> (y_t, h_t,+1):
x_t : input vector on time step t (actual data on processing for example actual word)
h_t : hidden state on time step t (imformation about steps in range [0, t), will be updated after step)
y_t : output vector (for example probability for ever word in dict)
o   : neural networks parametrs
```
### Input x Output relation
|Type relation|Application|
|-------------|-----------|
|*one to one*|image classification|
|*one to many*|image captioning|
|*many to one*|sentiment classification|
|*many to many*|machine translation|
|*many to many*|video classification|
### Activation function
Often use *tangh* for safe symetric by yaxis (plus negative value from x)

# My questions:
Activation function,
Normalization of data