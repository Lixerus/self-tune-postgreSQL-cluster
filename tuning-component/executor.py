class Executor():
    def __init__(self, conn):
        self.conn = conn

    async def execute(self, knobs:dict):
        async with self.conn as conn:
            async with conn.cursor() as cur:
                for key, value in knobs.items():
                    #print(f"Executing ALTER SYSTEM SET {key} TO {value};")
                    await cur.execute(f"ALTER SYSTEM SET {key} TO {value};")