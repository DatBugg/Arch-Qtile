# Arch-Linux

Guide to install and configurate Arch-Linux with Qtile (BIOS)

## Things you need to start install

- Arch ISO from [resource](https://archlinux.org/)
- Rufus to create bootable USB [resource](https://rufus.ie/es/)
- To start the installation it is easier to have a LAN connection available
- PenDrive

Keep in mind that the tutorial is to install Arch-Linux in an environment that only uses this OS

# Creating Bootable USB

- With Rufus burn the ISO image on the pendrive with the default options

# Installing

## First

 1. Connect the pendrive to the pc and turn it on by entering the boot menu, depending on the mother is the button (F1, F8, F9, F10, TAB or ESC).
 2. Select the pendrive as the boot drive.

# Let`s Do It

> I will write the commands with the explanation of each one

```bash
loadkeys = en
```

## Preparing the system
 Change Keyboard layout ("en", "es", or whatever you use)
 ```bash
loadkeys es
```
Check if network is enabled
 ```bash
iplink
```
Check conection
 ```bash
ping google.com  
```
 >It should return the response from the server, Ctrl + C to stop
 
In the case of a Wi-Fi connection follow this
 ```bash
iwctl
device list
station device scan
station device get-networks
station device connect SSID (name of your wifi)
iwctl --passphrase _passphrase_ station _device_ connect _SSID_
```

Ensure your system clock is accurate
 ```bash
timedatectl set-ntp true
```

 
 ## Partition & format the disks

 ```bash
fdisk -l
```
Returns the list of available disks, nos interesa el /dev
 ```bash
fdisk/dev/sda*
```
>  Where is the * put the disk number to partition, In this guide we will use the whole disk
 ```bash
o
```
>  Create partition table

Now we will create the partitions, I will directly leave the list of commands to do 3, "root, home and swap"
 ```bash
n
p
1
"enter"
+400G
n
e
2
"enter"
"enter"
n
"enter"
+50G
n
"enter"
"enter"
t
6
82
a
1
w
```
 ```bash
mkswap /dev/sda6
swapon
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda5
```

## Mount the file System
I use sda1, put the disk that has been marked as root
 ```bash
mount /dev/sda1* /mnt
mkdir /mnt/home
mount /dev/sda5 /mnt/home
```

## Instalation & Configuration basic

We are going to install the basics, then for my configuration more things will be added
 ```bash
pacstrap /mnt base linux linux-firmware pacman networkmanager grub sudo
```
 ```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
Now we go to arch-root
 ```bash
arch-chroot /mnt
```

We set the time zone, you can use this link https://www.zeitverschiebung.net/
 ```bash
ln -sf /usr/share/zoneinfo/*/Region*/City* /etc/localtime
```
We set de time
 ```bash
hwclock --systohc
```
 ```bash
nano /etc/locale.gen
```
Find the distribution you use, in my case "es_AR-UTF-8 UTF8"
 ```bash
ctrl o
ctrl x
```
 ```bash
locale-gen
```
 ```bash
echo "LANG=es_ES.UTF-8" > /etc/locale.conf
```
 ```bash
echo "KEYMAP=es" > /etc/vconsole.conf
```
> Put the keymap you use
 ```bash
echo "pchome" > /etc/hostname
```
> Replace hostname with your nick

 ```bash
nano /etc/hosts
```
 ```bash
 /etc/hosts
127.0.0.1	localhost
::1		localhost
127.0.1.1	myhostname*.localdomain myhostname*
ctrl o
ctrl x
```
> Replace myhostname with your nick domain

 ```bash
passwd 
```
> Set root password
> 
 ```bash
systemctl enable NetworkManager
```

 ```bash
grub-install /dev/sda
```

 ```bash
grub-mkconfig -o /boot/grub/grub.cfg
```
Create users
 ```bash
useradd -m datbugg
passwd datbugg
usermod -aG wheel.video.audio.storage
```

 ```bash
nano /etc/sudoers
```
> Uncomment "%wheel ALL=(ALL) ALL
 ```bash
ctrl o
ctrl x
```

 ```bash
exit
```

 ```bash
umount -R /mnt
```

 ```bash
shutdown now
```

> Remove the USB and start the pc


# Install Qtile and dependencies:

 ```bash
sudo pacman -S xorg
```

 ```bash
sudo pacman -S qtile lightdm lightdm-gtk-greeter xterm
sudo systemctl enable lightdm
```

## First steps

 ```bash
mod + enter
```
> open terminal

 ```bash
mod + enter
```
 ```bash
setxkbmap es
```

 ```bash
sudo pacman -S alacritty code firefox
```
> Alacritty is the terminal I use and code is for VSCode
 ```bash
sudo pacman -S rofi pulseaudio pavucontrol thunar
```

Clone this repository and copy my configs:

```bash
git clone https://github.com/DatBugg/Arch-Qtile.git
cp -r Arch-Qtile/qtile ~/.config
```

## Structure

In ```config.py```, which is the file where most people write all their config,

```python
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
```

If you want to change *autostart* programs, open  ```./autostart.sh```.

```bash
#!/bin/sh
# The & is to keep it running
# Example with volumeicon
volumeicon &
```

If you want to modify keybindings, open ```./settings/keys.py```
To modifyworkspaces, use ```./settings/groups.py```
Finally, if you want to add more layouts, check ```./settings/layouts.py```
The rest of files don't need any configuration.

## Themes

To create a theme, or see the available ones ```./themes```
To chose one, write the name of the theme you want in a file named ```./config.json```:

> Example
```json
{
    "theme": "dracula"
}
