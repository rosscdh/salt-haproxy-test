import re
import pprint
import logging
import salt.client

pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger(__name__)

server_list_pattern = re.compile('^Name\:\s(?P<name>.*)\sStatus\:\s(?P<status>.*)\sWeight\:\s(?P<weight>.*)\sbIn\:\s(?P<bIn>.*)\sbOut\:\s(?P<bOut>.*)$')  


def deploy(tgt_selector='haproxy', backend_selector='nodes', beta_backend_selector='beta_nodes', enable='webB(\d+)', disable=None):
    """
    """
    client = salt.client.LocalClient(__opts__['conf_file'])

    backends = client.cmd(tgt_selector,
                          'haproxy.list_servers',
                          [backend_selector],
                          kwarg={'objectify': True})

    if not backends:
        logger.warn('No backends could be selected: {} {}'.format(tgt_selector, backend_selector))

    for backend in sorted(backends.get('haproxy')):
        # set to drain in LB
        logger.info('Starting HAPROXY deploy on %s' % backend)

        server_line = server_list_pattern.search(backend).groupdict()
        name = server_line.get('name')

        if bool(re.search(enable, name)):
            # enable
            logger.info('Enable %s on %s' % (name, backend))
            client.cmd_async(tgt_selector,
                             'haproxy.set_state',
                             [name, backend_selector, 'ready'])

        elif disable is not None and bool(re.search(disable, name)) or disable is None:
            # disable
            logger.info('Disable %s on %s' % (name, backend))
            client.cmd_async(tgt_selector,
                             'haproxy.set_state',
                             [name, backend_selector, 'drain'])


    backends = client.cmd(tgt_selector,
                          'haproxy.list_servers',
                          [backend_selector],
                          kwarg={'objectify': True})
    backends = client.cmd(tgt_selector,
                          'haproxy.list_servers',
                          [beta_backend_selector],
                          kwarg={'objectify': True})
    pp.pprint(backends)
    return True
