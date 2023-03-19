FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /var/app
WORKDIR  /var/app

EXPOSE 8000

RUN pip3 install --upgrade pip
COPY requirements.txt /var/app/requirements.txt
RUN pip3 install -r requirements.txt --default-timeout=100 future
COPY . /var/app/.
# RUN python manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]