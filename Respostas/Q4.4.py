import ipaddress
import time
import random

def generate_random_prefix():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0/{random.randint(8, 24)}"

def longest_prefix_match_linear(ip, prefixes):
    matched_prefix = None
    for prefix in prefixes:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(prefix, strict=False):
            if matched_prefix is None or ipaddress.ip_network(prefix).prefixlen > ipaddress.ip_network(matched_prefix).prefixlen:
                matched_prefix = prefix
    return matched_prefix

class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix):
        node = self.root
        binary_prefix = self._ip_to_bin(prefix)
        for bit in binary_prefix:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.prefix = prefix

    def search(self, ip):
        node = self.root
        binary_ip = self._ip_to_bin(ip + "/32")
        longest_match = None
        for bit in binary_ip:
            if bit in node.children:
                node = node.children[bit]
                if node.prefix:
                    longest_match = node.prefix
            else:
                break
        return longest_match

    def _ip_to_bin(self, prefix):
        net = ipaddress.ip_network(prefix, strict=False)
        return bin(int(net.network_address))[2:].zfill(32)[:net.prefixlen]

prefixes = [generate_random_prefix() for _ in range(1000)]
random_ip = "192.168.1.55"

start = time.time()
linear_result = longest_prefix_match_linear(random_ip, prefixes)
linear_time = time.time() - start

trie = Trie()
for p in prefixes:
    trie.insert(p)

start = time.time()
trie_result = trie.search(random_ip)
trie_time = time.time() - start

print(f"IP consultado: {random_ip}")
print(f"Busca Linear: {linear_result}, Tempo: {linear_time:.6f} segundos")
print(f"Busca Trie: {trie_result}, Tempo: {trie_time:.6f} segundos")
