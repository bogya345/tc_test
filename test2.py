from datetime import datetime
import redis
import json
import datetime

def getConnection(category, connectioName, filename='./connections.json'):
    j = json.load(open(filename))
    print(j)

    t = j[category]
    
    for i in t:
        if i['name'] == connectioName:
            return i['host'], i['port'], i['db']

    print(t)
    raise Exception('There no connection like this')

    pass

def func_redis():

    host, port, db = getConnection('databases', 'redis')
    
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    key = str(datetime.datetime.now())
    r.set(key, key)

    print(r.get(key))

    return r.get(key)

if __name__ == '__main__':
    
    func_redis()

    pass