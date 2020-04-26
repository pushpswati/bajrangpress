from crontab import CronTab

cron = CronTab(user='ubuntu')
job = cron.new(command='/home/ubuntu/.virtualenvs/swatiEnv/bin/python /home/ubuntu/projects/bajrangpress/bajrangbali/corona_client/corona_client.py')

job.hour.every(5)
#job 2..
job2 = cron.new(command='/home/ubuntu/.virtualenvs/swatiEnv/bin/python /home/ubuntu/projects/bajrangpress/bajrangbali/corona_client/corona_client2.py')
job2.hour.every(5) 

job3 = cron.new(command='/home/ubuntu/.virtualenvs/swatiEnv/bin/python /home/ubuntu/projects/bajrangpress/bajrangbali/corona_client/corona_client_global.py')

job3.hour.every(5)

cron.write()
