import time

import requests
import yaml

config = yaml.safe_load(open("src/config.yml"))


async def get_alltasks(user):
    r = await make_request(config['URL'] + 'group/' + str(user.gid) + '/variant/' + str(user.vid) + '/task/list')
    return r.json()


async def get_task(user, taskid):
    r = await make_request(config['URL'] + 'group/' + str(user.gid) + '/variant/' + str(user.vid) + '/task/' + str(taskid))
    return r.json()


# Core method
# TODO: Количество попыток обращения и задержка между обращениями должны быть в конфиге
async def make_request(url):
    for i in range(0, 2):
        result = requests.get(url)
        if result.status_code == 200:
            return result
        time.sleep(2)
        raise Exception("Can't access DTA")