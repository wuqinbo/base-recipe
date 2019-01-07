#!/bin/sh
cd /var/www/app

# create logs directory if necessary
if [ -d logs ]; then
   echo "Using Logs directory logs..."
else
   echo "Creating logs directory..."
   mkdir ./logs
   echo "Creating logs directory...DONE!"
fi

nginx
# mongod --fork --logpath=/data/log/mongodb.log
# mongoimport -d MVP -c nutrition_health_layer01  --file ./dockerConfig/data/nutrition_health_layer01.json --type json
# mongoimport -d MVP -c nutrition_health_layer01 -u 'mvpuser' -p 'Philips&Mvp@1028' --file /data/db/nutrition_health_layer01.json --type json
# mongoimport -d MVPTest -c nutrition_health_layer02 -u 'henry' -p 'Henry@Test' --file /data/db/nutrition_health_layer02.json --type json
gunicorn run_app_dev:app -c ./dockerConfig/gunicorn.conf.py --log-level=debug --log-file /var/www/app/logs/gunicorn.log
