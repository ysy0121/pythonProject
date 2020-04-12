import platform
import sys
import os
import psutil

class WindowOS:

    def __init__(self):
        super(WindowOS, self).__init__()

    def os_platform(self):
        return platform.machine()

    def os_version(self):
        return platform.version()

    def os_release(self):
        return platform.release()

    def os_uname(self):
        usage_dict = dict(platform.uname()._asdict())
        str = usage_dict['system'] + ' ' + usage_dict['release'] + ' ' + usage_dict['machine'] + ' ' + usage_dict['node']
        return str

    def os_system(self):
        return platform.system()

    def os_processor(self):
        return platform.processor()

    def os_cpucount(self):
        return psutil.cpu_count()

    def os_cputime(self):
        return psutil.cpu_times(percpu=False)

    def os_cpupercent(self):
        usage_percent = psutil.cpu_percent(interval=1, percpu=False)
        return str(usage_percent)

    def os_vmemory(self):
        usage_dict = dict(psutil.virtual_memory()._asdict())
        usage_percent = usage_dict['percent']
        return str(usage_percent)

    def os_disk(self):
        usage_dict = dict(psutil.disk_usage('C:\\')._asdict())
        usage_percent = usage_dict['percent']
        return str(usage_percent)

    def os_network(self):
        usage_obj = psutil.net_io_counters(pernic=True)
        usage_dict = dict(usage_obj['이더넷']._asdict())
        #print(usage_dict)
        usage_percent = usage_dict['packets_sent']
        usage_percent = float(usage_percent) / (1024*1024)
        usage_percent = round(usage_percent,1)
        return str(usage_percent)

    def writeAll(self):
        print(self.os_platform())
        print(self.os_version())
        print(self.os_uname())
        print(self.os_system())
        print(self.os_processor())
        print(self.os_cpucount())
        print(self.os_cputime())
        print('cpu: '+self.os_cpupercent())
        print('memory: '+self.os_vmemory())
        print('disk: '+self.os_disk())
        print('network: ' + self.os_network())

if __name__ == "__main__":
    app = WindowOS();
    app.writeAll()
