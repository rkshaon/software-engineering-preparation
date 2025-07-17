# Version Check

## Most Common
```bash
cat /etc/os-release
```

Sample Output:
```bash
NAME="Ubuntu"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
ID=ubuntu
...
```

## For Ubuntu/Debian
```bash
lsb_release -a
```

Sample Output:
```bash
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.2 LTS
Release:	24.04
Codename:	noble
```

If you get `lsb_release: command not found`, you can install it using:
```bash
sudo apt install lsb-release
```

## Kernel version (not OS, but still useful)
```bash
uname -a
```

Example Output:
```bash
Linux my-host 5.15.0-91-generic #101-Ubuntu SMP ... x86_64 GNU/Linux
```

## Distro version (alternative)
```bash
hostnamectl
```

Example output:
```bash
 Static hostname: ip-172-31-41-104
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: ec26830473146038e9e9962622047ef2
         Boot ID: 85a551891c534fb38496b9219c123252
  Virtualization: xen
Operating System: Ubuntu 24.04.2 LTS              
          Kernel: Linux 6.8.0-1028-aws
    Architecture: x86-64
 Hardware Vendor: Xen
  Hardware Model: HVM domU
Firmware Version: 4.11.amazon
   Firmware Date: Thu 2006-08-24
    Firmware Age: 18y 10month 3w 2d 
```