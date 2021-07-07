from mitmproxy import ctx
from typing import Sequence

class BlockTraffic:
    def __init__(self):
        self.num = 0
        self.allowed_hosts = None

    def load(self, l):
        l.add_option(
            "allowed_hosts", Sequence[str], [], "Comma-separated list of allowed hosts",
        )        

    def running(self):
        if self.allowed_hosts is None:
            self.allowed_hosts = set(list(ctx.options.allowed_hosts) + ['mitm.it'])
            hosts_pretty = "\n".join(map(lambda host: f"\t{host}", self.allowed_hosts))
            ctx.log.info(f'BlockTraffic configured to allow hosts:\n{hosts_pretty}')
            if len(ctx.options.allowed_hosts) == 0:
                ctx.log.info("Set multiple allowed hosts with: --set allowed_hosts=www.someplace.com --set allowed_hosts=*.example.com")

    def request(self, flow):
        if flow.request.host in self.allowed_hosts or '*.'+('.'.join(flow.request.host.split('.')[1:])) in self.allowed_hosts:
            ctx.log.info(f"Allowing traffic for flow: {flow.request}")    
            return

        ctx.log.info(f"Block traffic for flow: {flow.request}")
        flow.kill()

addons = [
    BlockTraffic()
]
 