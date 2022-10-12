# crontab-HHA-507
Assignment week 6

## Pulling down data once a day at 6 pm
#### 0 5 * * *  /usr/bin/python3 /home/jannatul_ferdous/crontab-HHA-507/File.py >/home/jannatul_ferdous/crontab-HHA-507/log.text 2>&1 &

## Pulling down data every Sunday night at 10:00pm 
#### 0 22 * * SUN /usr/bin/python3 /home/jannatul_ferdous/crontab-HHA-507/File.py >/home/jannatul_ferdous/crontab-HHA-507/log.text 2>&1 &

## Pulling down data 
### 0 0 1 */3 * /usr/bin/python3 /home/jannatul_ferdous/crontab-HHA-507/File.py >/home/jannatul_ferdous/crontab-HHA-507/log.text 2>&1 &

## Create and open a virtual machine using GCP:
1. sudo apt-get update
2. which python3
3. git clone [github repo code]
4. cd crontab-HHA-507
5. pwd
6. nano File.py [update path directory]
7. crontab -e [enter cronjob schedule and create a log.text file]
8. systemctl status cron


