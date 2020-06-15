author__ = 'Gary.Chan'
from datetime import date
from icalendar import Calendar
from sonos.client.zone_player import S1
from sonos.workflow.fixture import WorkflowTestFixture
from sonos.workflow.suite import WorkflowTestSuite
from time import sleep

import fish
import logging
import requests


class smart_alarm(WorkflowTestFixture):

    def setUpFixture(self):
        self.ical_url = raw_input('Enter your iCal URL: ')
        self.zone = self.get_testbed_device_by_model(S1)

    def _set_alarm_state(self, expected_state):
        initial_state = self._get_alarm_state()
        if initial_state != expected_state:
            # print('Setting alarm state to <{}>'.format(expected_state))
            self.zone.AlarmClock.update_specified_alarm(
                alarm_id=4, enabled=expected_state)
            self._get_alarm_state()

    def _get_alarm_state(self):
        alarm = self.zone.AlarmClock.get_alarm(4)
        state = bool(int(alarm.get('Enabled')))
        # print('Alarm state = <{}>'.format(state))
        return state

    def test_smart_alarm(self):
        bird = fish.Bird()
        while True:
            today = date.today()
            todays_event = {today:None}
            req = requests.get(self.ical_url)
            cal = Calendar.from_ical(req.text)
            for event in cal.walk('vevent'):
                start = event.get('dtstart')
                event_date = start.dt
                event_name = event.get('summary')
                if today == event_date:
                    # print('Today is a holiday, {}'.format(event_name))
                    todays_event[today] = event_name
            if todays_event[today]:
                self._set_alarm_state(False)
            else:
                # print('Today is not a holiday')
                self._set_alarm_state(True)
            bird.animate()
            sleep(3)

if __name__ == '__main__':
    suite = WorkflowTestSuite(smart_alarm.__name__, log_level=logging.CRITICAL)
    suite.run(smart_alarm())
