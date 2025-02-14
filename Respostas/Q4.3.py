import ipaddress
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_prefix = False
        self.prefix = None

class IPv6Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix):
        binary_prefix = self.ipv6_to_binary(prefix)
        node = self.root
        for bit in binary_prefix:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_prefix = True
        node.prefix = prefix

    def longest_prefix_match(self, ip):
        binary_ip = self.ipv6_to_binary(ip)
        node = self.root
        longest_match = None
        for bit in binary_ip:
            if bit in node.children:
                node = node.children[bit]
                if node.is_prefix:
                    longest_match = node.prefix
            else:
                break
        return longest_match
    
    def ipv6_to_binary(self, ip):
        network = ipaddress.ip_network(ip, strict=False)
        return bin(int(network.network_address))[2:].zfill(128)[:network.prefixlen]

trie = IPv6Trie()
prefixes = ["2001:db8::/32", "2001:db8:1234::/48"]
for prefix in prefixes:
    trie.insert(prefix)

ip_test = "2001:db8:1234:5678::1"

start_time = time.time()
match = trie.longest_prefix_match(ip_test)
end_time = time.time()

print("Prefixo mais longo correspondente:", match)
print("Tempo de execução:", end_time - start_time, "segundos")
