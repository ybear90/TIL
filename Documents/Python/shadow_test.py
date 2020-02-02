test_var = 10

def func1():
  test_var = 12
  print("func1 test: ", test_var)
  def func2():
    test_var = 100
    print("func2 test: ", test_var)
  func2()
  
print(test_var)
func1()
