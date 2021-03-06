import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cfe7c1f0'.decode('hex')
P2P_PORT = 17777
ADDRESS_VERSION = 140
SCRIPT_ADDRESS_VERSION = 19
RPC_PORT = 17778
RPC_CHECK = defer.inlineCallbacks(lambda helpd: defer.returnValue(
            'help' in (yield helpd.rpc_help()) and
            (yield helpd.rpc_getblockchaininfo())['chain'] != 'main'
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('help_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('help_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tHELP'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'HelpCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/HelpCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.helpcore'), 'help.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://insight.gohelpfund.com/insight/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://insight.gohelpfund.com/insight/address/'
TX_EXPLORER_URL_PREFIX = 'https://insight.gohelpfund.com/insight/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
