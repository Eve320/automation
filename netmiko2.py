from netmiko import ConnectHandler

iosv_l2_S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'eve',
    'password': 'cisco'
}

iosv_l2_S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'eve',
    'password': 'cisco'
}


iosv_l2_S3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'eve',
    'password': 'cisco'
}

all_devices = [iosv_l2_S1, iosv_l2_S2, iosv_l2_S3]


for devices in all_devices:
    net_connect = ConnectHandler(**devices)

    for n in range (20,31):
        print ("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output) 