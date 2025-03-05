# BentoML - Machine Learning Model Deployment

## Overview
BentoML is an open-source framework designed to simplify the deployment of machine learning models. It provides a standardized way to package, distribute, and serve models efficiently across various platforms.

## Why Use BentoML?
### 1. **Standardized Model Packaging**
- Supports multiple ML frameworks like TensorFlow, PyTorch, Scikit-Learn, XGBoost, and more.
- Ensures models are packaged in a format that is easy to deploy and share.

### 2. **Efficient Model Serving**
- Provides high-performance API servers for serving ML models as REST or gRPC endpoints.
- Optimized for speed and scalability in production environments.

### 3. **Framework Agnostic**
- Enables seamless integration with various machine learning libraries.

### 4. **Versioning & Reproducibility**
- Tracks model versions, dependencies, and configurations to ensure reproducibility.

### 5. **Cloud & Container Integration**
- Supports deployment on cloud platforms like AWS Lambda, Google Cloud Run, and Azure.
- Compatible with containerization tools such as Docker and Kubernetes.

### 6. **Ease of Use**
- Simple Python APIs for packaging, deploying, and serving models without complex DevOps knowledge.

## Installation
```sh
pip install bentoml
```

## Getting Started
### **Save a Model**
```python
import bentoml
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
bentoml.sklearn.save_model("rf_model", model)
```

### **Serve the Model**
```sh
bentoml serve rf_model:latest
```

## When to Use BentoML?
- When you need to **deploy ML models quickly** with minimal setup.
- When you want to **serve models with a scalable API**.
- When you require **cloud and container support** for deployment.
- When you need to **version and track different models** for A/B testing.



## Steps involve
- Define a model
- Save a model
- Create a service
- Build a Bento
- Deploy a Bento


## What Learned
- it also has versoning capability
- can be seen via  -> bentoml models list



## To run the bentoml file 
- bentoml serve service.py:svc -- reload
- the upper ( add the service_file_name : model_using  -- reload (just in case if any change to model occur it will again get reloaded ))

- It will create swagger api created 
- for example if added [
  [1,2.3,4.2,1.0]
]

- it will give the response as [1]  # means choose the first category flower
