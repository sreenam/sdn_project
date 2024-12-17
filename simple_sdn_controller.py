#Import ryu 
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import set_ev_cls
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import arp
from ryu.lib.packet import ipv4

class SimpleSDNController(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(SimpleSDNController, self).__init__(*args, **kwargs)
        
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, [MAIN_DISPATCHER])
    def switch_features_handler(self, ev):
        self.logger.info("Switch connected: %s", ev.datapath.id)
        
    def start(self):
        self.logger.info("Starting SDN Controller...")
        super(SimpleSDNController, self).start()

    def stop(self):
        self.logger.info("Stopping SDN Controller...")
        super(SimpleSDNController, self).stop()

# Ensure the application doesn't exit
if __name__ == '__main__':
    app_manager.run_apps([SimpleSDNController])


