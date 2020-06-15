import upnp.helpers
from sonos.workflow.fixture import WorkflowTestFixture
from sonos.workflow.suite import WorkflowTestSuite

class EnableDisableFirstZPTestFixture (WorkflowTestFixture):
    
    def setUpFixture(self):
        self.logger.info("EnableDisableFirstZP: setUpFixture")
        self.helpers = upnp.helpers.Helpers(logger=self.logger)
        
        self.verifyTrueOrStop( len(self.my_devices) > 0, "this test requires at least 1 zones")
        self.test_zones = [ zp for zp in self.my_devices ]
        self.test_zp = self.test_zones[0]
    
    def test_enable_disable_first_zp(self):
        enable_res = self.test_zp.diag.enable_first_zp(self.test_zones)
        self.verifyTrueOrFailCase(enable_res, 'enable_first_zp should return True')
        disable_res = self.test_zp.diag.disable_first_zp()
        self.verifyTrueOrFailCase(disable_res, 'disable_first_zp should return True')
        
if __name__ == '__main__':
    suite = WorkflowTestSuite("EnableDisableFirstZPTestFixture")
    suite.run([EnableDisableFirstZPTestFixture()])
