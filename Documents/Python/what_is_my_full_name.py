def what_is_my_full_name(**kwargs):
  if 'first_name' not in kwargs.keys() and 'last_name' not in kwargs.keys():
    return "Nobody"
  elif 'first_name' in kwargs.keys() and 'last_name' not in kwargs.keys():
    return kwargs['first_name']
  elif 'first_name' not in kwargs.keys() and 'last_name' in kwargs.keys():
    return kwargs['last_name']
  else:
    return kwargs['last_name'] + ' ' +kwargs['first_name']

print(what_is_my_full_name(first_name="CG", last_name="Y"))
print(what_is_my_full_name(first_name="CG"))
print(what_is_my_full_name(last_name="Y"))
print(what_is_my_full_name())
