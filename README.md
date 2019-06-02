# game-reflexes
This game created for educational purpose using Raspberry Pi 3B+

There are 2 buttons and 1 red led which turns on random time. Which player is faster his/her green led blinks to inform that he/she was faster :)

You can view working version on youtube https://www.youtube.com/watch?v=vFSlp5xVFC0
Also connect schema can be viewed from the **reflexes-game-schema.png** file

All pins are BCM numbers (not BOARD):
```
Random turn on red LED    => 17
Player 1:
  Green Led               => 27
  Button                  => 22
Player 2:
  Green Led               => 23
  Button                  => 24
```

When you start app using `$ python game-reflexes.py` you will see message in the log like *Game just started* and later red led will turn on in a random time. It will be on till one of players will click the button to get his/her point.
