class Storage:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def storages(self):
        api_endpoint = '/api2/json/storage'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def storage(self, storage):
        api_endpoint = '/api2/json/storage/' + str(storage)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
