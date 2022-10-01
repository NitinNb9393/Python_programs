#!/bin/bash
#
tput clear
trap ctrl_c INT

function ctrl_c() {
        echo "**You pressed Ctrl+C...Exiting"
        exit 0;
}
#
echo -e "\n###################################################################################"
echo
echo
echo -e "\n           Welcome to audit of your linux machine by RISHIKESH MANE:           "
echo
echo
sleep 1
echo -e "\n###################### SERVER UPTIME  ##############################################"
echo
uptime | cut -d "," -f 1
echo
echo -e "\n###################### Last Server Reboot Timestamp ################################"
echo
dmesg | grep “systemd-” | head
echo
echo -e "\n###################### Server Local Time Zone [Expected IST, Highlight to NON-IST ]#"
echo
date +%Z
echo
echo -e "\n###################### server Date time and Timezone ###############################"
echo
date
echo
echo -e "\n###################### Last 10 installed packges with dates ########################"
echo
rpm -qa --last | tail -n  10
echo
echo -e "\n###################### OS version [Expected RHEL family, Highlight for different os]"
echo
cat /etc/redhat-release
echo
echo -e "\n###################### Kernel version ##############################################"
echo
hostnamectl | grep Kernel
echo
echo -e "\n###################### CPU - Virtual cores Total count #############################"
echo
nproc
echo
echo -e "\n###################### CPU - Clock speed ###########################################"
echo
cat /proc/cpuinfo | grep MHz
echo
echo -e "\n###################### CPU - Architecture ##########################################"
echo
lscpu | grep "Architecture"
echo
echo -e "\n###################### Disk - Mounted/Unmounted volumes, type, storage #############"
echo
findmnt -D
echo
echo -e "\n###################### Unmounted Volumes ###########################################"
echo
fdisk -l
echo
echo -e "\n###################### Public and Private address of system#########################"
echo
echo -e "\n                       Private IP                                                   "
ip route get 1.2.3.4 | awk '{print $7}'
echo
echo
echo -e "\n                       Public IP                                                    "
curl ifconfig.me
echo
echo
echo -e "\n###################### Hostname as I am using Aws ec2 instance of RHEl#########"
echo
hostname
echo
echo -e "\n###################### Networking - Bandwidth #################################"
echo
echo
echo -e "\n###################### OS Firewall (Allowed Ports & Protocols)#################"
echo
firewall-cmd --list-ports
echo
echo -e "\n###################### Network Firewall Allowed Ports #########################"
echo
netstat -tulpn | grep LISTEN
echo
echo -e "\n###################### Network Firewall Allowed Protocols #####################"
echo
netstat -s
echo
echo -e "\n###################### CPU - Utilization ######################################"
echo
vmstat
echo
echo -e "\n###################### RAM - Utilization ######################################"
echo
free -h
echo
free -h | awk '0+$5 >= 60 {print}'
echo
echo -e "\n###################### Storage ################################################"
echo
df
echo -e "\n                       If greater than 60 %                                    "
echo
df -P | awk '0+$5 >= 60 {print}'
echo
echo -e "\n###################### Highlight when current User Password Exipring ##########"
echo
chage -l root
echo
echo

exit 0;
