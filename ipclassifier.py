'''
Created on May 8, 2016
 
Checks what IP belongs to which subnet
'''
import socket,struct
 
def addressInNetwork3(ip,net):
    '''This function allows you to check if on IP belogs to a Network'''
    ipaddr = struct.unpack('=L',socket.inet_aton(ip))[0]
    netaddr,bits = net.split('/')
    netmask = struct.unpack('=L',socket.inet_aton(calcDottedNetmask(int(bits))))[0]
    network = struct.unpack('=L',socket.inet_aton(netaddr))[0] & netmask
    return (ipaddr & netmask) == (network & netmask)
 
def calcDottedNetmask(mask):
    bits = 0
    for i in xrange(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))
 
 
if __name__ == '__main__':
    address = str(raw_input("Enter IP:"))
     
    networka = "10.0.0.0/8"
    networkb = "172.16.0.0/12"
    networkc = "192.168.0.0/16"
     
    if addressInNetwork3(address,networka):
        print "IP: "+ address + " is in "+ networka
    elif addressInNetwork3(address,networkb):
        print "IP: "+ address + " is in "+ networkb
    elif addressInNetwork3(address, "192.168.0.0/16"):
        print "IP: "+ address + " is in "+ networkc
    else:
        print "Non-private IP"
