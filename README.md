Add below lines to `README.md` and update with your details

# Checkpoint8 Submission

- **COURSE INFORMATION: CSN400-2234**
- **STUDENT’S NAME: Dhruvkumar patel**
- **STUDENT'S NUMBER: 164386211**
- **GITHUB USER_ID: 164386211-myseneca** 
- **TEACHER’S NAME: Atoosa Nasiri** 

### Table of Contents

1. [Part A - Creating & Configuring VMs - Using Azure CLI Scripts](#Creating-&-Configuring-VMs)
2. [Part B - Basic Connectivity - Linux VMs Firewall Setting](#Basic-Connectivity-and-Linux-VMs-Firewall-Setting)
3. [Part C - Azure Cost Analysis Charts](#Azure-Cost-Analysis-Charts)

### Creating & Configuring VMs

1) 
```
Dhruv@LAPTOP-KI7OIOKF MINGW64 ~/Desktop/CSN 400 github-Azure/CSN400-Capstone-Public/CP8-Scripts/bash-scripts (main)
$ az vm list --output table
Name    ResourceGroup      Location       Zones
------  -----------------  -------------  -------
LR-73   STUDENT-RG-964269  canadacentral
LS-73   STUDENT-RG-964269  canadacentral
WC-73   STUDENT-RG-964269  canadacentral
WS-73   STUDENT-RG-964269  canadacentral



Dhruv@LAPTOP-KI7OIOKF MINGW64 ~/Desktop/CSN 400 github-Azure/CSN400-Capstone-Public/CP8-Scripts/bash-scripts (main)
$ az network nsg list --output table
Location       Name        ProvisioningState    ResourceGroup      ResourceGuid
-------------  ----------  -------------------  -----------------  ------------------------------------
canadacentral  LR-73-nsg   Succeeded            Student-RG-964269  5310ecdf-5512-4281-a46c-57587484e5de
canadacentral  LR-NSG-73   Succeeded            Student-RG-964269  ee44a43e-2bd1-4b59-85f7-116f77e3e846
canadacentral  LR73nsg156  Succeeded            Student-RG-964269  24aaef30-8574-4d6b-b87d-aa670d7c894b
canadacentral  LS-73-nsg   Succeeded            Student-RG-964269  3a7511ba-5527-4843-a783-fe45cf32f434
canadacentral  LS-NSG-73   Succeeded            Student-RG-964269  77757b13-9da2-4ffd-a654-d460a5ebe277
canadacentral  WC-73-nsg   Succeeded            Student-RG-964269  1932ce7e-9d8f-4e30-93df-93b42fbe4ab1
canadacentral  WC-NSG-73   Succeeded            Student-RG-964269  58d7712e-5eb6-434d-a269-c5bc71cbaae2
canadacentral  WS-73-nsg   Succeeded            Student-RG-964269  322a0060-bcfe-4ea2-b111-a75af501356c
canadacentral  WS-NSG-73   Succeeded            Student-RG-964269  7b848a6d-e4f6-46c3-87ca-f8fe8deb33b2



Dhruv@LAPTOP-KI7OIOKF MINGW64 ~/Desktop/CSN 400 github-Azure/CSN400-Capstone-Public/CP8-Scripts/bash-scripts (main)
$ az network nic list --output table
EnableAcceleratedNetworking    EnableIPForwarding    Location       MacAddress         Name    NicType    Primary    ProvisioningState    ResourceGroup      ResourceGuid                          VnetEncryptionSupported
-----------------------------  --------------------  -------------  -----------------  ------  ---------  ---------  -------------------  -----------------  ------------------------------------  -------------------------
False                          True                  canadacentral  00-22-48-B2-19-92  lr-73   Standard   True       Succeeded            Student-RG-964269  6491259c-becd-4e9b-9d96-fe8c4a7d422c  False
False                          False                 canadacentral  60-45-BD-62-18-4E  ls-73   Standard   True       Succeeded            Student-RG-964269  4f0b3736-eff2-40bb-a178-1d84f3b715c6  False
False                          False                 canadacentral  60-45-BD-5B-DB-19  wc-73   Standard   True       Succeeded            Student-RG-964269  a35b7dc6-5c22-4f6c-a5c0-973d619ce544  False
False                          False                 canadacentral  60-45-BD-5F-E9-FE  ws-73   Standard   True       Succeeded            Student-RG-964269  9a15cf7d-7fa2-4bd3-8868-0bbefacf8cf7  False


$ az disk list --output table
Name                                             ResourceGroup      Location       Zones    Sku              OsType    SizeGb    ProvisioningState
-----------------------------------------------  -----------------  -------------  -------  ---------------  --------  --------  -------------------
LR-73_OsDisk_1_f4386e632b9f4230ae02459cfa17b670  STUDENT-RG-964269  canadacentral           StandardSSD_LRS  Linux     64        Succeeded
LS-73_OsDisk_1_76729301d307440bbafb3a5876fa7641  STUDENT-RG-964269  canadacentral           StandardSSD_LRS  Linux     64        Succeeded
WC-73_disk1_9c84ed50ead34edf827547bdb6ca516d     STUDENT-RG-964269  canadacentral           StandardSSD_LRS  Windows   127       Succeeded
WS-73_disk1_ace3523eac894107a00ccee4b5c06217     STUDENT-RG-964269  canadacentral           StandardSSD_LRS  Windows   127       Succeeded

```

2) when we create Nic seprate from VM it gives some flexibility and independent management of networking resources and when we delete a VM , Nic is not deleted automatically and we have to delete it seperately if we want. 

3)  yes , when we create VM in the portal ,we can use existing NIC, and this capability allows us to reuse networking configuratrions which we have already setupped. and according to my point of view it is not an limitation when creating vm from portal.

