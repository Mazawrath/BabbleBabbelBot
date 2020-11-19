FROM python:3.10.0a2-slim-buster
RUN pip install tweepy
RUN pip install sentry-sdk
RUN pip install schedule
RUN mkdir -p tweets /
RUN mkdir -p tweets/approved /
ADD listener.py /
ADD credentials.py /
ADD curate.py /
ADD translate.py /
ADD tweeter.py /
ADD utility.py /
COPY startup.sh startup.sh /
CMD ["bin/bash", "startup.sh"]
