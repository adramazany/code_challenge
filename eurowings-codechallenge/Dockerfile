FROM bitnami/spark:latest

ENV PYSPARK_MAJEOR_PYTHON_VERSION=3

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]