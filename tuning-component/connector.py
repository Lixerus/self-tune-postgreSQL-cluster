import aiopg
import asyncio
import sys


if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class ConnectorPG():
    def __init__(self, dbname : str ='***', user : str ='****', password : str = '****', host : str ='***'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.pool = None

    async def create_pool(self):
        if self.pool == None:
            #print(f'Awaiting dbname={self.dbname} user={self.user} password={self.password} host={self.host}')
            self.pool = await aiopg.create_pool(f'dbname={self.dbname} user={self.user} password={self.password} host={self.host}')
        
    async def get_connection(self):
        if self.pool != None:
            return self.pool.acquire()
        else:
            await self.create_pool()

    async def close_pool(self):
        if self.pool != None:
            self.pool.close()
            await self.pool.wait_closed()

async def test():
    cnctr = ConnectorPG()
    await cnctr.create_pool()
    conn = await cnctr.get_connection()
    async with conn as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"SELECT * FROM pgbench_accounts LIMIT 10;")
            ret = []
            async for row in cur:
                ret.append(row)
            print( ret )
    await cnctr.close_pool()

if __name__ == "__main__":
    asyncio.run(test())