### generatively pre-trained transformer (GPT) - part 1
- Attention is all you need - https://arxiv.org/pdf/1706.03762.pdf
- sentencepiece by google - subword tokeniser
- tiktoken - "under the hood" GPT2 tokeniser
- the transformer will learn to predict the next word in a sequence depending on the previous word/s
- adam optimiser - https://arxiv.org/pdf/1412.6980.pdf
- torch.tril - lower triangular part of a matrix - used to average the attention weights
- isnt this extemely computationally expensive? 
- what is @ in pytorch? - matrix multiplication - how does it multiply for 3 dimensions? - https://pytorch.org/docs/stable/generated/torch.matmul.html