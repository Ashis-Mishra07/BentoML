'''

For optimised model referencing -> service.py file 

This file helps in making entire API and swagger API .

'''


import numpy as np
import bentoml
from bentoml.io import NumpyNdarray  # This is like a wrapper on NumpyNdarray 


# Now ypu have make ur model , and specify what ur model will do .
iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()


# Now inside the array you have to add it with comma separated like
# first is data_conversion  , second is model_runner  , etc (any number of models )
svc = bentoml.Service("iris_classifier" , runners=[iris_clf_runner]) 

@svc.api(input=NumpyNdarray() , output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = iris_clf_runner.predict.run(input_series)
    return result