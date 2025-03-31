from scapy.all import sniff, IP, TCP, UDP, ICMP
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

protocol_counts = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "Other": 0
}

def process_packet(packet):
    if IP in packet:
        if packet.haslayer(TCP):
            protocol_counts["TCP"] += 1
        elif packet.haslayer(UDP):
            protocol_counts["UDP"] += 1
        elif packet.haslayer(ICMP):
            protocol_counts["ICMP"] += 1
        else:
            protocol_counts["Other"] += 1

def visualize_data():
    labels = list(protocol_counts.keys())
    sizes = list(protocol_counts.values())

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Network Traffic Analysis by Protocol")
    plt.axis('equal')
    plt.show()

def main():
    num_packets = 50
    print(f"Starting packet sniffing for {num_packets} packets. Please wait...")
    sniff(count=num_packets, prn=process_packet)
    print("Packet capture complete!")
    print("Captured protocol counts:", protocol_counts)
    
    visualize_data()

if __name__ == "__main__":
    main()
