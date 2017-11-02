#!/usr/local/bin/python3
import subprocess, logging, sys, datetime

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename="githubPush.log")
logging.info('-----------------------------------------')
logging.debug('Program starts')

# Check for untracked files
stdout = subprocess.getoutput('git status')
if 'nothing to commit' in stdout:
    logging.info("Git clean, no changes made")
    sys.exit()

# Add commit
stdout = subprocess.getoutput('git add --all')

# Add updates for current date
stdout = subprocess.getoutput(f'git commit -m "Updates for {datetime.date.today()}"')

# Push to Github
stdout = subprocess.getoutput('git push')
logging.info(stdout)
