FROM python:3.9.10
ENV PIP_DISABLE_ROOT_WARNING=1
RUN python -m pip install --upgrade pip
COPY requirements.ci.txt requirements.ci.txt
RUN pip install -r requirements.ci.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
VOLUME /app
WORKDIR /app
ENV NO_COLOR=yes_please
ENV LANG=C
CMD ["python", "-m", "pytest"]