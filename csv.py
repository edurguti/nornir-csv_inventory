#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get,napalm_cli
from nornir.plugins.functions.text import print_result

def get_device_state(task):
    r = task.run( napalm_get, getters = [ "get_facts" ] )


nr = InitNornir(config_file="config.yaml")

print("Processing {} host(s)".format(len(nr.inventory.hosts)))

print(nr.inventory.hosts)

result = nr.run( task = get_device_state)
for host, host_data in sorted(result.items()):
    print("Host: ", host)
    for cmd in host_data[0].result:
        print("Command: ", cmd)

        print_result(result)
