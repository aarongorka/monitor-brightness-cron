# monitor-brightness-cron
A script that sets monitor brightness based on the time of day

## Prerequisites

Relies on having `ddcutil`, Python 3 and [sh](https://amoffat.github.io/sh/) installed.

## Example Cron

```
# run every 5 minutes
*/5 * * * * <some path>/monitor-brightness-cron/monitor_brightness.py 2>&1 | logger -t monitor_brightness
```
