import redis

client = redis.Redis(host="localhost", port=6379, db=0, password="password")
pipeline = client.pipeline(transaction=False)

pipeline.sadd("mylist", "element 1")
pipeline.sadd("mylist", "element 2")
pipeline.sadd("mylist", "element 3")
pipeline.sadd("mylist", "element 4")

print(pipeline.smembers("mylist"))
print(pipeline.execute())


with client.pipeline() as mypipe:
    print(mypipe.scard("mylist"))








