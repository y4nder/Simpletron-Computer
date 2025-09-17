from ProcessorFiles.Processor import Processor

class ProcessorFactory(object):
    
    @staticmethod
    def Processor_DEFAULT() -> Processor:
        """ Creates a Processor instance
        Returns:
            Processor: 
        """
        return Processor()