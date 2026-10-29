# Experiment No.—1: Implementation of Substitution and Transposition Ciphers

# Aim:
# To design and implement algorithms for encryption and decryption using classical substitution and
# transposition techniques.

# a) Caesar Cipher:-

text = input("enter a string: ")
shift = int(input("enter the shift value: "))
encrypted_result = ""
decrypted_result = ""
# Encryption
for char in text:
    if char.isupper():
        encrypted_result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        encrypted_result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        encrypted_result += char
print("Encrypted:", encrypted_result)
# Decryption
for char in encrypted_result:
    if char.isupper():
        decrypted_result += chr((ord(char) - shift - 65) % 26 + 65)
    elif char.islower():
        decrypted_result += chr((ord(char) - shift - 97) % 26 + 97)
    else:
        decrypted_result += char
print("Decrypted:", decrypted_result)

# b) Rail Fence Cipher :-

# Encryption
string = input("Enter a string: ")
def RailFence(txt):
    result = ""
    for i in range(len(txt)):
        if i % 2 == 0:
            result += txt[i]
    for i in range(len(txt)):
        if i % 2 != 0:
            result += txt[i]
    return result
def RailFenceDecrypt(txt):
    result = ""
    even_count = (len(txt) + 1) // 2
    even_part = txt[:even_count]
    odd_part = txt[even_count:]
    for i in range(even_count):
        result += even_part[i]
        if i < len(odd_part):
            result += odd_part[i]
    return result
encrypted = RailFence(string)
print("Encrypted:", encrypted)
decrypted = RailFenceDecrypt(encrypted)
print("Decrypted:", decrypted)



# Experiment No. 2 — RSA Encryption and Decryption

Aim: To implement the RSA algorithm for encryption and decryption of data using public and private keys.

Code:

p, q = 13, 17

n = p * q
t = (p - 1) * (q - 1)
e = 5
d = 77

message = int(input("Enter Your Message: "))

ciphertext = pow(message, e, n)
print("Encrypted message:", ciphertext)

decrypted_message = pow(ciphertext, d, n)
print("Decrypted message:", decrypted_message)




# Experiment No. 3 — Message Authentication Code (MAC)

Aim: To implement a Message Authentication Code for verifying the integrity and authenticity of a message.

Code:

p, q = 13, 17

n = p * q
t = (p - 1) * (q - 1)
e = 5
d = 77

message = int(input("Enter Your Message: "))

ciphertext = pow(message, e, n)
print("Encrypted message:", ciphertext)

decrypted_message = pow(ciphertext, d, n)
print("Decrypted message:", decrypted_message)




# Experiment No. 4 — Digital Signatures

Aim: To implement a digital signature technique for verifying the authenticity and integrity of a message.

Code:

import hmac
import hashlib

key = b"secret123"
message = b"Secure communication is important"

tag = hmac.new(key, message, hashlib.sha256).hexdigest()
print("MAC:", tag)

new_tag = hmac.new(key, message, hashlib.sha256).hexdigest()

if hmac.compare_digest(tag, new_tag):
    print("Message is authentic and has not been modified.")
else:
    print("Message authentication failed.")

new_key = b"secret678"
new_message = b"Secure communication has been modified"

naya_tag = hmac.new(
    new_key, new_message, hashlib.sha256
).hexdigest()

print("NEW_MAC:", naya_tag)

if hmac.compare_digest(tag, naya_tag):
    print("Message is authentic and has not been modified.")
else:
    print("Message authentication failed.")

if tag == new_tag:
    print("Message verification successful.")




# Experiment No. 5 — Diffie–Hellman Key Exchange

Aim: To implement the Diffie–Hellman Key Exchange algorithm for establishing a shared secret key between two communicating parties.

Code:

# Public Values
p = 23
g = 5
# Alice Private Key
a = 6
# Bob's Private Key
b = 15
A = pow(g, a, p)
B = pow(g, b, p)
print("Public Parameters:")
print("Prime (p):", p)
print("Generator (g):", g)
print("\nAlice's Public Key:", A)
print("\nBob's Public Key:", B)
# Calculate Shared Secret
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)
print("\nAlice's Shared Secret:", alice_secret)
print("\nBob's Shared Secret:", bob_secret)
# Verify Key Exchange
if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
    print("Shared Secret Key:", alice_secret)
else:
    print("Key Exchange Failed!")




# Experiment No. 6 — IP Security (IPsec) Configuration

Aim: Configure IPsec on network devices to provide secure communication and protect against unauthorized access and attacks.

Code — Router0:

enable
configure terminal

interface gigabitEthernet 0/2
ip address 10.0.0.1 255.255.255.252
no shutdown
exit

