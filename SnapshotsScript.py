import argparse
import time
import promox
from datetime import datetime
import logging

logger = logging.getLogger('Proxmox')
logger.setLevel(logging.DEBUG)
file = logging.FileHandler('../promox/snaplogfile.log')
file.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file.setFormatter(formatter)
logger.addHandler(file)


class SnapshotAutomat:

    def __init__(self, username, password, ipaddress):
        self.api = promox.PromoxApi(username, password, ipaddress)

    def get_nodes(self):
        nodes_list = []
        resp = self.api.Nodes.nodes()
        for node in resp['data']:
            nodes_list.append(node['node'])
        return nodes_list

    def get_vmid(self):
        vmid_list = []
        resp = self.api.Nodes.Qemu.qemu('proxmox')
        for vmid in resp['data']:
            vmid_list.append(vmid['vmid'])
        return vmid_list

    def snapshots_list(self, node, vmid):
        snapshots = []
        snap_counter = -1
        response = self.api.Nodes.Qemu.QemuSnapshot.snapshot(node, vmid)
        for snap in response['data']:
            snap_counter += 1
            snapshots.append(snap)
        return snapshots, {"snap_count": snap_counter}

    def snapshots_check(self, node, vmid):
        path = '/api2/json/nodes/' + node + '/qemu/' + str(vmid) + '/snapshot/'
        snapshots, snap_count = self.snapshots_list(node, vmid)
        snap_data = []
        snap_dates = []
        snap_name_to_delete = ''

        if snap_count['snap_count'] >= 7:
            logger.info("More than 7 snapshots. Deleting oldest and creating new snapshot.")
            for snap in snapshots:
                if 'snaptime' not in snap:
                    continue
                snap_data.append({'snap_name': snap['name'], 'snap_time': datetime.fromtimestamp(snap['snaptime'])})
                snap_dates.append(datetime.fromtimestamp(snap['snaptime']))
            oldest_snap = min(snap_dates)
            for snap in snap_data:
                if oldest_snap == snap['snap_time']:
                    logger.info("Snapshot to delete: " + snap['snap_name'] + ", from: " + str(oldest_snap))
                    snap_name_to_delete = snap['snap_name']

            oldest = self.api.write_request(path + '/' + snap_name_to_delete, method='delete')

            if oldest.status_code == 200:
                logger.info("Oldest snapshot deleted! Name: " + snap_name_to_delete)
            else:
                logger.error("Unable to delete oldest snapshot " + snap_name_to_delete)
                logger.error("Delete snapshot post request " + str(oldest.status_code))
            logger.info("Snapshot deleted! " + snap_name_to_delete)

            # Mimimum time between two requests, if doesn't work increase it.
            time.sleep(5)
            snapname = 'snapshot' + str(datetime.now()).replace(" ", "").replace(':', '_').replace('-',
                                                                                                   '_').replace(
                '.', '_')
            newsnap = self.api.write_request(path, method='post', name=snapname)

            if newsnap.status_code == 200:
                logger.info("New snapshot created! Name: " + snapname)
            else:
                logger.error("Unable to create new snapshot " + snapname)
                logger.error("New snapshot post request " + str(newsnap.status_code))

        elif snap_count['snap_count'] < 7:
            logger.info("Less than 7 snapshots. Creating new.")

            snapname = 'snapshot' + str(datetime.now()).replace(" ", "").replace(':', '_').replace('-',
                                                                                                   '_').replace(
                '.', '_')
            newsnap = self.api.write_request(path, method='post', name=snapname)

            if newsnap.status_code == 200:
                logger.info("New snapshot created! Name: " + snapname)
            else:
                logger.error("Unable to create snapshot!")
                logger.error("New snapshot post request " + str(newsnap.status_code))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='method name to call')
    parser.add_argument('-p', '--password', help='parameter')
    parser.add_argument('-ip', '--ipaddress', help='api key')
    args = parser.parse_args()

    username = str(args.username).strip()
    password = str(args.password).strip()
    ipaddress = str(args.ipaddress).strip()

    snaps = SnapshotAutomat(username, password, ipaddress)

    for node in snaps.get_nodes():
        for vmid in snaps.get_vmid():
            logger.info("SNAPSHOT CHECK FOR " + node + " NODE AND " + vmid + " VM")
            snaps.snapshots_check(node, vmid)
