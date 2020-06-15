__author__ = 'Gary.Chan'

from sonos.services.common import wait_until_true
from sonos.workflow.fixture import WorkflowTestFixture
from sonos.workflow.suite import WorkflowTestSuite

import sonos.exception
import time

MODEL = 'BR200'
NUM_ZONES = 10
ITERATIONS = 999999999999999
UPDATE_URL = 'http://10.22.12.24/~gchan/^29.3-88070'

class UpgradeStressTestFixture(WorkflowTestFixture):

    def setUpFixture(self):
        self.zones = [
            zp for zp in self.my_devices if zp.modelNumber == MODEL]
        self.verifyEqualOrStop(
            NUM_ZONES, len(self.zones), 'Should have {} zones'.format(
                NUM_ZONES))

    def test_upgrade_stress(self):
        iteration = 1
        try:
            while iteration <= ITERATIONS:
                self.logger.info('Iteration <{}> Started'.format(iteration))
                for zone in self.zones:
                    try:
                        zone.ZoneGroupTopology.BeginSoftwareUpdate(
                            UPDATE_URL, 1)
                    except sonos.exception.CommunicationError:
                        self.logger.info(
                            'Failed to find <{}> during iteration <{}>'.format(
                                zone, iteration))
                        self.zones.remove(zone)
                    except sonos.exception.UPnPMissingService:
                        self.logger.info(
                            'Failed to find UPnP Service during iteration <{}>'
                                .format(iteration))
                        # self.zones.remove(zone)
                    except sonos.exception.TimeoutError:
                        self.logger.info(
                            'Upgrade timed out during iteration <{}>'.format(
                                iteration))
                        self.zones.remove(zone)
                time.sleep(20)
                for zone in self.zones:
                    try:
                        wait_until_true(
                                lambda: zone.reconnect_device(),
                                iteration_delay=5, timeout_seconds=300)
                    except sonos.exception.TimeoutError:
                        self.logger.info(
                            'Upgrade timed out during iteration <{}>'.format(
                                iteration))
                self.logger.info('Iteration <{}> Completed'.format(iteration))
                iteration += 1
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    suite = WorkflowTestSuite(UpgradeStressTestFixture.__name__)
    suite.run(UpgradeStressTestFixture())
