import os
from data_processing import DataProcess

if __name__ == "__main__":
    foreign_file = os.path.join(os.path.abspath('..'), 'data', 'fbis.en.10k')
    native_file = os.path.join(os.path.abspath('..'), 'data', 'fbis.zh.10k')

    foreign_data_process = DataProcess(foreign_file)
    native_data_process = DataProcess(native_file)

    foreign_data_process.process()
    native_data_process.process()

