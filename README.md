# aviKvm
Prerequisites:
- Make sure genisoimage is installed (in the ansible host)
- Make sure the Avi Qcow2 image is available as defined in the var/params.yml file
- Make sure a VM is reachable with CPU virtualization enabled
- cat /proc/cpuinfo | grep vmx | wc -l needs to be greater than 0
- define a host file with credential

The Ansible playbook will work only on the host called "kvm":
- Update, Upgrade, Install Apt packages (including KVM packages)
- Create a new KVM Network (routed) and start it
- Transfer the Avi Qcow2 image to the KVM host or download it from the cloud
- Create an iso file with network config (IP address, Mask, Gateway) and transfer it to the KVM host
- Spin up a new instance for the Avi Controller (with the cdrom for IP parameters)
- Check the Avi controller https reachability
- Change the default password
- Configure the Tenant Settings

Example:
ansible-playbook -i hostslocalKvm main.yml

Script has been tested against:
- KVM host runs Ubuntu 14.04.05 LTS
- Avi 17.2.14, 18.1.3, 18.1.5
- Ansible 2.7.0
