
"""

大概流程：
三个线程，随机选择两个项目，每个项目随机生成三个模板配置

"""

# -*- coding:utf-8 -*-

import requests
import logging
import json
import time
import threading
import random
import PyMySQL

TOKEN = 'SECRET'
HEADERS = {
    'X-Auth-Token': TOKEN,
    'Content-Type': 'application/json'
}

HOST = '10.246.46.60:9090'


def get(url, project):
    headers = HEADERS.copy()
    headers['X-Auth-Project'] = project
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()
    except (requests.RequestException, ValueError):
        logging.exception("Url: '%s', Prj: '%s'", url, project)


def post(url, project, payload):
    headers = HEADERS.copy()
    headers['X-Auth-Project'] = project
    try:
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()
    except (requests.RequestException, ValueError):
        logging.exception("Url: '%s', Prj: '%s'", url, project)


def get_all_project():
    projects=["bobo", "qa", "dh2", "ocean", "cc", "g18", "g17", "whhh17", "opsys", "dev", "g37", "gdc", "cbg", "zhh", "g75", "mhxy", "g78", "uu", "a1", "xy3", "g83", "buzz", "g4", "cld", "g29", "g5", "h42", "a4", "g20", "g58kr", "elk", "g58jp", "pp", "g100", "h45","sapractice", "ngsocial", "g66", "galaxy", "push"]
    rand_projec=random.sample(projects,2)
    return rand_projec


def is_finished(stat_id, prj):
    url = 'http://%s/api/v1/configgens/stat_info/%s' % (HOST, stat_id)
    result = get(url, prj)
    if result:
        return result.get('stat_info', {}).get('finish', False)

def id_get(project):
    db = mysql.connect(user="galaxy2", passwd="galaxy2", db="galaxy2", host="10.246.46.60", port=19855, charset='utf8')
    db.autocommit(True)
    cur = db.cursor()
    sql='select aa.id,bb.projectCode from configtpl aa LEFT JOIN project bb on bb.id=aa.pid where projectCode=%s'
    cur.execute(sql,(project,))
    arr=[]
    for i in cur.fetchall():
        arr.append(i[0])
    db.close()
    if len(arr) <=3:
        return arr
    else:
        rand_id=random.sample(arr,3)
        return rand_id


def generate_all(prj):
    url = 'http://%s/api/v1/configgens/generate' % HOST
    id=id_get(prj)
    payload = {
        "type": "configtpl", "configtpl_ids": id
    }
    print id,payload
    result = post(url, prj, payload)
    if result:
        return result.get('detail', {}).get('stat_id')


def main():
    while True:
        time.sleep(100)
        projects = get_all_project()
        for p in projects:
            stat_id = generate_all(p)
            print stat_id
            if not stat_id:
                logging.error("'generate_all(%s)' failed", p)
                continue
            start_time = time.time()

            stat_error = 0
            while True:
                time.sleep(5)
                finished = is_finished(stat_id, p)
                if finished:
                    logging.info("generated: %s", p)
                    break
                if finished is None:
                    stat_error += 1
                    if stat_error > 1:
                        logging.error("get_stat(%s) failed", p)
                        break
                    else:
                        continue
                if time.time() - start_time > 400:
                    logging.error("generate timeout: %s", p)
                    break


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')
    logging.getLogger('requests').setLevel(logging.ERROR)
    t_objs=[]
    for i in range (3):
        t=threading.Thread(target=main,args=())
        t.setDaemon(True)
        t.start()
        t_objs.append(t)
    for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
        t.join()