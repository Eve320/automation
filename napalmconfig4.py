import json
from os import device_encoding

from napalm import get_network_driver


devicelist = ['192.168.122.72', '192.168.122.71']

for ip_address in devicelist:
    print("Connecting to " + str(ip_address))
    driver= get_network_driver('ios')
    iosv= driver(ip_address , 'eve' , 'cisco')
    iosv.open()

    iosv.load_merge_candidate(filename='ACL1.cfg')

    diffs = iosv.compare_config()
    if len(diffs)>0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required')
        iosv.discard_config()


    iosv.load_merge_candidate(filename='ospf.cfg')

    diffs = iosv.compare_config()
    if len(diffs)>0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No OSPF changes required')
        iosv.discard_config()

    iosv.close()