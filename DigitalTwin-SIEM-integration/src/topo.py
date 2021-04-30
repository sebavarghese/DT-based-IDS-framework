"""
FP topology
"""

from mininet.topo import Topo

from utils import PLC1_MAC, PLC2_MAC, PLC3_MAC, HMI_MAC, ATTCKR_MAC
from utils import PLC1_ADDR, PLC2_ADDR, PLC3_ADDR, HMI_ADDR, ATTCKR_ADDR, NETMASK


class FPTopo(Topo):

    """Filling plant (FP): 3 plcs + hmi + attacker"""

    def build(self):

        switch = self.addSwitch('s1')

        plc1 = self.addHost(
            'plc1',
            ip=PLC1_ADDR + NETMASK,
            mac=PLC1_MAC)
        self.addLink(plc1, switch)

        plc2 = self.addHost(
            'plc2',
            ip=PLC2_ADDR + NETMASK,
            mac=PLC2_MAC)
        self.addLink(plc2, switch)

        plc3 = self.addHost(
            'plc3',
            ip=PLC3_ADDR + NETMASK,
            mac=PLC3_MAC)
        self.addLink(plc3, switch)

        hmi = self.addHost(
            'hmi',
            ip=HMI_ADDR + NETMASK,
            mac=HMI_MAC)
        self.addLink(hmi, switch)

        attacker = self.addHost(
            'attacker',
            ip=ATTCKR_ADDR + NETMASK,
            mac=ATTCKR_MAC)
        self.addLink(attacker, switch)
