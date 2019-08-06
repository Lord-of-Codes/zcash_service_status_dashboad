from time import sleep

import requests

from .config import BLACKBOX_EXPORTER_URL
from .utils import send_slack_notification


try:
    blackbox_exporter_response = requests.get(
        BLACKBOX_EXPORTER_URL, timeout=5)
    send_slack_notification(message="Blackbox exporter is running just fine!")
except Exception as e:
    notif_response = send_slack_notification(
        message='Blackbox Exporter is not running and encountered the following error:')
    notif_response = send_slack_notification(
        message=str(e)
    )
