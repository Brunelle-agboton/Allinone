# production
FROM nginx:stable-alpine as production
WORKDIR /app
RUN apk update && apk add --no-cache python3 && \    
    python3 -m ensurepip && \   
    rm -r /usr/lib/python*/ensurepip && \  
    pip3 install --upgrade pip setuptools && \   
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \   
    rm -r /root/.cache
#RUN apk update && apk add mysql mysql-client mariadb-dev gcc
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

#COPY ./nginx/default.conf /etc/nginx/nginx.conf
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
EXPOSE 5000
#ENTRYPOINT ["python3", "app.py"]
CMD ["sh", "-c", "gunicorn -w 4 app:app --bind 0.0.0.0:5000 --daemon && nginx -g 'daemon off;'"]