ip route 192.168.2.0 255.255.255.0 10.0.0.2

access-list 110 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255

crypto isakmp policy 10
encryption aes
hash sha
authentication pre-share
group 5
exit

crypto isakmp key CIS123 address 10.0.0.2

crypto ipsec transform-set VPN-SET esp-aes esp-sha-hmac

crypto map VPN-MAP 10 ipsec-isakmp
set peer 10.0.0.2
set transform-set VPN-SET
match address 110
exit

interface gigabitEthernet 0/2
crypto map VPN-MAP
end
write memory
```

Code — Router1:

```
enable
configure terminal

interface gigabitEthernet 0/0
ip address 192.168.2.1 255.255.255.0
no shutdown
exit

interface gigabitEthernet 0/2
ip address 10.0.0.2 255.255.255.252
no shutdown
exit

ip route 192.168.1.0 255.255.255.0 10.0.0.1

access-list 110 permit ip 192.168.2.0 0.0.0.255 192.168.1.0 0.0.0.255

crypto isakmp policy 10
encryption aes
hash sha
authentication pre-share
group 5
exit

crypto isakmp key CIS123 address 10.0.0.1

crypto ipsec transform-set VPN-SET esp-aes esp-sha-hmac

crypto map VPN-MAP 10 ipsec-isakmp
set peer 10.0.0.1
set transform-set VPN-SET
match address 110
exit

interface gigabitEthernet 0/2
crypto map VPN-MAP
end
write memory
```

Verification commands:

```
show crypto isakmp sa
show crypto ipsec sa
```

```
ping 192.168.2.10
ping 192.168.1.10
```

# Experiment No. 7 — Web Security with SSL/TLS

Aim: To implement web security using SSL/TLS by configuring an HTTPS server with a digital certificate and verifying secure communication.

Code — OpenSSL commands:

```
openssl version
```

```
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

Code — `index.html`:

```
<!DOCTYPE html>
<html>
<head>
    <title>SSL/TLS Practical</title>
</head>
<body>
    <h1>Welcome to TYCS SSL Practical</h1>
    <h2>HTTPS is Working Successfully</h2>
</body>
</html>
```

Code — `server.py`:

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

HOST = "localhost"
PORT = 4443

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server.socket = context.wrap_socket(server.socket, server_side=True)

print("HTTPS Server Started")
print(f"Open https://{HOST}:{PORT}")

server.serve_forever()


Run:

python server.py

# Experiment No. 8 — Intrusion Detection System (IDS)

Aim: Set up and configure an intrusion detection system (IDS) to monitor network traffic and detect potential security breaches or malicious activities.

Code — Detection rule (`/etc/suricata/rules/local.rules`):

```
alert icmp any any -> any any (msg:"IDS LAB - ICMP Ping Detected"; sid:1000001; rev:1;)
```

Code — Check installation:

```
suricata --build-info
```

Code — Display rule:

```
cat /etc/suricata/rules/local.rules
```

Code — Validate configuration:

```
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Code — Find network interface:

```
ip -br addr
```

Code — Start Suricata (replace `enp0s3` with your interface):

```
sudo suricata -c /etc/suricata/suricata.yaml -i enp0s3
```

Code — Generate test traffic:

```
ping -c 4 8.8.8.8
```

Code — View alerts:

```
sudo tail -n 20 /var/log/suricata/fast.log
```

```
sudo grep 'IDS LAB - ICMP Ping Detected' /var/log/suricata/fast.log
```

# Experiment No. 9 — Malware Detection

Aim: To detect and analyze malware using the EICAR Anti-Malware Test File and VirusTotal.

Code / Procedure:

```
1. Open the official EICAR website.
2. Download the EICAR anti-malware test file.
3. Open https://www.virustotal.com/
4. Select the file-upload option.
5. Upload the EICAR test file.
6. Wait for the scan to complete.
7. Observe the detection results.
```

# Experiment No. 10 — Firewall Configuration and Rule-Based Filtering

Aim: To configure firewall rules for controlling network traffic and demonstrate rule-based filtering using Windows Defender Firewall.

Code / Procedure:

```
1. Open Windows Defender Firewall with Advanced Security.
2. Select Inbound Rules.
3. Click New Rule.
4. Select Program and click Next.
5. Select This program path.
6. Enter the Chrome executable path:

C:\Program Files\Google\Chrome\Application\chrome.exe

7. Select Allow the connection or Block the connection.
8. Select the required network profiles.
9. Enter the rule name: Chrome Inbound Rule.
10. Click Finish.
11. Verify that the rule appears and is enabled.
```