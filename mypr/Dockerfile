FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt 
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .


# ENTRYPOINT ["entrypoint.sh"]
# CMD [ "python", "manage.py", "makemigrations", "--no-input"]
CMD ["bash", "./entrypoint.sh"]