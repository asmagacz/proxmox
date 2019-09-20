class Nodes:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Apt = Apt(self.api_session, self.api_url)
        self.Ceph = Ceph(self.api_session, self.api_url)
        self.Certificates = Certificates(self.api_session, self.api_url)
        self.Disks = Disks(self.api_session, self.api_url)
        self.Firewall = Firewall(self.api_session, self.api_url)
        self.Hardware = Hardware(self.api_session, self.api_url)
        self.Lxc = Lxc(self.api_session, self.api_url)
        self.Network = Network(self.api_session, self.api_url)
        self.Qemu = Qemu(self.api_session, self.api_url)
        self.Replication = Replication(self.api_session, self.api_url)
        self.Scan = Scan(self.api_session, self.api_url)
        self.Services = Services(self.api_session, self.api_url)
        self.Storage = Storage(self.api_session, self.api_url)
        self.Tasks = Tasks(self.api_session, self.api_url)
        self.VzdumpExtraconfig = VzdumpExtraconfig(self.api_session, self.api_url)

    def nodes(self):
        api_endpoint = '/api2/json/nodes/'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def time(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/time'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def aplinfo(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/aplinfo'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def config(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/config'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def dns(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/dns'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def hosts(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/hosts'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def journal(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/journal'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def netstat(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/netstat'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def report(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/report'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrd(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/rrd'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrddata(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/rrddata'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def subscriptions(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/subscription'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def syslog(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/syslog'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def version(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/version'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def vncwebsocket(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/vncwebsocket'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Apt:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def apt(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/apt'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def changelog(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/apt/changelog'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def update(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/apt/update'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def versions(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/apt/versions'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Ceph:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Flags = Flags(self.api_session, self.api_url)
        self.Fs = Fs(self.api_session, self.api_url)
        self.Mds = Mds(self.api_session, self.api_url)
        self.Mgr = Mgr(self.api_session, self.api_url)
        self.Mon = Mon(self.api_session, self.api_url)
        self.Osd = Osd(self.api_session, self.api_url)
        self.Pools = Pools(self.api_session, self.api_url)

    def config(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/config'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def configdb(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/configdb'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def crush(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/crush'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def disks(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/disks'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/log'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rules(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/rules'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Flags:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def flags(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/flags'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Fs:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def flags(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/fs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Mds:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def mds(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/mds'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Mgr:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def mgr(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/mgr'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Mon:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def mon(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/mon'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Osd:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def osd(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/osd'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Pools:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def pools(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/ceph/pools'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Certificates:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def certificates(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/certificates'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def acme(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/certificates/acme'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def info(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/certificates/info'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Disks:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Zfs = Zfs(self.api_session, self.api_url)

    def disks(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def directory(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/directory'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def list(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/list'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def lvm(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/lvm'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def smart(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/smart'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Zfs:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def zfs(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/zfs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, node, name):
        api_endpoint = '/api2/json/nodes/' + node + '/disks/zfs/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Firewall:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Rules = Rules(self.api_session, self.api_url)

    def firewall(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/firewall'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/firewall/log'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def options(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/firewall/options'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Rules:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def rules(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/firewall/rules'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pos(self, node, pos):
        api_endpoint = '/api2/json/nodes/' + node + '/firewall/rules/' + str(pos)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Hardware:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Pci = Pci(self.api_session, self.api_url)

    def hardware(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/hardware'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Pci:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def pci(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/hardware/pci'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pciid(self, node, pciid):
        api_endpoint = '/api2/json/nodes/' + node + '/hardware/pci/' + str(pciid)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def mdev(self, node, pciid):
        api_endpoint = '/api2/json/nodes/' + node + '/hardware/pci/' + str(pciid) + "/mdev"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Lxc:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.LxcFirewall = LxcFirewall(self.api_session, self.api_url)
        self.LxcSnapshot = LxcSnapshot(self.api_session, self.api_url)
        self.LxcStatus = LxcStatus(self.api_session, self.api_url)

    def lxc(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def config(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/config'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def feature(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/feature'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrd(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/rrd'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrdata(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/rrdata'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def vncwebsocket(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/vncwebsocket'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class LxcFirewall:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.FirewallAliases = FirewallAliases(self.api_session, self.api_url)
        self.FirewallIpset = FirewallIpset(self.api_session, self.api_url)
        self.FirewallRules = FirewallRules(self.api_session, self.api_url)

    def firewall(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/log'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def options(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/options'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def refs(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/refs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class FirewallAliases:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def aliases(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/aliases'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, node, vmid, name):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/aliases/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class FirewallIpset:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def ipset(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/ipset'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, node, vmid, name):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/ipset/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def cidr(self, node, vmid, name, cidr):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/ipset/' + name + "/" + cidr
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class FirewallRules:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def rules(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/rules'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pos(self, node, vmid, pos):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/firewall/rules/' + str(pos)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class LxcSnapshot:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def snapshot(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/snapshot'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def config(self, node, vmid, snapname):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/snapshot/' + snapname + "/config"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class LxcStatus:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def status(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def current(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/lxc/' + str(vmid) + '/status/current'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Network:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def network(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/network'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def iface(self, node, iface):
        api_endpoint = '/api2/json/nodes/' + node + '/network/' + str(iface)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Qemu:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.Agent = Agent(self.api_session, self.api_url)
        self.Cloudinit = Cloudinit(self.api_session, self.api_url)
        self.QemuFirewall = QemuFirewall(self.api_session, self.api_url)
        self.QemuSnapshot = QemuSnapshot(self.api_session, self.api_url)
        self.QemuStatus = QemuStatus(self.api_session, self.api_url)

    def qemu(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def config(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/config'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def feature(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/feature'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def migrate(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/migrate'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pending(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/pending'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrd(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/rrd'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrddata(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/rrddata'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def vncwebsocket(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/vncwebsocket'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Agent:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def agent(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def exec_status(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/exec-status"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def file_read(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/file-read"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_fsinfo(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-fsinfo"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_host_name(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-host-name"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_memory_block_info(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-memory-block-info"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_memory_blocks(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-memory-blocks"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_osinfo(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-osinfo"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_time(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-time"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_timezone(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-timezone"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_users(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-users"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def get_vcpus(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/get-vcpus"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def info(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/info"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def network_get_interfaces(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/agent/network-get-interfaces"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Cloudinit:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def cloudinit(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/cloudinit"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def dump(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/cloudinit/dump"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QemuFirewall:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.QmFwAliases = QmFwAliases(self.api_session, self.api_url)
        self.QmFwIpset = QmFwIpset(self.api_session, self.api_url)
        self.QmFwRules = QmFwRules(self.api_session, self.api_url)

    def firewall(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall/log"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def options(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall/options"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def refs(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall/refs"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QmFwAliases:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def aliases(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall/aliases"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, node, vmid, name):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + "/firewall/aliases/" + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QmFwIpset:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def ipset(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/firewall/ipset'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def name(self, node, vmid, name):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/firewall/ipset/' + name
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def cidr(self, node, vmid, name, cidr):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/firewall/ipset/' + name + "/" + cidr
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QmFwRules:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def rules(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/firewall/rules'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def pos(self, node, vmid, pos):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/firewall/rules/' + str(pos)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QemuSnapshot:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def snapshot(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/snapshot'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def config(self, node, vmid, snapname):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/snapshot/' + snapname + "/config"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class QemuStatus:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def status(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def current(self, node, vmid):
        api_endpoint = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/status/current'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Replication:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def replication(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/replication'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node, logid):
        api_endpoint = '/api2/json/nodes/' + node + '/replication/' + str(logid) + "/log"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self, node, logid):
        api_endpoint = '/api2/json/nodes/' + node + '/replication/' + str(logid) + "/status"
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Scan:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def scan(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def cifs(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/cifs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def glusterfs(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/glusterfs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def iscsi(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/iscsi'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def lvm(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/lvm'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def lvmthin(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/lvmthin'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def nfs(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/nfs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def usb(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/usb'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def zfs(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/scan/zfs'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Services:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def services(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/services'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def state(self, node, service):
        api_endpoint = '/api2/json/nodes/' + node + '/services/' + str(service) + '/state'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Storage:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url
        self.StorageContent = StorageContent(self.api_session, self.api_url)

    def storage(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/storage'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrd(self, node, storage):
        api_endpoint = '/api2/json/nodes/' + node + '/storage/' + str(storage) + '/rrd'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def rrddata(self, node, storage):
        api_endpoint = '/api2/json/nodes/' + node + '/storage/' + str(storage) + '/rrddata'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self, node, storage):
        api_endpoint = '/api2/json/nodes/' + node + '/storage/' + str(storage) + '/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class StorageContent:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def content(self, node, storage):
        api_endpoint = '/api2/json/nodes/' + node + '/storage/' + str(storage) + '/content'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def volume(self, node, storage, volume):
        api_endpoint = '/api2/json/nodes/' + node + '/storage/' + str(storage) + '/content/' + str(volume)
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class Tasks:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def tasks(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/tasks'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def log(self, node, upid):
        api_endpoint = '/api2/json/nodes/' + node + '/tasks/' + str(upid) + '/log'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def status(self, node, upid):
        api_endpoint = '/api2/json/nodes/' + node + '/tasks/' + str(upid) + '/status'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()


class VzdumpExtraconfig:
    def __init__(self, api_session, api_url):
        self.api_session = api_session
        self.api_url = api_url

    def extraconfig(self, node):
        api_endpoint = '/api2/json/nodes/' + node + '/vzdump/extraconfig'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
