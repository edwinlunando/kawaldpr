from pipeline.storage import GZIPMixin, PipelineStorage


class GZIPCachedStorage(GZIPMixin, PipelineStorage):
    pass
