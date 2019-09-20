class Cluster:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Acme = Acme(self.api_session, self.api_url)
        self.Backup = Backup(self.api_session, self.api_url)
        self.Ceph = Ceph(self.api_session, self.api_url)
        self.Config = Config(self.api_session, self.api_url)
        self.Firewall = Firewall(self.api_session, self.api_url)
        self.Ha = Ha(self.api_session, self.api_url)
        self.Replication = Replication(self.api_session, self.api_url)

    def cluster(self):
        api_endpoint = '/api2/json/cluster'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self):
        api_endpoint = '/api2/json/cluster/log'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def nextid(self):
        api_endpoint = '/api2/json/cluster/nextid'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def options(self):
        api_endpoint = '/api2/json/cluster/options'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def resources(self):
        api_endpoint = '/api2/json/cluster/resources'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self):
        api_endpoint = '/api2/json/cluster/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def tasks(self):
        api_endpoint = '/api2/json/cluster/tasks'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Acme:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Account = Account(self.api_session, self.api_url)

    def acme(self):
        api_endpoint = '/api2/json/cluster/acme'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def directories(self):
        api_endpoint = '/api2/json/cluster/acme/directories'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def tos(self):
        api_endpoint = '/api2/json/cluster/acme/tos'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Account:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def account(self):
        api_endpoint = '/api2/json/cluster/acme/account'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, name):
        api_endpoint = '/api2/json/cluster/acme/account/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Backup:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def backup(self):
        api_endpoint = '/api2/json/cluster/backup'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def backupid(self, backupid):
        api_endpoint = '/api2/json/cluster/backup/' + str(backupid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Ceph:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def ceph(self):
        api_endpoint = '/api2/json/cluster/ceph'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def metadata(self):
        api_endpoint = '/api2/json/cluster/ceph/metadata'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self):
        api_endpoint = '/api2/json/cluster/ceph/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Config:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Nodes = Nodes(self.api_session, self.api_url)

    def config(self):
        api_endpoint = '/api2/json/cluster/config'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def join(self):
        api_endpoint = '/api2/json/cluster/config/join'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def qdevice(self):
        api_endpoint = '/api2/json/cluster/config/qdevice'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def totem(self):
        api_endpoint = '/api2/json/cluster/config/totem'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Nodes:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def nodes(self):
        api_endpoint = '/api2/json/cluster/config/nodes'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def node(self, node):
        api_endpoint = '/api2/json/cluster/config/nodes/' + node
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Firewall:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Aliases = Aliases(self.api_session, self.api_url)
        self.Groups = Groups(self.api_session, self.api_url)
        self.Ipset = Ipset(self.api_session, self.api_url)
        self.Rules = Rules(self.api_session, self.api_url)

    def firewall(self):
        api_endpoint = '/api2/json/cluster/firewall'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def macros(self):
        api_endpoint = '/api2/json/cluster/firewall/macros'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def options(self):
        api_endpoint = '/api2/json/cluster/firewall/options'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def refs(self):
        api_endpoint = '/api2/json/cluster/firewall/refs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Aliases:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def aliases(self):
        api_endpoint = '/api2/json/cluster/firewall/aliases'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, name):
        api_endpoint = '/api2/json/cluster/firewall/aliases/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Groups:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def groups(self):
        api_endpoint = '/api2/json/cluster/firewall/groups'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def group(self, group):
        api_endpoint = '/api2/json/cluster/firewall/groups/' + group
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pos(self, group, pos):
        api_endpoint = '/api2/json/cluster/firewall/groups/' + group + "/" + str(pos)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Ipset:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def ipset(self):
        api_endpoint = '/api2/json/cluster/firewall/ipset'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, name):
        api_endpoint = '/api2/json/cluster/firewall/ipset/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def cidr(self, name, cidr):
        api_endpoint = '/api2/json/cluster/firewall/ipset/' + name + "/" + str(cidr)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Rules:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def rules(self):
        api_endpoint = '/api2/json/cluster/firewall/rules'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pos(self, pos):
        api_endpoint = '/api2/json/cluster/firewall/rules/' + str(pos)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Ha:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.HaGroups = HaGroups(self.api_session, self.api_url)
        self.HaResources = HaResources(self.api_session, self.api_url)
        self.Status = Status(self.api_session, self.api_url)

    def ha(self):
        api_endpoint = '/api2/json/cluster/ha'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class HaGroups:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def groups(self):
        api_endpoint = '/api2/json/cluster/ha/groups'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def group(self, group):
        api_endpoint = '/api2/json/cluster/ha/groups/' + group
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class HaResources:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def resources(self):
        api_endpoint = '/api2/json/cluster/ha/resources'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def sid(self, sid):
        api_endpoint = '/api2/json/cluster/ha/resources/' + sid
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Status:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def status(self):
        api_endpoint = '/api2/json/cluster/ha/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def current(self):
        api_endpoint = '/api2/json/cluster/ha/status/current'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def manager_status(self):
        api_endpoint = '/api2/json/cluster/ha/status/manager_status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Replication:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def replication(self):
        api_endpoint = '/api2/json/cluster/replication'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def id(self, rid):
        api_endpoint = '/api2/json/cluster/replication' + str(rid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
