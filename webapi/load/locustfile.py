
from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    min_wait = 1000
    max_wait = 1000

    @task(3)
    def task1(self):
        self.client.post("/login",
                         {"username": "ellen_key", "password": "education"})

    @task(6)
    def task2(self):

        self.client.get("/")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000