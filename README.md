# nnlm-api

This a simple API to rerank search results using monoBERT.

### Install

`conda create -n  nnlm-api python=3.7`

`conda activate nnlm-api`


`pip install -r requirements.txt`

### Run

`uvicorn app.main:app --reload --port=8080`

### Test

`pytest`