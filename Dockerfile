FROM python

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip install -r ./requirements.txt
RUN pytest

EXPOSE 5000

CMD ["flask", "run",  "--host=0.0.0.0"]