# monitor-brightness-cron
A script that sets monitor brightness based on the time of day

## Prerequisites

Relies on having `ddcutil`, Python 3 and [sh](https://amoffat.github.io/sh/) installed.

## Example Cron

```
# run every 5 minutes
*/5 * * * * <some path>/monitor-brightness-cron/monitor_brightness.py 2>&1 | logger -t monitor_brightness
```

## Raspberry Pi

Say you have a monitor that supports DisplayPort and it doesn't support DDC over it, but _does_ have a HDMI port which supports DDC. One solution is to attach a Raspberry Pi to the HDMI port permanently for the sole purpose of running this script while you continue to use DisplayPort for video.

`/boot/config.txt`:
```
[pi4]
dtoverlay=vc4-kms-v3d

[all]
dtoverlay=vc4-kms-v3d
```

(note these are _not_ set to `vc4-fkms-v3d`, the `f` is absent)

```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y git python3-venv pipx ddcutil
pipx install --spec git+https://github.com/aarongorka/monitor-brightness-cron.git monitor-brightness-cron
```

Set your timezone appropriately:

```
sudo timedatectl set-timezone 'Australia/Sydney'
```

Ensure the `i2c_dev` kernel module is loaded:

```
echo i2c_dev | sudo tee -a /etc/modules
sudo modprobe i2c_dev
```
