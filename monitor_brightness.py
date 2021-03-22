#!/usr/bin/env python
import datetime
import sh

# borrowed from https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio
def remap(x, old_min, old_max, new_min, new_max):
    portion = (x - old_min) * (new_max - new_min) / (old_max - old_min)

    result = new_max - portion

    if x > 0 and x < 7:  # quick hack for 0 brightness between 0 and 7am
        return 0

    return min(max(int(result), 0), 50)

old_max = 20  # 8pm
old_min = 17  # 5pm
new_max = 50  # normal brightness
new_min = 0   # minimum brightness

now = datetime.datetime.now()
hour = now.hour
minute = (now.minute/60)
hour_minute = hour + minute  # hour with decimals for a smoother transition

# return a decreasing monitor brightess value between 5pm and 8pm
new_value = remap(x=hour_minute, old_min=old_min, old_max=old_max, new_min=new_min, new_max=new_max)
print(f"The hour is {hour_minute:.2f}, brightness value is {new_value}.")
sh.sudo.ddcutil(f"setvcp", "10", new_value)  # set the monitor brightness using `ddcutil`
