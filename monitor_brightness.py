#!/usr/bin/env python
import datetime
import sh

# borrowed from https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio
def get_brightness_value(
    hour_minute: float,
) -> int:
    hour_start = 10
    hour_end = 20
    brightness_min = 0
    brightness_max = 100

    if (
        hour_minute > 0 and hour_minute < 7
    ):  # quick hack for 0 brightness between 0 and 7am
        return 0

    portion = (
        (hour_minute - hour_start)
        * (brightness_max - brightness_min)
        / (hour_end - hour_start)
    )
    result = brightness_max - portion

    return min(max(int(result), brightness_min), brightness_max)


def get_hour_minute() -> float:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute / 60
    hour_minute = hour + minute  # hour with decimals for a smoother transition
    return hour_minute


if __name__ == "__main__":
    hour_minute = get_hour_minute()
    brightness_value = get_brightness_value(
        hour_minute=hour_minute,
    )
    print(f"The hour is {hour_minute:.2f}, brightness value is {brightness_value}.")

    # set the monitor brightness using `ddcutil`
    sh.sudo.ddcutil(f"setvcp", "10", new_value)
