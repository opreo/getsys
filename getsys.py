# getsys.py

import psutil
import platform
from datetime import datetime
import cpuinfo
import socket
import uuid
import re

from print_dict import * # import all from print_dict.py


# function for getting bytes in their proper formats
def get_size(bytes, suffix="b"):
    """
    scale bytes to its proper format
    e.g:
        1253656 => '1.20mb'
        1253656678 => '1.17gb'
    """
    factor = 1024
    for unit in ["", "k", "m", "g", "t", "p"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# main function for gathering system info and returning it as a dictionary
def get_system_info():
    """
    gather system information and return it as a dictionary
    """
    # general system info
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)

    # cpu information
    cpu = cpuinfo.get_cpu_info()
    cpufreq = psutil.cpu_freq()
    cpu_usage_per_core = psutil.cpu_percent(percpu=True, interval=1)
    
    # memory information
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    # disk information
    partitions_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            partitions_info.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "total_size": get_size(usage.total),
                "used": get_size(usage.used),
                "free": get_size(usage.free),
                "percent": usage.percent,
            })
        except PermissionError:
            continue
    
    disk_io = psutil.disk_io_counters()
    
    # network information
    network_info = []

    if_addrs = psutil.net_if_addrs()

    for interface_name, interface_addresses in if_addrs.items():

        for address in interface_addresses:

            info = {"interface": interface_name}

            if str(address.family) == 'AddressFamily.AF_INET':

                info.update({
                    "ip_address": address.address,
                    "netmask": address.netmask,
                    "broadcast_ip": address.broadcast,
                })

            elif str(address.family) == 'AddressFamily.AF_PACKET':

                info.update({
                    "mac_address": address.address,
                    "netmask": address.netmask,
                    "broadcast_mac": address.broadcast,
                })

            network_info.append(info)
    
    net_io = psutil.net_io_counters()

    # final dictionary
    return {

        "os": {
            "hostname": uname.node,
            "os": uname.system,
            "major_release": uname.release,
            "version_number": uname.version,
        },

        "cpu": {
            "cpu_architecture": uname.machine,
            "cpu": cpu.get("brand_raw", "unknown"),
            "cpu_identifier": uname.processor,
            "cpu_cores": psutil.cpu_count(logical=False),
            "cpu_logical_processors": psutil.cpu_count(logical=True),
            "cpu_max_freq": f"{cpufreq.max:.2f}mhz" if cpufreq else "unknown",
            "cpu_min_freq": f"{cpufreq.min:.2f}mhz" if cpufreq else "unknown",
            "cpu_current_freq": f"{cpufreq.current:.2f}mhz" if cpufreq else "unknown",
            "cpu_usage_per_core": cpu_usage_per_core,
            "cpu_total_usage": f"{psutil.cpu_percent()}%",
        },

        "boot": {
            "boot_time": f"{boot_time.year}/{boot_time.month}/{boot_time.day} {boot_time.hour}:{boot_time.minute}:{boot_time.second}",
        } ,

        "memory": {
            "memory_total": get_size(svmem.total),
            "memory_available": get_size(svmem.available),
            "memory_used": get_size(svmem.used),
            "memory_percent": svmem.percent,
        },

        "swap": {
            "swap_total": get_size(swap.total),
            "swap_free": get_size(swap.free),
            "swap_used": get_size(swap.used),
            "swap_percent": swap.percent,
        },

        "disk_partitions": partitions_info,

        "disk_io": {
            "total_read": get_size(disk_io.read_bytes),
            "total_write": get_size(disk_io.write_bytes),
        },

        "network_interfaces": network_info,

        "network_io": {
            "local_ip": socket.gethostbyname(socket.gethostname()),
            "mac": ":".join(re.findall("..", "%012x" % uuid.getnode())),
            "bytes_sent": get_size(net_io.bytes_sent),
            "bytes_received": get_size(net_io.bytes_recv),
        },

    }


# the real work starts here
if __name__ == "__main__":

    system_info = get_system_info()

    print("\n" + "system_info:" + "\n" + "=" * 20 + "\n")
    print_dict(system_info)
    print("\n")