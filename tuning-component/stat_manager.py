from collections import Counter
import tuner, asyncio
class Stat_Manager():
    def __init__(self):
        self.query_rw = Counter({"UPDATE" : 0, "SELECT" : 0})
        self.dbrw = 0.5
        self.threshold = 0.2
        self.tuner = tuner.Tuner()

    def add_update(self):
        self.query_rw["UPDATE"] += 1

    def add_select(self):
        self.query_rw["SELECT"] += 1

    async def asses_dbrw(self):
        summ = sum(self.query_rw.values())
        if summ < 1000:
            return 0
        new_dbrw = self.query_rw["SELECT"] / (1+summ)
        print(f"Assesed dbrw {self.dbrw}, new {new_dbrw}, {self.query_rw.items()}")
        if abs(new_dbrw - self.dbrw) > 0.2 :
            self.dbrw = new_dbrw
            self.tuner.tune_knobs(new_dbrw)
            return 1
        return 0
    
    async def monitor_stats(self, executor):
        state = await self.asses_dbrw()
        if state == 1:
            await executor.execute(await self.get_new_knobs())
        else:
            await asyncio.sleep(0.5)
    
    async def get_new_knobs(self):
        return self.tuner.get_knobs()