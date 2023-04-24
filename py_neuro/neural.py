import os

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
        if  ( len(wmatrix) < 1 or (len(bvec)>0 and len(bvec)!=len(wmatrix[0]) ) ) :
            raise ValueError("wmatrix len should be greater than zero and if bvec len more than zero it should be equal to len wmatrix")
        self.wmatri = wmatrix
        self.bvec=bvec

    def F(X):
        pass

    def f(X):
        pass

    def S(X):
        pass

    pass
# class for load configuration
class nconstr:
    path = ""
    def __init__(self, path_to_config):
        if path_to_config is None or os.path.exists(path_to_config) == false:
            self.path = "./default.json"
        if os.path.exists(self.path) == False:
            raise ValueError("Got empty configuration file path and do not found config in workdir")
        
    def load():
        pass
    
    def check():
        pass
    
# class for loading model from bin file
class nloader:
    path = ""
    def __init__(self, path_to_config):
        if path_to_config is None or os.path.exists(path_to_config) == false:
            self.path = "./default.bin"
        if os.path.exists(self.path) == False:
            raise ValueError("Got empty configuration file path and do not found config in workdir")
    
    def load():
        pass
    
    def check():
        pass

# class that load configuration file and load binary files with weights
class nbuilder:
    pass
