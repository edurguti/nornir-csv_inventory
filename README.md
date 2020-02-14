# nornir-csv_inventory
Example CSV Inventory for Nornir

config.yaml contains an example nornir configuration which references the csv_inventory plugin, and specifies the file name to find the inventory
inventory.csv is the actual inventory in host,platform,user,password format
csv.py is an example nornir script to access said inventory and iterate through it to run a get_state command
csv_inventory/* is the sample csv_inventory plugin
