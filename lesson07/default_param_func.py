def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  while True:
    ok = input(prompt)
    if ok in ('y', 'yes', 'ye'):
      return True
    if ok in ('n', 'no', 'nop', 'nope '):
      return False
    retries = retries -1
    if retries < 0:
      raise OSError('uncooperative use')
    print(complaint)

ask_ok('Do you really want to quit?')