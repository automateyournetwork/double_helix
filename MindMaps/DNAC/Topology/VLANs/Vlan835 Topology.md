# Vlan835
## Nodes
### c3504.abc.inc
#### ID: 6b741b27-f7e7-4470-b6fc-d5168cc59502
#### Platform
##### Type: Cisco 3504 Wireless LAN Controller
##### Series: Cisco 3500 Series Wireless LAN Controller
##### Family: Wireless Controller
##### ID: AIR-CT3504-K9
#### Identity 
##### IP: 10.10.20.51
##### MAC: ac:4a:56:6c:7c:00
##### Software Version: 8.5.140.0
##### Role: ACCESS
##### Role Source: AUTO
##### Fabric Role: AUTO
##### Parent Node ID: None
#### Greyout: True
### leaf1.abc.inc
#### ID: aa0a5258-3e6f-422f-9c4e-9c196db115ae
#### Platform
##### Type: Cisco Catalyst 9300 Switch
##### Series: Cisco Catalyst 9300 Series Switches
##### Family: Switches and Hubs
##### ID: C9300-24U
#### Identity 
##### IP: 10.10.20.81
##### MAC: 84:8a:8d:05:76:00
##### Software Version: 17.3.3
##### Role: ACCESS
##### Role Source: AUTO
##### Parent Node ID: None
#### Greyout: 
### leaf2.abc.inc
#### ID: f0cb8464-1ce7-4afe-9c0d-a4b0cc5ee84c
#### Platform
##### Type: Cisco Catalyst 9300 Switch
##### Series: Cisco Catalyst 9300 Series Switches
##### Family: Switches and Hubs
##### ID: C9300-24U
#### Identity 
##### IP: 10.10.20.82
##### MAC: 68:ca:e4:37:8d:80
##### Software Version: 16.11.1c
##### Role: DISTRIBUTION
##### Role Source: AUTO
##### Parent Node ID: None
#### Greyout: 
### spine1.abc.inc
#### ID: f16955ae-c349-47e9-8e8f-9b62104ab604
#### Platform
##### Type: Cisco Catalyst 9300 Switch
##### Series: Cisco Catalyst 9300 Series Switches
##### Family: Switches and Hubs
##### ID: C9300-48U
#### Identity 
##### IP: 10.10.20.80
##### MAC: 70:1f:53:73:8d:00
##### Software Version: 16.11.1c
##### Role: ACCESS
##### Role Source: AUTO
##### Parent Node ID: None
#### Greyout: 
## Links
### ID: 1363363
#### Source: 6b741b27-f7e7-4470-b6fc-d5168cc59502
#### Target: f0cb8464-1ce7-4afe-9c0d-a4b0cc5ee84c
#### Status: up
#### Greyout: True
#### Start Port
##### GigabitEthernet0/0/1
###### ID: c798c1ac-8bc2-4d7f-a7fc-4cfff1b9ca0a
###### Speed: 1000000
#### End Port
##### GigabitEthernet1/0/4
###### ID: 51949286-5fdc-4b77-94ff-b589a3dd408b
###### Speed: 1000000
### ID: 1363362
#### Source: f0cb8464-1ce7-4afe-9c0d-a4b0cc5ee84c
#### Target: f16955ae-c349-47e9-8e8f-9b62104ab604
#### Status: up
#### Greyout: True
#### Start Port
##### GigabitEthernet1/0/3
###### ID: 34827744-22df-4549-8c04-3800b6f3be1a
###### Speed: 1000000
#### End Port
##### GigabitEthernet1/0/3
###### ID: 2665c38f-6c2e-4479-95ad-26f505f45b80
###### Speed: 1000000
### ID: 1363365
#### Source: aa0a5258-3e6f-422f-9c4e-9c196db115ae
#### Target: f16955ae-c349-47e9-8e8f-9b62104ab604
#### Status: up
#### Greyout: True
#### Start Port
##### GigabitEthernet1/0/2
###### ID: c04fa596-58fb-4c31-948b-29411ad5f167
###### Speed: 1000000
#### End Port
##### GigabitEthernet1/0/2
###### ID: d1b4d290-5788-4a80-a9b0-f351408ca9c0
###### Speed: 1000000