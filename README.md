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
loadkeys = en
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
3. 

## Mount the file System
I use sda1, put the disk that has been marked as root
 ```bash
mount /dev/sda1* /mnt
```

 ```bash
swapon /dev/sda6
```
> I use sda1, put the disk that has been marked as root

## Instalation & Configuration basic

We are going to install the basics, then for my configuration more things will be added
 ```bash
pacstrap /mnt base linux linux-firmware
```
 ```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
 ```bash
arch-chroot /mnt
```
We set the time zone, you can use this link https://www.zeitverschiebung.net/
 ```bash
ln -sf /usr/share/zoneinfo*/Region*/City* /etc/localtime
```
We set de time
 ```bash
hwclock --systohc
```
 ```bash
locale-gen
```
Create the file
 ```bash
/etc/locale.conf
```
 ```bash
LANG=_en_US.UTF-8
```
Create the file 
 ```bash
/etc/vconsole.conf
```
Put the keymap you use
 ```bash
KEYMAP=_de-latin1
```
Replace hostname with your nick
 ```bash
/etc/hostname*
```
 ```bash
 /etc/hosts
127.0.0.1	localhost
::1		localhost
127.0.1.1	_myhostname*.localdomain myhostname*
```
> Replace myhostname with your nick domain

Set root password
 ```bash
mkinitcpio -P
passwd
```

## Next steps in progress





# Install Qtile and dependencies:

```
sudo pacman -S qtile pacman-contrib
yay -S nerd-fonts-ubuntu-mono
pip install psutil
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

```python
# Change interface arg, use ip address to find which one you need
 widget.Net(**base(bg='color3'), interface='wlp2s0'),
```

Once that's done, you can login. But keep in mind keybindings will not work
unless you have the same programs that I use and the same configs. You can
either change keybindings or install the software I use and my config files,
check out [this section](https://github.com/antoniosarosi/dotfiles#keybindings)
for instructions.

## Structure

In ```config.py```, which is the file where most people write all their config,
I only have an *autostart* function and some other variables like
*cursor_warp*.

```python
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
```

If you want to change *autostart* programs, open  ```./autostart.sh```.

```bash
#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
```

If you want to modify keybindings, open ```./settings/keys.py```. To modify
workspaces, use ```./settings/groups.py```. Finally, if you want to add more
layouts, check ```./settings/layouts.py```, the rest of files don't need any
configuration.

## Themes

To set a theme, check which ones are available in ```./themes```, and write
the name of the theme you want in a file named ```./config.json```:

```json
{
    "theme": "material-ocean"
}
