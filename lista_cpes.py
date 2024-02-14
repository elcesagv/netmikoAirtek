with open("LISTA_IP_CPE.txt") as file:
   arrays=file.read().splitlines()
devicesTotal = []
for ip in arrays:
    devicesTotal.append({
    "device_type": "mikrotik_routeros",
    "ip": ip,
    "username": "cgonzalez",
    "password": "cagv8991",
    "port": 22
    })

   


devices = [
 {
    "device_type": "mikrotik_routeros",
    "ip": "10.17.3.16",
    "username": "cgonzalez",
    "password": "cagv8991",
    "port": 22,
    "session_log":"lognetmiko.log"
}
]

for ips in devicesTotal:
    print(ips)