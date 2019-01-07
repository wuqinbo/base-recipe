FROM zhuipiaochen/centos7:base
MAINTAINER mike,spensersheng

WORKDIR /var/www/app

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["sh", "./dockerConfig/start.sh"]

