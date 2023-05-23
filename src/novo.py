def soma(x: float, y: float) -> float:
    return x + y
 

if __name__ == "__main__":
   print(soma(10, 10))



def fatorial(n):
  if n == 0 or n == 1:
    return 1;
  else:
    return n * fatorial(n - 1)


print(fatorial(5))
