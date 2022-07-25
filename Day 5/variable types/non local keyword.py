def f1():
  x = "John"
  def f2():
    nonlocal x
    x = "hello"
  f2()
  return x

print(f1())