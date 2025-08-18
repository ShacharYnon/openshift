FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data-loader/services/ services/ 

# EXPOSE 5000

CMD ["uvicorn" ,"services.server:app" ,"--host" ,"0.0.0.0" ,"--port" ,"8000"]
