FROM python:3.10

# EXPOSE 8080

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc \
    libpq-dev \
    python3-dev

RUN apt-get clean 

COPY ticket-agency-app/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

RUN mkdir /app/utils
COPY ticket-agency-app/src/** /app/
COPY ticket-agency-app/src/utils/* /app/utils/

# ENV GOOGLE_APPLICATION_CREDENTIALS="/app/white-option-413812-b1df76077256.json"

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py"]
#,"--server.enableCORS", "false", "--browser.serverAddress", "0.0.0.0", "--browser.gatherUsageStats", "false", "--server.port", "8501"]


