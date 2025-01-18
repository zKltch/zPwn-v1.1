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


def r(REMOTE_INFO:str,REMOTE_LOCAL:bool):
    global r

    if REMOTE_LOCAL==True:
        r=process(REMOTE_INFO)
        
    
    else:                                           
        

        REMOTE_IP=REMOTE_INFO.split()[1]
        REMOTE_PORT=int(REMOTE_INFO.split()[2])

        r=remote(REMOTE_IP,REMOTE_PORT)
