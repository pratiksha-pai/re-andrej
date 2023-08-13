Skeleton of the lecture micrograd. I plan to use this in order to build it from scratch on my own.
Derivatives
- derivative of a function, chain rule, backpropagation, write notes
- get derivatives of a complex function if possible, here the derivatives should be written in terms of computation graphs
- sketch out these functions to understand what these functions are doing

Data Structure for the simple micrograd object
- add a class Value, init with just the data, repr, add and mul methods
- after this basic ops, we need to create a children, prev
- how would you initialize these? we need pointers to children from curr and pointer to curr from children. we also need to know what op is connecting them
- draw this computation graph (is there a better way than draw dot?) - learn a little about graphviz
- at this point give them labels (is there a better way to visualise them, wrt to the name of the variable, instead of label)
- for consistency use the formula, L = d * f; e = a*b; d = e+c; a= 2, b=-3, c=10, f=-2
- the nodes of the graph here indicate the weights of the NN? why?
- also do you understand what is the difference between a normal function and building out this funtion using a computational graph? 
why is this approach better? (works on a comp better than using direct math/a function? any other reason?)
- why does chain rule work? do you understand the intuition behind it? its basically multiplying the rates of change
- at this point you'd need self.grad to store the gradient of the current node (gradient of the current node wrt to the last node)
- (YOU HAVE A PRESENTATION DUE TOMO, STOP WATCHING LECTURES PLIS)
- skip the manual part of creating the grad on your own and write the code for it
- oooo mult swaps the grad values of children to the node value, why? use function xy to visualise this
- what is gradient check? 
- addition routes the gradient from parents to children whereas mult swaps then gradients with the node value of the other child 
- mult kinda couples the children together, addition doesn't (couples the gradients not the nodes?)
- 