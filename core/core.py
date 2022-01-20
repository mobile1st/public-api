from core.core_base import CoreBase
from controllers.axie_event import AxieEvent


class Core(CoreBase):
    """Docstring for Core."""

    def __init__(self, session, conf):
        """TODO: to be defined1.

        :session: TODO
        :conf: TODO

        """
        super(Core, self).__init__(session, conf)
        self.event = AxieEvent(session, conf)
