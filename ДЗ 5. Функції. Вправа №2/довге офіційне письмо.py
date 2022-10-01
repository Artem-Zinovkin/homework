def options(name1, surname1, name2, surname2, post2):
    return name1, surname1, name2, surname2, post2


if __name__ == '__main__':
    name1, surname1, name2, surname2, post2 = options("Vasily", "Ivanov", "Grigory", "Sidorov", "President")

    letter = f""" Dear {name1} {surname1},

  We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa.
  Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a.

  ________________
  {name2} {surname2}
  {post2}"""

print(letter)




