- the bigram - context is the previous word
### Bengio et al 2003
- every word is embedded in a 30 dimensional vector
- the vectors move around, and words that mean similar things are close together 
- MLP to predict the next word, given the previous word, by maximising the log likelihood of the training data
- cross entropy loss function is nothing but the average negative log likelihood
- why use cross entropy instead of writing it on your own - because it is numerically stable, not much memory
- how are logits calculated in cross entropy loss? 
- train, def/validation, test split - 80/10/10
- when dev loss and trainign loss are roughly the same, it means that the model is not overfitting, meaning that the model is not memorising the training data, meaning we can train for more epochs/scale the model/try fitting it a little more
- 


questions:
- plot of learning rate vs loss - lri is changed but the loss magnitude is also changing, wont it affect the plot? (or does it matter?) - late stages of learning during training is assigneda higher learning rate than the early stages of learning - does this accuractely find out what the learning rate should be?
- why do we only take the negative log likelihood of the correct word? should we not take the negative log likelihood of all the words in the vocabulary? - wont that penalise the rest of the words more? https://youtu.be/TCH_1BHY58I?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&t=1927
- 