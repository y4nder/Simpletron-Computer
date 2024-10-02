from ProcessorFiles.Processor import Processor

class ProcessorFactory(object):
    def Processor_DEFAULT() -> Processor:
        return Processor()