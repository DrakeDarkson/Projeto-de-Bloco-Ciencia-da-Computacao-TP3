import ipaddress
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.prefix = None

class IPv4Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, prefix):
        node = self.root
        binary_prefix = self._prefix_to_bin(prefix)
        for bit in binary_prefix:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end = True
        node.prefix = prefix
    
    def longest_prefix_match(self, ip):
        node = self.root
        binary_ip = self._ip_to_bin(ip)
        longest_match = None
        for bit in binary_ip:
            if bit in node.children:
                node = node.children[bit]
                if node.is_end:
                    longest_match = node.prefix
            else:
                break
        return longest_match
    
    def _prefix_to_bin(self, prefix):
        net = ipaddress.IPv4Network(prefix, strict=False)
        return bin(int(net.network_address))[2:].zfill(32)[:net.prefixlen]
    
    def _ip_to_bin(self, ip):
        return bin(int(ipaddress.IPv4Address(ip)))[2:].zfill(32)

if __name__ == "__main__":
    start_time = time.time()
    trie = IPv4Trie()
    prefixes = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
    for p in prefixes:
        trie.insert(p)
    
    ip_to_search = "192.168.1.100"
    result = trie.longest_prefix_match(ip_to_search)
    end_time = time.time()
    
    print(f"Prefixo mais específico para {ip_to_search}: {result}")
    print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")
