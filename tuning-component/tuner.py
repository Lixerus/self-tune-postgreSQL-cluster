class Tuner():
    TUNING_KNOBS = {'max_wal_size' : [512 , 2048], 'wal_writer_delay' : [100, 400], 'default_statistics_target' : [10, 1000], 'maintenance_work_mem' : [100000 , 629760],
                    'effective_cache_size' : [1,4], 'temp_buffers' : [528, 2048]}
    def __init__(self):
        self.max_wal_size = 1024
        self.wal_writer_delay = 200
        self.default_statistics_target= 100
        self.maintenance_work_mem = 300000
        self.effective_cache_size = 2
        self.temp_buffers = 1024

    def tune_knobs(self, rw):
        l,r = self.TUNING_KNOBS['max_wal_size']
        self.max_wal_size = (r-l) * (1-rw) + l
        l,r = self.TUNING_KNOBS['wal_writer_delay']
        self.wal_writer_delay = (r-l) * (1-rw) + l
        l,r = self.TUNING_KNOBS['default_statistics_target']
        self.default_statistics_target = (r-l) * rw + l
        l,r = self.TUNING_KNOBS['maintenance_work_mem']
        self.maintenance_work_mem = (r-l) * (1 - rw) + l
        l,r = self.TUNING_KNOBS['effective_cache_size']
        self.effective_cache_size = (r-l) * rw + l
        l,r = self.TUNING_KNOBS['temp_buffers']
        self.temp_buffers = (r-l) * rw + l

    def get_knobs(self):
        return {
        "max_wal_size" : self.max_wal_size,
        "wal_writer_delay" : self.wal_writer_delay,
        "default_statistics_target" : self.default_statistics_target,
        "maintenance_work_mem" : self.maintenance_work_mem,
        "effective_cache_size" : self.effective_cache_size,
        "temp_buffers" : self.temp_buffers
        }