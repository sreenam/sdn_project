from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.node import Controller
from mininet.cli import CLI

def simple_network():
    net = Mininet(controller=Controller)

    # Create a simple topology with one switch and two hosts
    topo = SingleSwitchTopo(k=2)
    net.build()

    # Add controller
    c0 = net.addController('c0')

    # Start the network
    net.start()

    # Run the Mininet CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    simple_network()


# Add the controller to Mininet
c0 = net.addController('c0', controller=Controller, protocol='tcp', port=6633)

