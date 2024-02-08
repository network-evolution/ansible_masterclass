from ansible.module_utils.basic import AnsibleModule
import csv

def main():
    module = AnsibleModule(
        argument_spec = dict(
        device_facts = dict(type='dict', required=True),
        dest_csv_path = dict(type='str', required=False, default = '/home/dev/ansible_masterclass/21_custom_module' ),
        dest_csv_file = dict(type='str', required=False, default='facts_file.csv')
        )
    )

    try:
        device_facts = module.params['device_facts']
        sorted_device_facts = dict(sorted(device_facts.items()))
        csv_filename = f"{module.params['dest_csv_path']}/{module.params['dest_csv_file']}"

        csv_header = ["inventory_name","device_ip", "hostname", "model", "version", "serial_number"]

        with open(csv_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_header)
            writer.writeheader()
            for device, details in sorted_device_facts.items():
                writer.writerow({
                    "inventory_name": device,
                    "device_ip": details['ansible_host'],
                    "hostname": details['ansible_facts']['net_hostname'],
                    "model": details['ansible_facts']['net_model'],
                    "version": details['ansible_facts']['net_version'],
                    "serial_number": details['ansible_facts']['net_serialnum'],
                })

        module.exit_json(changed=True, output="Saved content to CSV")
    except Exception as e:
        module.fail_json(msg="Module Failed", exception= str(e))
if __name__ == '__main__':
    main()