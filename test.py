import asyncio, sys
import connector
import stat_manager, query_parser, datagetter, executor

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    cncter = connector.ConnectorPG()
    await cncter.create_pool()
    conn = await cncter.get_connection()
    exec = executor.Executor(conn)
    st_man = stat_manager.Stat_Manager()
    dg = datagetter.DataGetter()
    qp = query_parser.QueryParser(stat_manager=st_man)

    while True:
        try:
            fname = 'C:\Program Files\PostgreSQL\\14\data\logs\postgresql-2024-04-25_182000.log'
            qp.parse(fname)
            await st_man.monitor_stats(exec)
        except KeyboardInterrupt:
            print("Kbibnt stopping")
            cncter.close_pool()
    
if __name__ == "__main__":
    asyncio.run(main())