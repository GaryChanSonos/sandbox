from mplayer import Player

from sonos.client.zone_player import SOUNDBAR
from sonos.services.common import wait_until_true
from sonos.workflow.fixture import WorkflowTestFixture
from sonos.workflow.suite import WorkflowTestSuite
MPLAYER_ARGS = (
    '-nolirc', '-vo', 'null', '-ac', 'hwac3', '-ao', 'alsa:device=hdmi')
TRACK = '/mnt/Automation/DolbyDigitalSignals/6ch_voices_id_7.ac3'
EXPECTED_STREAM_TYPE = 'Dolby Digital Surround'


class SpdifPlayback(WorkflowTestFixture):

    def setUpFixture(self):
        self.zone = self.get_testbed_device_by_model(SOUNDBAR)
        self.verifyTrueOrStop(
            self.zone.diag.is_toslink_connected(),
            'TOSLINK should be connected')
        self.mplayer = Player(args=MPLAYER_ARGS)

    def tearDownFixture(self):
        self.mplayer.stop()
        self.mplayer.quit()

    def _is_stream_type_expected(self):
        """
        Verifies TOSLINK Stream Type is expected

        :return: Is Stream Type expected?
        :rtype: :obj:`bool`
        """
        return self.zone.diag.get_toslink_stream_type() == EXPECTED_STREAM_TYPE

    def test_spdif_playback(self):
        """
        Verifies SPDIF playback by checking TOSLINK Stream Type 
        """
        self.mplayer.loadfile(TRACK)
        wait_until_true(
            lambda: self._is_stream_type_expected(),
            timeout_seconds=10,
            reason="Timed out waiting for expected stream type")

if __name__ == '__main__':
    suite = WorkflowTestSuite(SpdifPlayback.__name__)
    suite.run(SpdifPlayback())
