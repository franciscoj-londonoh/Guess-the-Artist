FROM python:3.7
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt 
COPY . /app 

# Generate pikle file
WORKDIR /app/ML_model
RUN python model.py

# set work directory
WORKDIR /app

# set app port
EXPOSE 8501


ENTRYPOINT ["python3"] 

# Run app.py when the container launches
CMD [ "app.py","run","--host","0.0.0.0"] 
