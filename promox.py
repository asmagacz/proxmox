# !/usr/bin/python3
"""Promox API Script"""
import requests
import urllib3
import clusterNode
import accessNode
import nodesNode
import poolsNode
import storageNode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class PromoxApi:
    """Main Api Node Class"""

    def __init__(self, username, password, ipaddress):
        self.api_url = "https://" + ipaddress
        self.username = username
        self.password = password
        self.api_session = self.login()
        self.Access = accessNode.Access(self.api_session, self.api_url)
        self.Cluster = clusterNode.Cluster(self.api_session, self.api_url)
        self.Nodes = nodesNode.Nodes(self.api_session, self.api_url)
        self.Pools = poolsNode.Pools(self.api_session, self.api_url)
        self.Storage = storageNode.Storage(self.api_session, self.api_url)

    def login(self):
        api_session = requests.Session()
        api_endpoint = "/api2/extjs/access/ticket"
        querystring = {"username": self.username, "password": self.password, "realm": "pam"}

        try:
            response = api_session.post(self.api_url + api_endpoint, data=querystring, verify=False)
            token = {
                "PVEAuthCookie": response.json()['data']['ticket']
            }
            api_session.cookies.update(token)
        except Exception as ex:
            print("Error:", ex)
            exit(1)

        return api_session

    def nodes(self):
        api_endpoint = '/api2/json/nodes'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()

    def write_request(self, path, **kwargs):
        method = kwargs.get('method', None)
        name = kwargs.get('name', None)
        api_session = requests.Session()
        api_endpoint = "/api2/extjs/access/ticket"
        querystring = {"username": self.username, "password": self.password, "realm": "pam"}

        try:
            response = api_session.post(self.api_url + api_endpoint, data=querystring, verify=False)
            token = {
                "PVEAuthCookie": response.json()['data']['ticket'],
            }
            headers = {
                "CSRFPreventionToken": response.json()['data']['CSRFPreventionToken']
            }
            api_session.cookies.update(token)
            api_session.headers.update(headers)
        except Exception as ex:
            print("Error:", ex)
            exit(1)
        if method == 'delete':
            delete = api_session.delete(self.api_url + path)
            return delete
        elif method == 'post':
            delete = api_session.post(self.api_url + path, data={'snapname': name})
            return delete
        # , 'vmstate': '0'

    def version(self):
        api_endpoint = '/api2/json/version'
        data = self.api_session.get(self.api_url + api_endpoint)
        return data.json()
