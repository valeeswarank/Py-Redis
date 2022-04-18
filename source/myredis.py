import redis


def printconsol(obj):
    print(obj)


# Decorator to print the result
def console_print(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        for res in results:
            print(str(res, "UTF-8"))
    return wrapper


class MyRedis:
    def __init__(self):
        self.redis = redis.Redis(host="localhost", port=6379, db=0, password="password")

    def strings(self):
        self.redis.set("name", "valeeswaran")
        printconsol(self.redis.get("name"))

        address = {"city": "tdr", "zipcode": 612104, "country": "India"}
        self.redis.mset(address)
        printconsol(self.redis.mget("city", "zipcode", "country"))
        self.redis.incr("zipcode")
        printconsol(self.redis.mget("city", "zipcode", "country"))
        self.redis.incrby("zipcode", 100)
        printconsol(self.redis.mget("city", "zipcode", "country"))
        printconsol(self.redis.exists("name"))
        self.redis.expire("country", 5)
        printconsol(self.redis.getset("name", "valeeswaran"))

    def hashes(self):
        person1 = {"name": "rishi", "city": "chennai"}
        # person2 = {"name": "vaishu", "city": "tdr"}
        self.redis.hset("100", mapping=person1)
        printconsol(self.redis.hget("100", "name"))
        printconsol(self.redis.hgetall("100"))
        printconsol(self.redis.hexists("100", "name"))
        # self.redis.hmset(name="101", mapping=person2)
        # printconsol(self.redis.hgetall("101"))
        # printconsol(self.redis.hgetall("101"))

    def lists(self):
        self.redis.lpush("fruits", "apple", "banana", "cherry", "grapes", "mango")
        printconsol(self.redis.lrange("fruits", 0, -1))
        self.redis.rpush("fruits", "jackfruit")
        printconsol(self.redis.lrange("fruits", 0, -1))
        self.redis.lpop("fruits")  # remove from begining
        self.redis.rpop("fruits")  # remove from end
        printconsol(self.redis.lrange("fruits", 0, -1))
        printconsol(self.redis.lrange("fruits", 0, 4))  # retrive only 5 items
        self.redis.expire("fruits", 10)

    def sets(self):
        self.redis.sadd("tags", "python", "javascript", "oracle", "vba", "mssql")
        printconsol((self.redis.smembers("tags")))
        printconsol(self.redis.sismember("tags", "javascript"))  # check the item is exists
        self.redis.sadd("tags:python", "panda", "numpy", "django")  # adding sublist
        printconsol((self.redis.smembers("tags:python")))  # getting sublist

    def sortedsets(self):
        self.redis.zadd(name="marks", mapping={"tamil": 100, "english": 99, "maths": 100})
        printconsol(self.redis.zrange("marks", 0, -1, withscores=True))
        printconsol(self.redis.zrangebyscore("marks", 100, 100, withscores=True))

    @console_print
    def test(self):
        self.redis.set("name", "Bhuvaneswari")
        self.redis.set("city", "chennai")
        obj = list()
        obj.append(self.redis.get("name"))
        obj.append(self.redis.get("city"))
        return obj


if __name__ == "__main__":
    REDIS = MyRedis()
    REDIS.test()
