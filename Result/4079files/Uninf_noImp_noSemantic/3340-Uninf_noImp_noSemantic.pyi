from typing import Any

def send_email(alert_readings: Any, address: Any) -> None: ...
def reset_email_sent_flag_if_alerts_clear(alert_results: Any, email_sent: Any): ...
def check_sensor_alert_limits(alert_results: Any, alert_flag: Any): ...
