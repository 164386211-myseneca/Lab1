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



s



s
s

s
s

s
s
s
s











### Basic Connectivity and Linux VMs Firewall Setting






s
s
s
s
s
s
s
s
s

s
s
s
s
s
s

























### Azure Cost Analysis Charts
