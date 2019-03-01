import json, os, yaml, sys
#
# This python script reads an ansible ymal params file like the following:
# kvm:
#   username: avi
#   networkTemplate: network.xml.j2
#   domainTemplate: domain.xml.j2
#   networks:
#     - name: net1
#       bridgeName: virbr1
#       networkIp: 200.1.1.1
#       networkMask: 255.255.255.0
#   domains:
#     - name: avi-controller1
#       id: 1
#       uuid: 09fb234f-542e-e688-8b0d-e7aebab8c9ab
#       ip: 200.1.1.11
#       mask: 255.255.255.0
#       gw: 200.1.1.1
#     - name: avi-controller2
#       id: 2
#       uuid: 09fb234f-542e-e688-8b0d-e7aebab8c9ac
#       ip: 200.1.1.12
#       mask: 255.255.255.0
#       gw: 200.1.1.1
#     - name: avi-controller3
#       id: 3
#       uuid: 09fb234f-542e-e688-8b0d-e7aebab8c9ad
#       ip: 200.1.1.13
#       mask: 255.255.255.0
#       gw: 200.1.1.1
# to:
# avi_cluster:
#   ip:
#   - 200.1.1.12
#   - 200.1.1.13
#   name: avi-cluster
# avi_credentials:
#   api_version: 18.1.5
#   controller: 200.1.1.11
#   password: avi123
#   username: admin
#
#
paramsFile = sys.argv[1]
password = sys.argv[2]
version = sys.argv[3]
outputFile = sys.argv[4]
username = 'admin'
with open(paramsFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
try:
  controllerLeader = data_loaded['kvm']['domains'][0]['ip']
except:
  exit()
if len(data_loaded['kvm']['domains']) == 1:
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster': False}
if len(data_loaded['kvm']['domains']) == 3:
  controllerFollower = []
  controllerFollower.append(data_loaded['kvm']['domains'][1]['ip'])
  controllerFollower.append(data_loaded['kvm']['domains'][2]['ip'])
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster': {'name': 'avi-cluster', 'ip': controllerFollower }}
with open(outputFile, 'w') as outfile:
    yaml.dump(avi_credentials, outfile, default_flow_style=False)
outfile.close
