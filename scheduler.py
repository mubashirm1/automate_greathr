from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
import import_ipynb
from main import main
# Create scheduler
ist = pytz.timezone('Asia/Kolkata')
scheduler = BlockingScheduler(timezone=ist)

# Run at 9:30 AM and 7:00 PM, Monday to Friday
scheduler.add_job(main, CronTrigger(day_of_week='mon-fri', hour='9,19', minute='30,0',timezone=ist))
scheduler.start()
