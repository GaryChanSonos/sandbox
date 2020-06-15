__author__ = 'Gary.Chan'

from sonos.client.zone_player import S18
from sonos.services.common import wait_until_true
from sonos.workflow.fixture import combinatorial
from sonos.workflow.suite import WorkflowTestSuite
from time import sleep
from voice.voice_end_to_end.voice_end_to_end_base import (
    VoiceEndToEndBase, VOICETAP_PATH_BASE)

ITERATIONS = 999999999999999
VOICETAP_PATH = VOICETAP_PATH_BASE + "basic/"
VOICETAP = 'alexa_whats_the_weather_polly.wav'
VOICETAP_FILES_LIST = [VOICETAP]


class VoiceLoopTestFixture(VoiceEndToEndBase):

    def generate_tupelo(self):
        yield (self.get_testbed_device_by_model(S18),)

    def setUpFixture(self):
        super(VoiceLoopTestFixture, self).setUpFixture()
        self.get_files_from_nas(VOICETAP_PATH, files_list=VOICETAP_FILES_LIST)

    def setUpTest(self, zp):
        super(VoiceLoopTestFixture, self).setUpTest(zp)

    @combinatorial("generate_tupelo")
    def test_voice_loop(self, zp):
        iteration = 1
        try:
            while iteration <= ITERATIONS:
                self.logger.info('Iteration <{}> Started'.format(iteration))
                url = self.get_voicetap_url(VOICETAP)
                self.voice_overlay.load_and_start_overlay(url)
                wait_until_true(
                    lambda: zp.diag.is_player_ducked(),
                    iteration_delay=1,
                    timeout_seconds=20,
                    reason="Player should be ducked while playing TTS"
                )
                wait_until_true(
                    lambda: not zp.diag.is_player_ducked(),
                    iteration_delay=1,
                    timeout_seconds=60,
                    reason='Player should NOT be ducked after playing TTS'
                )
                self.verifyTrueOrFailCase(
                    zp.is_anacapa_running(),
                    'Anacapa should be running'
                )
                self.logger.info('Iteration <{}> Completed'.format(iteration))
                sleep(3)
                iteration += 1
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    suite = WorkflowTestSuite(VoiceLoopTestFixture.__name__)
    suite.run([VoiceLoopTestFixture()])
