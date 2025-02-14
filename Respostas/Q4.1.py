import ipaddress
import time

def validar_ipv4_no_prefixo(ip, prefixo):
    rede = ipaddress.ip_network(prefixo, strict=False)
    return ipaddress.ip_address(ip) in rede

def main():
    inicio = time.time()
    ip = "192.168.1.5"
    prefixo = "192.168.1.0/24"
    resultado = validar_ipv4_no_prefixo(ip, prefixo)
    print(f"O IP {ip} está no prefixo {prefixo}: {resultado}")
    print(f"Tempo total de execução: {time.time() - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
