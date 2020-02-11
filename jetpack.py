import signal
import os
import time
import random
from colorama import init,Fore,Back
init()

from alarmexception import AlarmException
from input import _getChUnix as getChar
from background import Background
from board import Board
from mandalorian import Mandalorian
from bullets import Bullets
from enemy import Enemy,Ball
from shield import Shield
from magnet import Magnet
from obstacle import Obstacle_0,Obstacle_1,Obstacle_2,Obstacle_3,Obstacle_4,Obstacle_5

obj_shield = Shield()
listb = []
listm = []
pro = []
boss_list = []
boss_pro = []

obj_board = Board(50,2000)
obj_board.create()
y=-10
for i in range(8):
	x=1+random.randint(0,34)
	y+=20+random.randint(30,40)
	obj_magnet = Magnet(x,y)
	obj_magnet.place_magnet(obj_board.get_mat())
	listm.append(obj_magnet)

obj_mandalorian = Mandalorian(45,0)
obj_mandalorian.start_pos(obj_board.get_mat())
obj_background = Background()
obj_background.create_ground(obj_board.get_mat())
obj_background.create_sky(obj_board.get_mat())

c=2
d=3
while d<650:
	chance = random.randint(0,5)
	e=d
	if chance == 0:
		obs = Obstacle_0(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	elif chance == 1:
		obs = Obstacle_1(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	elif chance == 2:
		obs = Obstacle_2(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	elif chance == 3:
		obs = Obstacle_3(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	elif chance == 4:
		obs = Obstacle_4(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	elif chance == 5:
		obs = Obstacle_5(c,d)
		obs.place_obstacle(obj_board.get_mat(),c,d)
	c=2+random.randint(0,34)
	d+=8+random.randint(2,6)

boss = Enemy(15,790)
boss.put_boss(15,790,obj_board.get_mat())
k=0
yes=0
last=0
sh=0
t=0.1
boo=0
act=0
yo=1
acc=1
meh=0
time1=0
time2=0

def movmandalorian(left,right):
    global sh,last,t,boo,act,yo,acc,meh,time1,time2
    def alarmhandler(signum, frame):
        ''' input method '''
        raise AlarmException

    def user_input(timeout=0.15):
        ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    char = user_input()
    if char == " ":
    	if obj_shield.get() == 1:
    		sh=1
    		yo=0
    		obj_shield.activate(obj_board.get_mat(),obj_mandalorian)
    		last=time.time()
    		time1=10
    		time2=60

    if char == 'k':
    	boo = 1
    	act = time.time()

    if char == 'b':
    	var=Bullets(obj_mandalorian.get_x(),obj_mandalorian.get_y()+4);
    	listb.append(var)

    if char == 'd':
    	obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
    	obj_mandalorian.set_y(obj_mandalorian.get_y()+3)
    	xm=obj_mandalorian.get_x()
    	ym=obj_mandalorian.get_y()
    	if ym+3 >= right:
    		obj_mandalorian.set_y(right-3)
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	elif ym+2>=790:
    		obj_mandalorian.set_y(787)
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	# elif obj_board.get_mat()[xm][ym] == Fore.GREEN+'0'+'\x1b[0m' and obj_board.get_mat()[xm][ym+1] == Fore.GREEN+'0'+'\x1b[0m' and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
    	# 	obj_mandalorian.set_life(4)   			
    	elif obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_collision():
    		if obj_board.get_mat()[xm][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)	
    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_magnet():    	
    		acc=1
    		meh=1
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	else:
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.set_life()
    			obj_board.spawn_mandalorian(obj_mandalorian,left)

    if char == 'a':
    	obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
    	obj_mandalorian.set_y(obj_mandalorian.get_y()-3)
    	xm=obj_mandalorian.get_x()
    	ym=obj_mandalorian.get_y()
    	if ym < left:
    		obj_mandalorian.set_y(left)
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)

    	elif obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_collision():
    		if obj_board.get_mat()[xm][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_magnet():    	
    		acc=1
    		meh=1
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	else:
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.set_life()
    			obj_board.spawn_mandalorian(obj_mandalorian,left)

    if char == 'q':
    	quit()

    if char == 'w':
    	acc=1
    	obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
    	obj_mandalorian.set_x(obj_mandalorian.get_x()-3)
    	xm=obj_mandalorian.get_x()
    	ym=obj_mandalorian.get_y()
    	if xm <= 0:
    		obj_mandalorian.set_x(1)
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)

    	elif obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)

    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_collision():
    		if obj_board.get_mat()[xm][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+1][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_board.get_mat()[xm+2][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
    			obj_mandalorian.set_coins()
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_magnet():    	
    		acc=1
    		meh=1
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
    	else:
    		if obj_shield.get() == 0 and obj_shield.get2() == 0:
    			obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
    		else:
    			obj_mandalorian.set_life()
    			obj_board.spawn_mandalorian(obj_mandalorian,left)

cou=0
cr=0
x=time.time()
left=k
right=k+204
obj_board.printi(0)
while True:
	boss.put_boss(boss.get_x(),boss.get_y(),obj_board.get_mat())
	time.sleep(0.1)
	vali = 180 - (round(time.time()) - round(x))
	print('\033c')
	print("LIVES:",obj_mandalorian.get_life(),end='\t \t')
	print("COINS:",obj_mandalorian.get_coins(),end='\t \t')
	print("Time Remaining:",vali,end='\t \t')
	print("Boss life:",boss.get_life(),end='\t \t')
	print("Kills:",obj_mandalorian.get_kills(),end='\t \t')
	print("Sheild_duration",time1,end='\t \t')
	print("Sheild_available_in",time2)

	for i in range(len(listm)):
		listm[i].place_magnet(obj_board.get_mat())

	if sh > 0:
		if(round(time.time()) - round(last) >= 70):
			obj_shield.refill()
			sh=0
		elif(round(time.time()) - round(last) >= 10):
			obj_shield.deactivate(obj_board.get_mat(),obj_mandalorian)
			yo=1
		if yo==0:
			time1=9-(round(time.time()) - round(last))
		else:
			time2=70-(round(time.time()) - round(last))

	obj_magnet.check_range(obj_board.get_mat(),listm,left,right,obj_mandalorian)
	if right <= 860:
		if sh == 0 or yo == 1:
			if boo>0:
				if(round(time.time()) - round(act) >= 10):
					boo=0
				else:
					k+=2
					obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
					obj_mandalorian.increment_position(obj_board.get_mat(),0,2)
			else:
				k+=1
				obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
				obj_mandalorian.increment_position(obj_board.get_mat(),0,1)
		else:
			if boo>0:
				if(round(time.time()) - round(act) >= 10):
					boo=0
				else:
					k+=2
					obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),1)
					obj_mandalorian.increment_position(obj_board.get_mat(),1,2)
			else:
				k+=1
				obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),1)
				obj_mandalorian.increment_position(obj_board.get_mat(),1,1)

		if right>=795:
			xm=obj_mandalorian.get_x()
			bm=boss.get_x()
			rm=boss.get_x()+20
			if xm >= bm and xm<=rm:
				pass
			elif xm < bm:
				boss.change_position_up(obj_board.get_mat())
			elif xm+2>rm:
				boss.change_position_down(obj_board.get_mat())
			if time.time() - boss.get_last() >=1.5:
				var1=Ball(xm,boss.get_y()-3)
				boss_list.append(var1)
				var1.increment(obj_board.get_mat())
				boss.set_last(time.time())

	else:
		xm=obj_mandalorian.get_x()
		bm=boss.get_x()
		rm=boss.get_x()+20
		if xm >= bm and xm<=rm:
			pass
		elif xm < bm:
			boss.change_position_up(obj_board.get_mat())
		elif xm+2>rm:
			boss.change_position_down(obj_board.get_mat())
		if time.time() - boss.get_last() >=1.5:
			var1=Ball(xm,boss.get_y()-3)
			boss_list.append(var1)
			var1.increment(obj_board.get_mat())
			boss.set_last(time.time())


	left=k
	right=k+204		
	obj_board.printi(k)

	for i in range(len(listb)):
		listb[i].disappear_bullets(obj_board.get_mat())
		if (i in pro):
			continue
		listb[i].set_y(listb[i].get_y()+5)
		ym=listb[i].get_y()
		xm=listb[i].get_x()
		if ym-5 >= right:
			pro.append(i)
		if ym>=750:
			if obj_board.get_mat()[xm][ym] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-1] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-2] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-3] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-4] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-5] == Fore.GREEN+'0'+'\x1b[0m':
				boss.set_life()
				pro.append(i)
				#listb[i].increment_bullets(obj_board.get_mat())
			elif obj_board.get_mat()[xm][ym] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-1] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-2] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-3] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-4] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-5] in listb[i].get_allowed_collision():
				listb[i].increment_bullets(obj_board.get_mat())
			else:
				pro.append(i)
		elif obj_board.get_mat()[xm][ym] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-1] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-2] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-3] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-4] in listb[i].get_allowed_collision() and obj_board.get_mat()[xm][ym-5] in listb[i].get_allowed_collision():
			listb[i].increment_bullets(obj_board.get_mat())
		elif obj_board.get_mat()[xm][ym] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-1] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-2] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-3] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-4] == Fore.GREEN+'0'+'\x1b[0m' or obj_board.get_mat()[xm][ym-5] == Fore.GREEN+'0'+'\x1b[0m':
			boss.set_life()
			pro.append(i)
		elif obj_board.get_mat()[xm][ym] == Fore.YELLOW+'$'+'\x1b[0m' or obj_board.get_mat()[xm][ym-1] == Fore.YELLOW+'$'+'\x1b[0m' or obj_board.get_mat()[xm][ym-2] == Fore.YELLOW+'$'+'\x1b[0m' or obj_board.get_mat()[xm][ym-3] == Fore.YELLOW+'$'+'\x1b[0m' or obj_board.get_mat()[xm][ym-4] == Fore.YELLOW+'$'+'\x1b[0m' or obj_board.get_mat()[xm][ym-5] == Fore.YELLOW+'$'+'\x1b[0m':
			pass
		else:
			p=max(xm-9,0)
			q=max(ym-10,0)
			a=min(xm+9,47)
			b=min(ym+10,900)
			for c in range(xm,p,-1):
				for j in range(ym,q,-1):
					obj_board.get_mat()[c][j] = " "
				for j in range(ym,b,1):
					obj_board.get_mat()[c][j] = " "
			for c in range(xm,a,1):
				for j in range(ym,b,1):
					obj_board.get_mat()[c][j] = " "
				for j in range(ym,q,-1):
					obj_board.get_mat()[c][j] = " "
			obj_mandalorian.set_kills()
			pro.append(i)


	for i in range(len(boss_list)):
		if (i in boss_pro):
			continue
		boss_list[i].disappear_bullets(obj_board.get_mat())
		boss_list[i].set_y(boss_list[i].get_y()-2)
		ym=boss_list[i].get_y()
		xm=boss_list[i].get_x()
		if ym+2 <= left:
			boss_pro.append(i)
		elif obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
			boss_list[i].increment(obj_board.get_mat())
		elif obj_board.get_mat()[xm][ym] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm][ym+1] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm][ym+2] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+1][ym] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+1][ym+1] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+2][ym+2] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+2][ym] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+2][ym+1] == Fore.RED+'O'+'\x1b[0m' and obj_board.get_mat()[xm+2][ym+2] == Fore.RED+'O'+'\x1b[0m':
			pass
		else:
			if obj_shield.get() == 0 and obj_shield.get2() == 0:
				obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
			else:
				obj_mandalorian.set_life()
				obj_board.spawn_mandalorian(obj_mandalorian,left)
	movmandalorian(left,right)

	if obj_mandalorian.get_life() <= 0 or vali <=0 :
		print("You lose		BETTER LUCK NEXT TIME")
		print("Score:\n")
		print("Lives",obj_mandalorian.get_life(),end='\n')
		print("COINS:",obj_mandalorian.get_coins(),end='\n')
		print("Kills:",obj_mandalorian.get_kills(),end='\n')
		print("Total:",obj_mandalorian.get_coins()*2+obj_mandalorian.get_kills()*3+2*obj_mandalorian.get_life(),end='\n')
		quit()

	elif boss.get_life() <=0 :
		print("Congratulations You Win!!")
		print("Score:\n")
		print("Lives",obj_mandalorian.get_life(),end='\n')
		print("COINS:",obj_mandalorian.get_coins(),end='\n')
		print("Kills:",obj_mandalorian.get_kills(),end='\n')
		print("Total:",obj_mandalorian.get_coins()*2+obj_mandalorian.get_kills()*3+5+2*obj_mandalorian.get_life(),end='\n')
		quit()

	if obj_mandalorian.get_x() < 45:
		var=0
		xm=obj_mandalorian.get_x()
		ym=obj_mandalorian.get_y()
		obj_mandalorian.disappear_mandalorian(obj_board.get_mat(),0)
		if obj_mandalorian.get_x() + acc <= 45:
			obj_mandalorian.set_x(obj_mandalorian.get_x()+acc)
			var=1
		else:
			d=45-obj_mandalorian.get_x()
			obj_mandalorian.set_x(45)
			acc=0
		if meh==1:
			acc=1
			meh=0
		else:
			acc+=1
		obs=0
		if var>0:
			for i in range(acc):
				if obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
					pass
				elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_collision():
					if obj_board.get_mat()[xm][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
				elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_magnet():    	
					acc=1
				else:
					obs=1
					break
				xm+=1
			if obs>0:
				if obj_shield.get() == 0 and obj_shield.get2() == 0:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
				else:
					obj_mandalorian.set_life()
					obj_board.spawn_mandalorian(obj_mandalorian,left)
			else:
				if obj_shield.get() == 0 and obj_shield.get2() == 0:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
				else:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
		else:
			for i in range(d):
				if obj_board.get_mat()[xm][ym] == " " and obj_board.get_mat()[xm][ym+1] == " " and obj_board.get_mat()[xm][ym+2] == " " and obj_board.get_mat()[xm+1][ym] == " " and obj_board.get_mat()[xm+1][ym+1] == " " and obj_board.get_mat()[xm+1][ym+2] == " " and obj_board.get_mat()[xm+2][ym] == " " and obj_board.get_mat()[xm+2][ym+1] == " " and obj_board.get_mat()[xm+2][ym+2] == " ":
					pass
				elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_collision() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_collision():
					if obj_board.get_mat()[xm][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+1][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym+1] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
					if obj_board.get_mat()[xm+2][ym+2] == Fore.YELLOW+"$"+'\x1b[0m':
						obj_mandalorian.set_coins()
				elif obj_board.get_mat()[xm][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+1][ym+2] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+1] in obj_mandalorian.get_magnet() and obj_board.get_mat()[xm+2][ym+2] in obj_mandalorian.get_magnet():    	
					acc=1
				else:
					obs=1
					break
				xm+=1
			if obs>0:
				if obj_shield.get() == 0 and obj_shield.get2() == 0:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
				else:
					obj_mandalorian.set_life()
					obj_board.spawn_mandalorian(obj_mandalorian,left)
			else:
				if obj_shield.get() == 0 and obj_shield.get2() == 0:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),1)
				else:
					obj_mandalorian.reappear_mandalorian(obj_board.get_mat(),0)
	else:
		acc=1