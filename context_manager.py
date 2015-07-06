__author__ = 'root'

"""
Context manager

with expression as variable:
    suite
"""

"""
Simple context manager
"""
with open("/etc/hosts", "r") as hosts_in:
    print(hosts_in.read())

"""
Bad Dual context manager
"""
with open("/etc/hosts", "r") as hosts_in:
    with open("/tmp/hosts", "w") as hosts_out:
        hosts_out.write(hosts_in.read())

"""
Good Dual context manager
"""
with open("/etc/hosts", "r") as hosts_in, open("/tmp/hosts", "w") as hosts_out:
    hosts_out.write(hosts_in.read())


