import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

filename = 'C:/Users/misl7603/Example/Sample.ipynb'
with open(filename) as ff:
    nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
    
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

nb_out = ep.preprocess(nb_in)