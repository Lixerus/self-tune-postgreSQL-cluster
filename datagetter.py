import os, re

class DataGetter():
    def __init__(self, period : float = 1, dir : str = '****', target:str = None):
        self.period = period
        self.dir = dir
        self.target = target

    async def get_file_name(self):
        if self.target == None:
            last_file_name : str = os.listdir(self.dir)[-1]
            #print(f"Got file {last_file_name}")
            self.target = re.split(r'_|-|.l', last_file_name)[-2]
            return f'{self.dir}\\postgresql-2024-04-26_{self.target}.log'
        elif os.path.isfile(f'{self.dir}\\postgresql-2024-04-26_{int(self.target)+100}.log'):
            self.target = int(self.target)+100
            #print(f"Found new postgresql-2024-04-25_{self.target}.log")
            return f'{self.dir}\\postgresql-2024-04-26_{self.target}.log'
        else:
            #print(f"Couldnt find postgresql-2024-04-25_{self.target}.log")
            return None


def test():
    dir : str = "****"
    print(type(dir))
    last_file_name : str = os.listdir(path=dir)[-1]
    print(last_file_name)
    dg = DataGetter()
    dg.get_file_name()

if __name__ == "__main__":
    test()