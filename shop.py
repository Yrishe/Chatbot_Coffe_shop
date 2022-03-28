from time import sleep

# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")

  drink_tem = drink_temp()
  size = get_size()
  drink_type = get_drink_type()
  cup = cup_type()

  print("Alright, that's a {} {} {} in {}!".format(size,drink_tem,drink_type,cup))
  nome = input("Can I get your name please? \n> ")
  print("Thanks, {}! Your drink will be ready shortly.".format(nome))
  print("...")
  sleep(1)
  print("Your order is ready!")


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] latte \n> ")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return 'latte' + order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] Latte \n[b] Non-Fat Latte \n[c] Soy Latte \n> ")
  if res == 'a':
    return ' latte'
  elif res == 'b':
    return ' non-fat latte'
  elif res == 'c':
    return ' soy latte'
  else:
    print_message()
    return order_latte()

def cup_type():
  res = input("Would like to use a new plastic cup or your reusable cup? \n[a] New Plastic Cup \n[b] Your Reusable Cup \n> ")
  if res == 'a':
    return ' new plastic cup'
  elif res == 'b':
    return ' your reusable cup'
  else:
    print_message()
    return cup_type()

def drink_temp():
  res = input("What would like to have, hot or iced drink?\n[a] Hot Drink \n[b] Iced Drink \n> ")
  if res == 'a':
    return 'Hot'
  elif res == 'b':
    return 'Iced'
  else:
    print_message()
    return drink_temp()


# Call coffee_bot()!
coffee_bot()

