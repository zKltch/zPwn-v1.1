from pwn import *

context.arch='amd64'
r=''

def s(payload): return r.send(payload)
def sl(payload): return r.sendline(payload)
def sla(after, payload): return r.sendlineafter(after, payload)
def sa(after, payload): return r.sendafter(after, payload)
def rc(num): return r.recv(num)
def rcl(): return r.recvline()
def rcls(num): return r.recvlines(num)
def rcu(payload): return r.recvuntil(payload)
def ita(): return r.interactive()
def cl(): return r.close()
def debug(): context.log_level='DEBUG'
def gdbat(): return gdb.attach(r)


def r(REMOTE_INFO:str):
    global r

    REMOTE_IP=REMOTE_INFO.split()[1]
    REMOTE_PORT=int(REMOTE_INFO.split()[2])
    r=remote(REMOTE_IP,REMOTE_PORT)

def p(REMOTE_INFO:str):
    global r
    r=process(REMOTE_INFO)
    
