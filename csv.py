#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get,napalm_cli

def get_device_state(task):
    r = task.run( napalm_get, getters = [ "get_facts" ] )


nr = InitNornir(config_file="config.yaml")

print("Processing {} host(s)".format(len(nr.inventory.hosts)))

print(nr.inventory.hosts)

result = nr.run( task = get_device_state)
for host, host_data in sorted(result.items()):
    debug_log("Host: " + host)
    for cmd in host_data[1].result:
        print("Command: ", cmd)

        print_results(result)
