---
layout: post
subtitle: Router
categories: [Network]
header:
    image: header.jpg
    align:
    text: light
---

Here is a list of commonly used CISCO device configuration commands, because too many are hard to remember, so write here for enquiries when necessary.

Enable privileged EXEC mode
```bash
Router> enable
Router#
```

Enter configuration mode
```bash
Router# conf t
Router(config)#
```

Assign a device name
```bash
Router(config)# hostname R1
```

Disable DNS lookup
```bash
Router(config)# no ip domain-lookup
```

Assign the privileged EXEC encrypted password
```bash
Router(config)# enable secret class
Router(config)#security passwords min-length 8
```

Assign cisco as the console password and enable login
```bash
Router(config)# line con 0
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# exit
Router(config)# 
```

Assign cisco as the vty password and enable login
```bash
Router(config)# line vty 0 4
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# exit
Router(config)# 
```

Encrypt the clear text passwords
```bash
Router(config)# service password-encryption
security passwords min-length 10
```

Create a banner
```bash
Router(config)# banner motd # Unauthorized access prohibited!#
***********************************************
  Warning: Unauthorized Access is Prohibited!
***********************************************
```

Configure and activate interfaces on the router
```bash
Router(config)# int g0/0
Router(config-if)# description Connection to PC-A
Router(config-if)# ip address 192.168.0.1 255.255.255.0
Router(config-if)# no shut
Router(config-if)#
Router(config)# int g0/1
Router(config-if)# description Connection to PC-B OR S1
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shut
Router(config-if)# exit
Router(config)# exit
```

Save the running configuration to the startup file
```bash
Router# copy running-config startup-config
```

Set the clock on the router
```bash
Router# clock set 00:00:00 29 March 2018
```

Erase the startup configuration file from NVRAM
```bash
Switch# show flash //if switch have been created VLANS
Switch# delete vlan.dat //删除VLANS配置文件
Router#/Switch# erase startup-config
Router#/Switch# reload
```
Set SSH of Router
```bash
(config)#:
hostname RouterName
service password-encryption
config ip address
ip domain-name name.com
username any_user password any_password

crypto key generate rsa
login block-for 180 attempts 4 within 120

(config-line)#
line vty 0 4
transport input ssh
login local

#
copy running-config startup-config

when test
ssh -l(letter,not number) any_user ip

show run to display config
```

SET IPV6
```bash
(config)# ipv6 unicast-routing
int g0/0
ipv6 address FE80::1 link-local
no shut
int G0/1
ipv6 address FE80::1 link-local
no shut

ipv6 address 2001:DB8:ACAD:A::1/64
```
