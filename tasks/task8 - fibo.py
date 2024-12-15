memory = [0, 1]

def fibo(n):
    if n < 0:
        return None
    if n < len(memory):
        return memory[n]
    else:
        memory.append(fibo(n-1) + fibo(n-2))
        return memory[n]
    
print(fibo(n = 88))
print(memory)