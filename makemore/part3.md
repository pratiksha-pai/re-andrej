### activations, gradients, batchnorm 
- what is decorator in pytorch? torch.no_grad
- what is a logit in the last layer of a NN? - it is the output of the last layer before the activation function is applied
- loss = negative log likelihood is calculated by getting the negative log likehood assigned for the correct word
- dead neuron - when the neuron is not learning/activated because the gradient is 0 (self.grad is 0, ex for tanh/other activation when the derivative is 0)
- torch int kaiming_normal - what is fan_in and fan_out? - fan_in is the number of inputs to the layer, fan_out is the number of outputs from the layer
- batch normalistion - at initialisation - normalise the hidden states to be gaussian  
- do we update the NN during dev/validation? - No, only during training
- we add a batch norm layer after pre activation function (before activation function) in order to normalise the data
- batch normalisation - here the batch is kinda adding some entrpy to the data, so we need to add some noise to the data in order to make it more robust - also acts like regularisation
- in order to remove this property of coupling the batches some other normalisation techs are used - like layer normalisation, instance normalisation, group normalisation
- bnbias is used hence we dont need to add bias to the linear layer
- why do we need non linearity - in order to represent non linear functions
- momentum for batchnorm1d - what is it? - it is the momentum for the running mean and running variance - meaning how much of the previous mean and variance to keep
- for small batch size it is better to use a small momentum value and for large batch size it is better to use a large momentum value - WHY? THINK THROUGH 
- what is stochastic gradient descent? - it is when we use a batch of data to calculate the gradient and update the weights
- context manager - with torch.no_grad() - what is it? - it is a way to use the torch.no_grad() decorator without having to use the decorator
- what is cross entropy loss? - it is the negative log likelihood loss - it is used for classification problems
- why are tanh called squashing functions? - because they squash the input between -1 and 1
- how is the gain affecting output of tanh layer, the linear layer, and the gradient distribution? - the gain is affecting the output of the tanh layer by scaling the output of the tanh layer by the gain, the linear layer by scaling the output of the linear layer by the gain, and the gradient distribution by scaling the gradient by the gain?
- dpes not matter how any linear layers we have, we can always combine them into one linear layer - why? - because we can always combine the weights of the linear layers into one weight matrix
- this is the reason we use tanh 
- multiple linear layers stacked on top of each other is the same as one linear layer in the forward pass but have different optimisations for the backward pass - why?

questions:
- go through this part - https://youtu.be/P6sfmUTpUmc?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&t=494
- in order to get the std to be 1, we need to normalise the data - by fividing it by the square root of nin (number of inputs) - why?
- why do we add torch.no_grad for functions, arent the grads calculated for variables? (parameters) hence it does not matter if we dont add that decorator?
- batchnorm1d do we use track_running_stats is false and momentum some value (momentum is of no use when track_running_stats is false)

papers/refs mentioned:
- devling deep into rectufiers - kaming he et al - https://arxiv.org/pdf/1502.01852.pdf
- batch normalisation - https://arxiv.org/pdf/1502.03167.pdf
- resnet pytorch - https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py
