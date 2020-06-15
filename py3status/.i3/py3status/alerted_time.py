from datetime import datetime
class Py3status:
    format = '{hour}:{minute}:{second}'
    alert_hour_min = 0
    alert_hour_max = alert_hour_min + 6
    alert_color = "#FF0000"
    normal_color = "#FFFFFF"

    def alerted_time(self):
        self.alert_hour_min = self._valid_hour(self.alert_hour_min)
        self.alert_hour_max = self._valid_hour(self.alert_hour_max)
        hour = str(datetime.now().time().hour)
        if len(hour) < 2:
            hour = "0" + str(hour)
        minute = str(datetime.now().time().minute)
        if len(minute) < 2:
            minute = "0" + str(minute)
        second = str(datetime.now().time().second)
        if len(second) < 2:
            second = "0" + str(second)
        data = {
            'hour':hour,
            'minute':minute,
            'second':second
        }
        full_text = self.py3.safe_format(self.format,data)
        color = self.normal_color
        if self._check_alerthour(hour) :
            color = self.alert_color

        return {
            'full_text': full_text,
            'color': color,
            'cached_until': 1
        }
    def _check_alerthour(self,hour):
        if self.alert_hour_max < self.alert_hour_min:
            if self.alert_hour_min <= int(hour) and int(hour) <= self.alert_hour_max + 24:
                return True
        else:
            if self.alert_hour_min <= int(hour) and int(hour) <= self.alert_hour_max:
                return True
        return False
    def _valid_hour(self,hour):
        while not hour >= 0 or not hour < 23:
            if hour > 23:
                hour += -24
            if hour < 0:
                hour += 24
        return hour