4)  for LR-NSG-73
   inbound Security Rules:
AllowVnetInBound: Allows inbound traffic from any source to the Virtual Network.
AllowAzureLoadBalancerInBound: Allows inbound traffic from the Azure Load Balancer.
DenyAllInBound: Denies all other inbound traffic.
    Outbound Security Rules:
AllowVnetOutBound: Allows outbound traffic from the Virtual Network to any destination within the Virtual Network.
AllowInternetOutBound: Allows outbound traffic from any source to the Internet.
DenyAllOutBound: Denies all other outbound traffic.

5)

 ```
$ az image list --output table
HyperVGeneration    Location       Name             ProvisioningState    ResourceGroup
------------------  -------------  ---------------  -------------------  -----------------
V2                  canadacentral  lr-73-ver-0.0.1  Succeeded            STUDENT-RG-964269
V2                  canadacentral  ls-73-ver-0.0.1  Succeeded            STUDENT-RG-964269
V2                  canadacentral  wc-73-ver-0.0.1  Succeeded            STUDENT-RG-964269
V2                  canadacentral  ws-73-ver-0.0.1  Succeeded            STUDENT-RG-964269
```

6
7


### Basic Connectivity and Linux VMs Firewall Setting


1)
  
    ```
   [dpatel475@LS-73 ~]$ sudo systemctl status apache2
Unit apache2.service could not be found.
[dpatel475@LS-73 ~]$ sudo systemctl status mariadb
Unit mariadb.service could not be found.
[dpatel475@LS-73 ~]$
```


2) 
The default setting allows all incoming and outgoing traffic (ACCEPT policy) in the INPUT and OUTPUT chains. FORWARD chain has an ACCEPT policy for forwarding traffic.
the improverments we can do are: 
Change the INPUT chain policy to DROP or REJECT to deny all incoming traffic by default.
Allow only necessary services and sources in the INPUT chain using specific rules.

3) hostname of LS
```
   [dpatel475@LS-73 ~]$ hostnamectl
   Static hostname: LS-73
         Icon name: computer-vm
           Chassis: vm
        Machine ID: c30654a8e7de4cd68b942774c4e1ccca
           Boot ID: 1fcb3b56e7d548ce8caf644690a9c8d6
    Virtualization: microsoft
  Operating System: Red Hat Enterprise Linux 8.8 (Ootpa)
       CPE OS Name: cpe:/o:redhat:enterprise_linux:8::baseos
            Kernel: Linux 4.18.0-477.10.1.el8_8.x86_64
      Architecture: x86-64
```
hostname of LR 
```
[dpatel475@LR-73 ~]$ hostnamectl
   Static hostname: LR-73.CSN4002234.com
         Icon name: computer-vm
           Chassis: vm
        Machine ID: c30654a8e7de4cd68b942774c4e1ccca
           Boot ID: 85013f53541348b3bd4577212892157a
    Virtualization: microsoft
  Operating System: Red Hat Enterprise Linux 8.8 (Ootpa)
       CPE OS Name: cpe:/o:redhat:enterprise_linux:8::baseos
            Kernel: Linux 4.18.0-477.10.1.el8_8.x86_64
      Architecture: x86-64
```
4) 

### Azure Cost Analysis Charts
