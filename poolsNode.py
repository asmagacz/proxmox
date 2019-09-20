class Pools:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def pools(self):
        api_endpoint = '/api2/json/pools'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def poolid(self, poolid):
        api_endpoint = '/api2/json/pools/' + str(poolid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
