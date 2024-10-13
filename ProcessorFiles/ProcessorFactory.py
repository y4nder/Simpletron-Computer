from ProcessorFiles.Processor import Processor

class ProcessorFactory(object):
    def Processor_DEFAULT() -> Processor:
        """ Creates a Processor instance
        Returns:
            Processor: 
        """
        return Processor()