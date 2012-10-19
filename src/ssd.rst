======
 Disk
======

Disk /dev/sdb: 128.0 GB, 128035676160 bytes, 250069680 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1              63    31246424    15623181    5  Extended
/dev/sdb5             126     3903794     1951834+  83  Linux
/dev/sdb6         3903858     7807589     1951866   83  Linux
/dev/sdb7         7807653    11711384     1951866   83  Linux
/dev/sdb8        11711448    31246424     9767488+  83  Linux

 Ext4
======

[andrea@dell ~]$ sudo mkfs.ext4 /dev/sdb5
mke2fs 1.42.5 (29-Jul-2012)
Discarding device blocks: done                            
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
122160 inodes, 487958 blocks
24397 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=503316480
15 block groups
32768 blocks per group, 32768 fragments per group
8144 inodes per group
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done 

Mounted ifile system
====================

/dev/sdb5 on /home/andrea/ssd_tests/ext4 type ext4 (rw,relatime,data=ordered)
/dev/sdb6 on /home/andrea/ssd_tests/ext3 type ext3 (rw,relatime,data=ordered)
/dev/sdb7 on /home/andrea/ssd_tests/brtfs type btrfs (rw,relatime,ssd,space_cache)

Performance
===========

[andrea@dell ssd_tests]$ sudo hdparm -t /dev/sda5

/dev/sda5:
 Timing buffered disk reads: 342 MB in  3.02 seconds = 113.36 MB/sec

[andrea@dell ssd_tests]$ sudo hdparm -t /dev/sdb5 

/dev/sdb5:
 Timing buffered disk reads: 1388 MB in  3.00 seconds = 462.57 MB/sec
