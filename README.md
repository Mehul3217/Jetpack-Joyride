													DASS Assignment-1
														The Mandalorian

Packages Required:
	colorama
	pip3 install colorama

Instructions:

1. Run:
       python3 jetpack.py

2. Rules(how to play):
->  a,w,d: to control Left,Up,Right movements of Mandalorian
->  ' ': Press space bar to activate the shield
->  b: to fire bullets
->  k: to in increase game speed for 10 sec.
->  q: to quit the game
->  When w is not prssed the mandlorian is attrcted towards ground due to gravity.
->  Enemies(beams,ice balls) and boss killed by shooting bullets by pressing 'b' but contact with them kills Mandalorian
->  You have 4 lives,killed 4 times, game over
->  You can have sheild by pressing 'Space bar' which protects you from all sort of enemies,lasts for 10 sec and require 60 sec to backup.
->  Collecting coin gains in 2 points,killing enemies 3 points,killing boss adds 5 points. 
->  You are given 180 sec to win the game
->  The dragon fires snowballs to defend himself , the mandlorian must dodge them . If he is hit by the snowballs he losses life.

3. Classes:
a) Board: 		Creates 50x1000 matrix for gameplay having all things inside it.
b) Mandalorian: Creates main character of play i.e. Mando
c) Ball: 		For ice balls used by enemy
d) Enemy: 		Creates boss enemy
e) Obstacle: 	Creates all beams,coins patterns,etc..
f) Magnet: 		Creates magnet which causes constant attractive force towards it
g) Sheild: 		Creates sheild which protects mando from obstacles
h) Background: 	Creates ground and sky
i) Bullets: 	Creates bullets used by mando to kill enemies

4. Files:
.   alarmexception.py
.   background.py
.	board.py
.	bullets.py
.	enemy.py
.	input.py
.	jetpack.py
.	magnet.py
.	mandalorian.py
.	obstacle.py
.	shield.py


5. Features of Game:
- Inheritance :- The mandlorian and boss enemy are inherited from the Person class.
	      :- Obstacles of different types are inherited from Obstacle class.
- Encapsulation and Abstraction :- The fact that I have made classes for each object in the game.
- Polymorphism :- Function overriding has been used in placing and removing obstacles in the sub classes of Main class Obstacle.
