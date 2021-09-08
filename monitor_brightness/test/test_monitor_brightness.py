#!/usr/bin/env python3
import sys
import pytest
import monitor_brightness
from monitor_brightness import *


def test_brightness_values_at_night():
    brightness_value = brightness_value = get_brightness_value(
        hour_minute=21.00,
    )
    assert brightness_value == 0


def test_brightness_values_in_afternoon():
    brightness_value = brightness_value = get_brightness_value(
        hour_minute=18.00,
    )
    assert 0 < brightness_value < 25


def test_brightness_values_in_morning():
    brightness_value = brightness_value = get_brightness_value(
        hour_minute=13.00,
    )
    assert 60 < brightness_value < 100
