import promox
import argparse
import json
from datetime import datetime


class BackupsCheck:

    def __init__(self, username, password, ipaddress):
        self.api = promox.PromoxApi(username, password, ipaddress)

    def discover_vms(self):
        vms_list = []
        for node in self.api.Nodes.nodes()['data']:
            for vmid in self.api.Nodes.Qemu.qemu(node['node'])['data']:
                vms_list.append({"vm": vmid['vmid']})
        output = json.dumps({'data': vms_list}, indent=4, ensure_ascii=False)
        return output

    def get_vmids(self):
        vmids_list = []
        for node in self.api.Nodes.nodes()['data']:
            for vmid in self.api.Nodes.Qemu.qemu(node['node'])['data']:
                vmids_list.append(vmid['vmid'])
        return vmids_list

    def get_backup_tasks(self, vmid):
        backup_tasks_list = []
        for task in self.api.Cluster.tasks()['data']:
            if task['type'] == 'vzdump' and task['id'] == vmid:
                backup_tasks_list.append(task)
        return backup_tasks_list

    def get_backup_time(self, option, mid, status):
        # option parameter = starttime or endtime
        output = []
        for vmid in self.get_vmids():
            if vmid == mid:
                backups_time = []
                backup_tasks = self.get_backup_tasks(vmid)
                for tasks in backup_tasks:
                    backups_time.append(tasks[option])
                latest_time = max(backups_time)

                for task in backup_tasks:
                    if latest_time == task[option]:
                        if status == 'status':
                            return task['status']
                        else:
                            output.append({"vmid": vmid, option: str(datetime.fromtimestamp(task[option]))})
        return output


class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='method name to call')
    parser.add_argument('-p', '--password', help='parameter')
    parser.add_argument('-ip', '--ipaddress', help='api key')
    parser.add_argument('-o', '--option', help='option = starttime or endtime')
    parser.add_argument('-id', '--vmid', help='virtual machine id')
    parser.add_argument('-s', '--status', help='status')
    parser.add_argument('-m', '--method', help='method name')
    args = parser.parse_args()

    username = str(args.username).strip()
    password = str(args.password).strip()
    ipaddress = str(args.ipaddress).strip()
    option = str(args.option).strip()
    vmid = str(args.vmid).strip()
    status = str(args.status).strip()
    method = str(args.method).strip()

    backups = BackupsCheck(username, password, ipaddress)

    while switch(method):
        if case('discovery'):
            print(backups.discover_vms())
            break
        if case('backup'):
            print(backups.get_backup_time(option, vmid, status))
            break
        break
