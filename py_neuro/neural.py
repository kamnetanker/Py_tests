# class for neural net managing
class nnet:
    layers=[] 
    def __init__(self, layers=[]):
        self.layers = layers
    def perform(self, input=[]):
        if(len(input)==0 or len(input)!=len(layers[0])):
            raise ValueError('input size should be equal to input layer size')
        # ToDo call nlayer perform
    pass
# class for neural net matrix container
class nlayer:
    wmatrix = []
    bvec = []
    input = []
    output = []
    def __init__(self, wmatrix=[[]], bvec=[]):
        if  ( len(wmatrix) < 1 or (len(bvec)>0 and len(bvec)!=len(wmatrix) ) ) :
            raise ValueError("wmatrix len should be greater than zero and if bvec len more than zero it should be equal to len wmatrix")

    pass
# class for load configuration
class nconstr:

    pass
# class for loading model from bin file
class nloader:

    pass
