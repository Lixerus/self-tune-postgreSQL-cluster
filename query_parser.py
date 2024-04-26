class QueryParser():
    def __init__(self, stat_manager):
        self.stat_manager = stat_manager

    def parse(self, path : str):
        with open(path, 'r') as f:
            #print("Started parsing")
            for line in f:
                if line.find("UPDATE") != -1 or line.find("INSERT") != -1:
                    self.stat_manager.add_update()
                elif line.find("SELECT") != -1:
                    self.stat_manager.add_select()

async def test():
    import stat_manager
    sm = stat_manager.Stat_Manager()
    qp = QueryParser(sm)
    print(await sm.asses_dbrw())
    qp.parse(path = 'C:\Program Files\PostgreSQL\\14\data\logs\postgresql-2024-04-25_182000.log')
    print(await sm.asses_dbrw())

# if __name__ == "__main__":
#     asyncio.run(test())