import re
import json, argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('logfile', help='relative/absolute path to log file to be parsed')
args = parser.parse_args()

LOGFILE = args.logfile
LOGFORMAT = re.compile(r"[*] [*] [INFO]: *")
TRAFFIC_LOG = []

with open(LOGFILE) as log:
    logs = log.read().splitlines()[1:-1]
    for _log in logs:
        dt, tm, lvl, msg1, msg2, *cnt = _log.split(' ')
        log = dict(
            date = dt,
            time = tm,
            log_level = lvl,
            msg = msg1 + msg2,
            details = json.loads(' '.join(cnt)) 
        )
        TRAFFIC_LOG.append(log)

TRAFFIC_COUNT = Counter([log['details']['type'] for log in TRAFFIC_LOG])
OUTPUT = {
    'car': TRAFFIC_COUNT['car'],
    'motorcycle': int((TRAFFIC_COUNT['motorcycle'] + TRAFFIC_COUNT['bicycle']) / 2),
    'truck': TRAFFIC_COUNT['truck'],
}

print(OUTPUT, sum(OUTPUT.values()))