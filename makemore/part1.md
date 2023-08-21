### learn LLMs - makemore
- ex isabella, here i is more likely going to be the start word, s is going to likely follow i, a follows is, and note a is more likely going to the end word
- ? bigram model: p(w1, w2, w3, w4) = p(w1) * p(w2|w1) * p(w3|w2) * p(w4|w3)
- for bigram model you can use the zip function to iterate over the bigrams
- wrap the word with start and end characters, this is so we can model the probability of the first word and the last word
- why is generally get() used instead of map[item] - because in get function we can add a default value 
- N[0, :] - this is the first row of the matrix
- generator - this is a function that returns a sequence of values for a given seed value
- torch.multinomial - this is a function that takes a vector of probabilities and returns a random index based on the probabilities
-  for bigram model - parameters are simply the probabilities of each word given the previous word, loss is the negative log likelihood of the next word given the previous word, maximising the likelihood is the same as minimising the negative log likelihood/average negative log likelihood
- model smoothing - add a small value to each count to avoid zero probabilities, inf negative log likelihoods

using NN to learn the bigram model
- why one hot encoding? - because we want to represent each word as a vector of size vocab_size, and we want to have a 1 at the index of the word and 0s everywhere else, why because encoding it as integer does nit make sense
- x_enc = F.one_hot(x, vocab_size).float() - this is how you one hot encode a tensor - make sure the dtype is float - because we are going to multiply it with a float matrix in the NN 
- randn - this is a function that returns a tensor of random numbers from a normal distribution with mean 0 and std 1
- logits - are log counts - which are then exponentiated to get the counts - which are then normalised to get the probabilities
- softmax - is nothing but exponentiation of the logits divided by the sum of the exponentiated logits
- in order to have a backpropable loss function we need to have a differentiable function
- mse - for regression problems, cross entropy or negative log likelihood for classification problems
- remember - gradient is the direction at which the function increases the most, so we want to go in the opposite direction of the gradient to minimise the loss - meaning, get the negative gradient
- function backward() - this is the function that calculates the gradients of the loss with respect to the parameters (does not do the actual gradient descent)
- for calculating in a bigram you dont need to initialise the network with the max length of the word, because we care only about the previous word, so we can initialise the network with the vocab size
- logits = xenc * W - here since xenc is a one hot encoded vector, we are simply selecting the row of the matrix that corresponds to the word - meaning we are plucking the row of the matrix for that character which gives the probability distribution of the next word
- why do we add regularisation? - because we want to avoid overfitting, we want the model to generalise well to unseen data
- acc to andrej - we are trying the push W towards 0, when we do a W.mean() we are accumulating losses, hence trying to push W towards 0
- regularisation increases uniform prediction


questions/learn:
- why are bigram sums same across rows and columns? 
- fstrings = f'{var=}' - this is a new feature in python 3.8? 
- learn broadcast rules in pytorch
- probabilty basics - ( bayes rule, conditional probability, chain rule, marginalization, independence )
- linear algebra concepts - eigen values, eigen vectors, matrix multiplication, matrix inverse, matrix transpo
- learn what torch.multinomial does 