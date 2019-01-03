#!/bin/bash
#
# ./KvmLocal.sh 192.168.17.151 avi avi123
#
# Parameters
KvmIp=$1
KvmUsername=$2
KvmPassword=$3
PackageList="['qemu-kvm', 'libvirt-bin', 'ubuntu-vm-builder', 'bridge-utils', 'virtinst', 'python-lxml']"
KvmNetworkTemplateFile="network.xml.j2"
KvmDomainTemplateFile="domain.xml.j2"
KvmNetworkName="net1"
KvmBridgeName="virbr1"
KvmNetworkIp="10.1.1.1"
KvmNetworkMask="255.255.255.0"
AviControllerIp="10.1.1.5"
AviBinFile="/home/avi/bin/avi/controller-17.2.14-9128.qcow2"
AviControllerCpu="6"
AviControllerMem="14336000"
AviInstanceName="avi-controller"
AviControllerIpFile="avi_meta_controller.yml.j2"
#
AviBinFileBaseName=`basename $AviBinFile`
#
echo "---
all:
  hosts:
    $KvmIp
  vars:
    ansible_user: $KvmUsername
    ansible_ssh_pass: $KvmPassword
    ansible_become_pass: $KvmPassword" > hosts
#
ansible-playbook -i hosts --extra-vars="{'PackageList': $PackageList}" AptUpdateUpgradeKVM.yml
#
ansible-playbook -i hosts --extra-vars="KvmNetworkTemplateFile=$KvmNetworkTemplateFile \
KvmNetworkName=$KvmNetworkName KvmBridgeName=$KvmBridgeName KvmNetworkIp=$KvmNetworkIp \
KvmNetworkMask=$KvmNetworkMask KvmDhcpStart=$KvmDhcpStart KvmDhcpEnd=$KvmDhcpEnd \
AviBinFile=$AviBinFile AviBinFileBaseName=$AviBinFileBaseName AviControllerCpu=$AviControllerCpu \
AviControllerMem=$AviControllerMem AviInstanceName=$AviInstanceName \
KvmDomainTemplateFile=$KvmDomainTemplateFile AviControllerIpFile=$AviControllerIpFile \
AviControllerIp=$AviControllerIp KvmUsername=$KvmUsername" ConfigureKvm.yml
#
rm -f hosts config.iso avi_meta_controller.yml
