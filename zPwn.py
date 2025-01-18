from pwn import *

context.arch='amd64'
r=''

def s(payload): return r.send(payload.encode())
def sl(payload): return r.sendline(payload.encode())
def sla(after, payload): return r.sendlineafter(after.encode(), payload.encode())
def sa(after, payload): return r.sendafter(after.encode(), payload.encode())
def rc(num): return r.recv(num.encode()).decode()
def rcl(): return r.recvline().decode()
def rcls(num): return r.recvlines(num.encode()).decode()
def rcu(payload): return r.recvuntil(payload.encode()).decode()
def ita(): return r.interactive()
def cl(): return r.close()
def debug(): context.log_level='DEBUG'


def r(REMOTE_INFO:str):
    global r

    REMOTE_IP=REMOTE_INFO.split()[1]
    REMOTE_PORT=int(REMOTE_INFO.split()[2])
    r=remote(REMOTE_IP,REMOTE_PORT)

def p(REMOTE_INFO:str):
    global r
    r=process(REMOTE_INFO)
    
