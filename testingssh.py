from netmiko import ConnectHandler

saka_pe = {
    'device_type': 'cisco_ios',
    'ip': '10.0.111.254',
    'username': 'chidubem.nwabuisi',
    'password': 'Buisi54321@1056%', 
}

net_connect = ConnectHandler(**saka_pe)
output = net_connect.send_command('show ip int brief')
print(output)