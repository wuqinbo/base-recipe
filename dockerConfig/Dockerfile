FROM wuqingbo/centos7:python3
MAINTAINER qinbo.wu

WORKDIR /var/www/base-recipe

COPY . .

RUN pip3 install --no-cache-dir -r ./requirements.txt

CMD ["sh", "./dockerConfig/start.sh"]

