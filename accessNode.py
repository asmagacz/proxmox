class Access:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Domains = Domains(self.api_session, self.api_url)
        self.Groups = Groups(self.api_session, self.api_url)
        self.Users = Users(self.api_session, self.api_url)
        self.Roles = Roles(self.api_session, self.api_url)

    def access(self):
        api_endpoint = '/api2/json/access'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def ticket(self):
        api_endpoint = '/api2/json/access/ticket'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Domains:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def domains(self):
        api_endpoint = '/api2/json/access/domains'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def realm(self, realm):
        api_endpoint = '/api2/json/access/domains/' + realm
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Groups:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def groups(self):
        api_endpoint = '/api2/json/access/groups'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def gropuid(self, groupid):
        api_endpoint = '/api2/json/access/groups/' + str(groupid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Roles:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def roles(self):
        api_endpoint = '/api2/json/access/roles'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def roleid(self, roleid):
        api_endpoint = '/api2/json/access/roles/' + roleid
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Users:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def users(self):
        api_endpoint = '/api2/json/access/users'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def userid(self, userid):
        api_endpoint = '/api2/json/access/users/' + str(userid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def tfa(self, userid):
        api_endpoint = '/api2/json/access/users' + str(userid) + "/tfa"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
