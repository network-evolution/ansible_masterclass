import csv

device_facts = {
        "r2": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "r2",
            "net_image": "flash0:/vios-adventerprisek9-m",
            "net_iostype": "IOS",
            "net_model": "IOSv",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.10.12",
            "net_serialnum": "9QHFV402RD6P14SG12CFZ",
            "net_system": "ios",
            "net_version": "15.6(2)T",
            "network_resources": {}
        },
        "r1": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "vIOS_61",
            "net_image": "flash0:/vios-adventerprisek9-m",
            "net_iostype": "IOS",
            "net_model": "IOSv",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.10.12",
            "net_serialnum": "93ZRXYQB0DAH4XW6LK9KZ",
            "net_system": "ios",
            "net_version": "15.6(2)T",
            "network_resources": {}
        },
        "r3": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "CSR-17.3",
            "net_image": "bootflash:packages.conf",
            "net_iostype": "IOS-XE",
            "net_model": "CSR1000V",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.10.12",
            "net_serialnum": "90OR9CH8IZ7",
            "net_system": "ios",
            "net_version": "17.03.03",
            "network_resources": {}
        }
    }

sorted_device_facts = dict(sorted(device_facts.items()))

csv_filename = '/home/dev/ansible_masterclass/21_custom_module/new_generated_file.csv'
csv_header = ["inventory_name", "hostname", "model", "version", "serial_number"]

with open(csv_filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer.writeheader()
    for device, details in sorted_device_facts.items():
        writer.writerow({
            "inventory_name": device,
            "hostname": details['net_hostname'],
            "model": details['net_model'],
            "version": details['net_version'],
            "serial_number": details['net_serialnum'],
        })

print(__name__)