from nornir.core.deserializer.inventory import Inventory
from csv_inventory.file_get_contents import file_get_contents
import os

class CsvInventory(Inventory):
    def __init__(self, **kwargs):

        if "csv_filename" not in kwargs.keys() or os.path.exists( kwargs["csv_filename"] ) == False:
            raise FileNotFoundError

        csv_inventory = self.load_csv_data( kwargs["csv_filename"] )

        hosts = csv_inventory
        groups = {}
        defaults = {}

        super().__init__(hosts=hosts, groups=groups, defaults=defaults, **kwargs)

    def load_csv_data(self, filename):
        # Read that in to a variable
        config = file_get_contents( filename )

        # Initialize empty return value
        csv_data = {}

        # Assumed file format
        # hostname,platform,user,password

        # Walk the rancid config for interesting things we care about
        for line in config:
            # Temporary working variable
            data = {}

            items = line.split(",")
            data["hostname"] = items[0]
            data["platform"] = items[1]
            data["username"] = items[2]
            data["password"] = items[3]

            csv_data[items[0]] = data

        # Do we have any devices??
        if len(items) == 0:
            raise "No Items"

        return csv_data
