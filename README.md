# pi-reboot
Single GPIO button shutdown/reboot script for Raspberry Pi.

## Setup
- Clone repository
- Add cron job with `crontab -e`: `@reboot cd <script location> & python reboot.py`
