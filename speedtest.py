import speedtest

s = speedtest.Speedtest()

print("Wait...\n")

down = s.download() / 1048576
up = s.upload() / 1048576
ping = round(s.results.ping)

print(f"Download: {down} mbps")
print(f"Upload: {up} mbps")
print(f"Ping: {ping} ms")

"""
I'll love the light for it shows me the way, yet I'll endure the darkness because it shows me the stars.
"""
