
# write some code to build your image
FROM python:3.8.12


COPY requirements.txt /requirements.txt 
COPY api /api
COPY model.joblib /model.joblib
COPY TaxiFareModel /TaxiFareModel
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD uvicorn api.fast:app --host 0.0.0.0 --port 8080