import numpy as np

class Network(object):

    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.rand(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x, y in zip(sizes[:-1],sizes[1:])]



if __name__=="__main__":
    NN = Network([10,10,10])
    print(NN.biases)
    print(NN.weights)