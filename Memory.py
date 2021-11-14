from Config import Config

from subprocess import check_output
import ctypes
import win32api as wapi
import win32process as wproc
import win32con as wcon

import psutil
import pymem
import pymem.process
import pymem.memory

class Memory:
    def __init__(self):
        self.baseAddress = self.getBaseAddress()

    def getPid(self, process_name):
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                return proc.pid

    def getBaseAddress(self):
        pid = self.getPid(Config.PROCESS.value)
        if not pid:
            raise Exception("The game is not running")
            return
        process_handle = wapi.OpenProcess(wcon.PROCESS_ALL_ACCESS, False, pid)
        module_handles = wproc.EnumProcessModules(process_handle)
        module_handles_count = len(module_handles)
        module_index = 0  # 0 - the executable itself
        if module_index > module_handles_count:
            module_index = 0
        return module_handles[module_index]
    def getMountedAddress(self, address):
        return hex(self.baseAddress + address)

    def getFloat(self, hexAdress):
        address = self.getMountedAddress(hexAdress)
        process = pymem.process
        mem = pymem.memory

        DMC5 = pymem.Pymem(Config.PROCESS.value)
        DMC5_base = DMC5.process_handle

        return mem.read_float(address=int(address, 16), handle=DMC5_base)