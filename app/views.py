import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from scapy.all import rdpcap, IP, TCP
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import np

# Directories
PCAP_DIRECTORY = "pcap_files"
STATIC_DIRECTORY = "static"

# Ensure directories exist
if not os.path.exists(PCAP_DIRECTORY):
    os.makedirs(PCAP_DIRECTORY)

if not os.path.exists(STATIC_DIRECTORY):
    os.makedirs(STATIC_DIRECTORY)


def home(request):
    # Fetch recently uploaded files
    recent_files = [f for f in os.listdir(PCAP_DIRECTORY) if f.endswith(".pcap")]
    return render(request, "app/home.html", {"recent_files": recent_files})


@csrf_exempt
def upload_pcap(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("pcap_file")
        if not uploaded_file:
            return JsonResponse({"error": "No file uploaded"}, status=400)

        # Save the uploaded PCAP file
        file_path = os.path.join(PCAP_DIRECTORY, uploaded_file.name)
        with default_storage.open(file_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Analyze the PCAP file
        try:
            packets = rdpcap(file_path)
            df = extract_packet_data(packets)
            protocol_counts, total_bandwidth = analyze_packet_data(df)

            # Generate protocol distribution graph
            graph_path = os.path.join(STATIC_DIRECTORY, "protocol_distribution.png")
            generate_protocol_graph(protocol_counts, graph_path)

            # Detect potential port scans
            port_scan_suspects = detect_port_scanning(df)

            return JsonResponse({
                "message": f"File {uploaded_file.name} analyzed successfully.",
                "total_bandwidth": f"{total_bandwidth} bytes",
                "graph_path": f"/{graph_path}",
                "port_scan_suspects": port_scan_suspects.to_dict(),
            })
        except Exception as e:
            return JsonResponse({"error": f"Error analyzing PCAP file: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def analyze_pcap_file(pcap_path):
    packets = rdpcap(pcap_path)
    packet_data = []
    bandwidth = 0
    ip_matrix = {}

    for packet in packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto = packet[IP].proto
            size = len(packet)

            bandwidth += size
            packet_data.append({"src_ip": src_ip, "dst_ip": dst_ip, "protocol": proto, "size": size})

            # Build communication matrix
            if src_ip not in ip_matrix:
                ip_matrix[src_ip] = {}
            if dst_ip not in ip_matrix[src_ip]:
                ip_matrix[src_ip][dst_ip] = 0
            ip_matrix[src_ip][dst_ip] += size

    df = pd.DataFrame(packet_data)

    # Calculate metrics
    protocol_distribution = df["protocol"].value_counts()
    top_communicators = df.groupby(["src_ip", "dst_ip"]).size().reset_index(name="packet_count")
    latency = calculate_latency(packets)  # Calculate latency distribution

    return {
        "bandwidth": bandwidth,
        "protocol_distribution": protocol_distribution,
        "top_communicators": top_communicators,
        "latency_distribution": latency,
        "ip_matrix": ip_matrix,
    }

def calculate_latency(packets):
    latency_data = []
    for packet in packets:
        if "time" in packet:
            latency_data.append(packet.time)
    return np.diff(latency_data) if len(latency_data) > 1 else []


def extract_packet_data(packets):
    packet_data = []
    for packet in packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
            size = len(packet)
            packet_data.append({"src_ip": src_ip, "dst_ip": dst_ip, "protocol": protocol, "size": size})
    return pd.DataFrame(packet_data)


def analyze_packet_data(df):
    protocol_counts = df["protocol"].value_counts()
    total_bandwidth = df["size"].sum()
    return protocol_counts, total_bandwidth


def generate_protocol_graph(protocol_counts, output_path):
    plt.figure(figsize=(8, 6))
    protocol_counts.plot(kind="bar", color="skyblue")
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.savefig(output_path)
    plt.close()


def detect_port_scanning(df, threshold=100):
    port_scan_df = df[df["protocol"] == 6].groupby("src_ip")["dst_ip"].count()
    port_scan_suspects = port_scan_df[port_scan_df > threshold]
    return port_scan_suspects

@csrf_exempt
def generate_pcap(request):
    # Generate PCAP file
    if request.method == "POST":
        interface = request.POST.get("interface")
        if not interface:
            return JsonResponse({"error": "No interface selected"}, status=400)

        pcap_file = PCAP_DIRECTORY / f"{interface}_capture.pcap"
        command = ["tcpdump", "-i", interface, "-c", "100", "-w", str(pcap_file)]
        try:
            subprocess.run(command, check=True)
            return JsonResponse({"message": f"PCAP file {pcap_file.name} generated successfully"})
        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": f"Failed to capture packets: {e}"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)
