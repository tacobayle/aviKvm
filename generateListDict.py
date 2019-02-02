import json, os, yaml, sys, ast
paramsFile = sys.argv[1]
with open(paramsFile, 'r') as stream:
  data_loaded = yaml.load(stream)
stream.close
list = []
d = {}
ips = []
d['name'] = 'controller'
for domain in data_loaded['kvm']['domains']:
  ips.append(domain['ip'])
d['ip'] = ips
list.append(d)
print(json.dumps(list))
