from time import sleep
from thread_processing import run_concurrent_processes
from sonos.services.common import wait_until_true
from sonos.subnet import Devices

net = Devices()
devices = [x for x in net.allDevices]
dut32m = [x for x in net.allDevices if x.cli.get_arch() == 'ppc'][0]

def wait_for_content_direcories():
    wait_until_true(lambda: all([hasattr(zp, 'ContentDirectory') for zp in devices]), timeout_seconds=60, iteration_delay=1)

def clear_backtraces():
    for x in devices:
        x.cli.clear_backtrace()

def check_for_backtraces():
    for zp in devices:
        if zp.cli.has_backtrace():
            print [zp, zp.cli.command('cat /jffs/backtrace')]
            print '\n\n\n\n\n'
            raw_input('see above backtrace on {}'.format(zp))

def show_all_share_versions():
    versions = []
    for x in devices:
        versions.append(x.settings.get_share_settings_version())
    print versions

def test_anacapa_crash(share='10k'):
    check_for_backtraces()
    clear_backtraces()
    dut = dut32m
    wait_until_true(lambda: len(net.allDevices) > 0, iteration_delay=1)
    not_duts = [x for x in net.allDevices if x != dut]
    not_dut = not_duts[0]
    for zp in devices:
        zp.ContentDirectory.remove_all_shares()
    not_dut.settings.sync_share_settings(timeout_seconds=90)
    print 'indexing nas {} share on all devices'.format(share)
    not_dut.ContentDirectory.add_share('//camb-sqa-nas2/Automation/indexing_performance/{}/'.format(share), '', '', sync_timeout=90)
    print 'not_dut added {} share, waiting for share settings sync'.format(share)
    not_dut.settings.sync_share_settings(timeout_seconds=90)
    # TODO: Fix automated mode
    # if manual == False:
    #    # this index is simply replicated meta data from 1 to 65000 with .mp3 extension
    #    indexed_track_uri = 'x-file-cifs://camb-sqa-nas2/Automation/indexing_performance/{}/1.mp3'.format(share)
    #    #indexed_track_uri = dut.ContentDirectory.get_track_uri_for_filename('1.mp3')
    #    print 'indexed track uri to play {}'.format(indexed_track_uri)
    print '\n\n\n\n\n'
    raw_input('prepare to play a share track on the dut once it starts replicating')
    print '======== refreshing index on not_dut, dut will replicate ========'
    not_dut.ContentDirectory.RefreshShareIndex('Full')
    not_dut.ContentDirectory.wait_for_share_indexing_to_complete(
                                    wait_until_done=True, test_interval=0.5)
    print '======== waiting for dut to begin replication ========'
    wait_until_true(dut.ContentDirectory.is_indexing, iteration_delay=0.2)
    print '======== dut is indexing, attempt indexed track playback ========'
    print '\n\n\n\n\n'
    raw_input('======== dut is replicating, quickly attempt to start indexed playback on dut, then press return =========')
    try:
        while dut.ContentDirectory.is_indexing():
            print 'dut still indexing, play away'
            sleep(1)
    except AttributeError:
        raw_input('======== caught AttributeError, likley anacapa crashed on dut\n check for /jffs/backtrace ========')
    # TODO: Fix automated mode
    # else:
    #    dut.AVTransport.SetAVTransportURI(indexed_track_uri,'')
    #    dut.AVTransport.Play()
    print 'printing any backtraces found'
    check_for_backtraces()
    for zp in devices:
        zp.ContentDirectory.remove_all_shares()

if __name__ == '__main__':
    test_anacapa_crash()
