from locust import HttpUser, task


class JsonPlaceHolderPublicApi(HttpUser):
    @task
    def get_all_posts(self):
        self.client.get("https://jsonplaceholder.typicode.com/posts")
