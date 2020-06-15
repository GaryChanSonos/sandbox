__author__ = 'Gary.Chan'

from sonos.services.common import wait_until_true
from sonos.workflow.fixture import WorkflowTestFixture
from sonos.workflow.suite import WorkflowTestSuite
from time import sleep
import argparse

IDLE_SPEED = '396000'
HIGH_SPEED = '996000'
GET_SPEED = 'cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'
SET_SPEED = 'echo {} > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed'
SET_SPEED_WAIT = 1
GET_SPEED_WAIT = 1
IDLE_SPEED_WAIT = 30
IDLE_SPEED_TIMEOUT = 180

class EncoreFrequencyScalingTestFixture(WorkflowTestFixture):

    def __init__(self):
        super(EncoreFrequencyScalingTestFixture, self).__init__()
        self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-i', '--iterations', type=int, help='iterations', required=True)
        args = parser.parse_args()
        self.iterations = args.iterations

    def setUpFixture(self):
        self.encores = [zp for zp in self.my_devices if zp.modelNumber == 'S6']
        gc = self.encores[0]
        self.verifyEqualOrStop(3, len(self.encores), 'Should have 3 Encores')
        for zp in self.encores:
            if zp != gc:
                zp.AVTransport.join_group(gc)
            wait_until_true(lambda: self.get_speed(zp) == IDLE_SPEED,
                            iteration_delay=IDLE_SPEED_WAIT,
                            timeout_seconds=IDLE_SPEED_TIMEOUT)
        for zp in self.encores:
            zp.cli.stop_anacapa_nicely()

    def tearDownFixture(self):
        for zp in self.encores:
            self.set_speed(zp, HIGH_SPEED)
            zp.cli.start_anacapa()
            zp.AVTransport.leave_group()

    def get_speed(self, zp):
        sleep(GET_SPEED_WAIT)
        return zp.cli.command(GET_SPEED)

    def set_speed(self, zp, expected_speed):
        sleep(SET_SPEED_WAIT)
        zp.cli.command(SET_SPEED.format(expected_speed))
        actual_speed = self.get_speed(zp)
        self.verifyEqualOrFailCase(expected_speed, actual_speed,
                                   'expected_speed should equal actual_speed')

    def alternate_speeds(self):
        for zp in self.encores:
            self.set_speed(zp, HIGH_SPEED)
            self.set_speed(zp, IDLE_SPEED)

    def test_encore_frequency_scaling(self):
        iteration = 1
        try:
            while iteration <= self.iterations:
                self.logger.info('Iteration <{}> Started'.format(iteration))
                self.alternate_speeds()
                self.logger.info('Iteration <{}> Completed'.format(iteration))
                iteration += 1
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    suite = WorkflowTestSuite('EncoreFrequencyScalingTestFixture')
    suite.run(EncoreFrequencyScalingTestFixture())
