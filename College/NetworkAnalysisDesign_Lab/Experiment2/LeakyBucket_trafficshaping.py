from array import array


class LeakyBucket:
    def __init__(self, no_queries, input_pkt_size, output_pkt_size):
        self.packets_stored = array("i")
        self.bucket_size = 10
        self.bucket_size_left = 10
        self.no_queries = no_queries
        self.input_pkt_size = input_pkt_size
        self.output_pkt_size = output_pkt_size

    def shape_traffic(self):
        pass
