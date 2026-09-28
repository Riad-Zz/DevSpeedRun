"""
Phase 1 - OOP: Class Attributes vs Instance Attributes
"""

class ServerInstance:
    # Class attribute shared across all instances
    total_active_servers = 0
    CLOUD_REGION = "us-east-1"

    def __init__(self, instance_id: str, ip_address: str):
        # Instance attributes unique to each object
        self.instance_id = instance_id
        self.ip_address = ip_address
        ServerInstance.total_active_servers += 1

    def terminate(self):
        ServerInstance.total_active_servers -= 1
        print(f"Terminated {self.instance_id}")

s1 = ServerInstance("srv-01", "10.0.0.1")
s2 = ServerInstance("srv-02", "10.0.0.2")

print(f"Region: {ServerInstance.CLOUD_REGION}")
print(f"Total active servers: {ServerInstance.total_active_servers}")
assert ServerInstance.total_active_servers == 2
