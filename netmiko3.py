from netmiko import ConnectHandler

iosv_l2_S4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'eve',
    'password': 'cisco'
}

iosv_l2_S5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'eve',
    'password': 'cisco'
}


iosv_l2_S6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'eve',
    'password': 'cisco'
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()

print(lines)

all_devices = [iosv_l2_S4, iosv_l2_S5, iosv_l2_S6]


for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
