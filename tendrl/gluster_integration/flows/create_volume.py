from tendrl.gluster_integration.flows.flow import Flow


class CreateVolume(Flow):
    def run(self):
        super(CreateVolume, self).run()