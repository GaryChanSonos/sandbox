from sonos.workflow.fixture import WorkflowTestFixture, combinatorial
from sonos.workflow.suite import WorkflowTestSuite


class HtGenerators(WorkflowTestFixture):

    def setUpFixture(self):
        self.tests = []

    def tearDownFixture(self):
        for test in self.tests:
            self.logger.info(test)

    def setUpTest(self):
        self.tests.append(self._testMethodName)

    @combinatorial('generate_testbed_stereo_pairable_devices')
    def test_generate_testbed_stereo_pairable_devices(self, left, right):
        self.tests.append('{} {}'.format(left.modelNumber, right.modelNumber))

    @combinatorial('generate_testbed_ht_satellite_capable_devices')
    def test_generate_testbed_ht_satellite_capable_devices(self, left, right):
        self.tests.append('{} {}'.format(left.modelNumber, right.modelNumber))

    @combinatorial('generate_testbed_ht_master_capable_devices')
    def test_generate_testbed_ht_master_capable_devices(self, master):
        self.tests.append(master.modelNumber)

    @combinatorial('generate_testbed_ht_master_satellite_capable_devices')
    def test_generate_testbed_ht_master_satellite_capable_devices(
            self, master, left, right):
        self.tests.append('{} {} {}'.format(
            master.modelNumber, left.modelNumber, right.modelNumber))

if __name__ == '__main__':
    suite = WorkflowTestSuite(HtGenerators.__name__)
    suite.run(HtGenerators())
