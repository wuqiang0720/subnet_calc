import ipaddress

def calculate_subnet(network_cidr):
    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
    except ValueError as e:
        return f"Invalid network: {e}"

    result = {
        "Network address": str(network.network_address),
        "Broadcast address": str(network.broadcast_address),
        "Netmask": str(network.netmask),
        "Wildcard mask": str(network.hostmask),
        "Number of hosts": network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses,
        "Hosts": [str(ip) for ip in network.hosts()]
    }
    return result

if __name__ == "__main__":
    # 这里写死了一个示例网络，可以用参数或输入替换
    net = "192.168.1.0/28"
    info = calculate_subnet(net)

    if isinstance(info, str):
        print(info)
    else:
        print(f"Subnet calculation for {net}:")
        for k, v in info.items():
            if k == "Hosts":
                print(f"{k} (first 5 hosts): {v[:5]} ...")
            else:
                print(f"{k}: {v}")
