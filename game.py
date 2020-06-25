from random import randrange
game_running = True

while game_running == True:

    player = {'name': 'Monster Slayer', 'attack': 15, 'heal': 10, 'health': 100}
    monster = {'name': 'Big Bad Monster', 'attack': 15, 'health': 100}

    print('Enter your name to begin:')
    player['name'] = input()
    print('')
    print('Great! Your name is ' + player['name'] + '!')
    print('')

    new_round = True

    while new_round == True:

      player['attack'] = randrange(15, 30)
      monster['attack'] = randrange(15, 30)
      player['heal'] = randrange(10, 15)

      pHeal = player['heal']

      pA = player['attack']
      mA = monster['attack']

      pH = player['health']
      mH = monster['health']

      player_won = False
      monster_won = False

      print('HP of ' + player['name'] + ' is: ' + str(pH))
      print('HP of ' + monster['name'] + ' is: ' + str(mH))
      print('')

      print('Please select action:')
      print('1) Attack')
      print('2) Heal')
      print('3) Change your name')
      print('4) Change the name of the monster')
      print('5) New Game')
      print('6) Exit Game')

      player_choice = input()

      if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <= 0:
            player_won = True

        else:
          player['health'] = player['health'] - monster['attack']
          if player['health'] <= 0:
            monster_won = True

        print('')
        print('Player attack for ' + str(pA) + ' points of damage!')
        print('Monster attacks back for ' + str(mA) + ' points of damage!')
        print('')

      if player_choice == '2':
        player['health'] = player['health'] + player['heal']
        print('Refreshing heal for ' + str(pHeal) + ' much needed life points :-)')
        print(monster['name'] + ' does nothing...')

      if player_choice == '3':
        print('What is the name of this new hero?')
        print('Enter new name:')
        player['name'] = input()
        print('')
        print('Great! Your name is ' + player['name'] + '!')
        print('')

      if player_choice == '4':
        print('Name of the monster? Enter new name:')
        monster['name'] = input()
        print('')
        print('Now kill ' + monster['name'] + '!')
        print('')

      if player_choice == '5':
        new_round = False

      if player_choice == '6':
        new_round = False
        game_running = False

      if monster_won == True:
        new_round = False
        print('')
        print('Aww.. You lost! Try Again!')
        print('')
        
      if player_won == True:
        new_round = False
        print('')
        print('Congrats! You slayed the monster!')
        print('')



