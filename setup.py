from distutils.core import setup

setup(
    name="monitor-brightness-cron",
    version="0.0.1",
    install_requires=[
        "sh >= 1.14.1",
    ],
    scripts=["monitor_brightness.py"]
)
