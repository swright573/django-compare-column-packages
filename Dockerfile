# start from an official image
FROM python:3

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# expose port 8000
EXPOSE 8000

# default command to start the container
CMD ["gunicorn", "--chdir", "compare_columns", "--bind", "0.0.0.0:8000", "-c", "gunicorn.conf.py", "compare_columns.wsgi:application"]