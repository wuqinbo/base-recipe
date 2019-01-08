#!/bin/sh
cd /var/www/base-recipe

# create logs directory if necessary
if [ -d logs ]; then
   echo "Using Logs directory logs..."
else
   echo "Creating logs directory..."
   mkdir ./logs
   echo "Creating logs directory...DONE!"
fi

nginx
gunicorn run_app:app -c ./dockerConfig/gunicorn.conf.py --log-level=debug --log-file /var/www/base-recipe/logs/gunicorn.log
