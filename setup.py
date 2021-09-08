from distutils.core import setup

setup(
    name="monitor-brightness-cron",
    version="0.0.4",
    packages=['monitor_brightness', 'monitor_brightness.test'],
    install_requires=[
        "sh >= 1.14.1",
    ],
    entry_points={
        "console_scripts": ["monitor-brightness-cron=monitor_brightness.monitor_brightness:set_monitor_brightness"]
    },
)
