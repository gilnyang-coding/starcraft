from random import*

#유닛 클래스/ 이름, 체력, 속도/ 어느 방향으로 이동/ 피헤 입음
class unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0}유닛이 생성되었습니다.".format(name))

    def move(self,location):
        print("{0}: {1}시 방향으로 움직입니다.[속력:{2}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        if self.hp>damage:
            self.hp-=damage
            print("{0}:{1}의 데미지를 받았습니다. [남은 체력:{2}]".format(self.name,damage, self.hp))
        elif self.hp<=damage:
            self.hp=0
            print("{0}:파괴되었습니다.[남은 체력:{1}]".format(self.name,self.hp))


#어택 유닛 클래스/이름, 체력, 속도, 데미지/ 공격 함
class attack_unit(unit):
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp,speed)
        self.damage=damage

    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격하겠다. [공격력:{2}]".format(self.name,location,self.damage))


#마린 클래스/40, 1, 5/ 스팀팩: 체력 10 감소, 이동 및 공격 속도 증가.
class marine(attack_unit):
    def __init__(self): #어택유닛 클래스의 변수만으로 가겠다는 거.
        attack_unit.__init__(self,"마린", 40, 1, 5)
        
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("스팀팩을 사용합니다.[현재 체력:{0}]".format(self.hp))
            
        else:
            print("체력이 부족합니다. [현재 체력:{0}]".format(self.hp))




#탱크 클래스/150, 1, 35/ 시즈 모드: 탱크를 지상에 고정, 공격력 증가.
class tank(attack_unit):
    
    def __init__(self):
        attack_unit.__init__(self,"탱크", 150, 1, 35)
        self.seize_developed=False
    def seize_mode(self):
        if self.seize_developed==False:
            print("시즈모드를 가동하겠다.")
            self.seize_developed==True
        
        elif self.seize_developed==True:
            print("시즈모드를 중지하겠다.")
            self.seize_developed==False
        


#플라이어블 클래스/ 나는 속도
class flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed


#플라이어블 어택 유닛 클래스/이름, 체력, 나는 속도, 데미지
class flyable_attack_unit(flyable, attack_unit):
    def __init__(self, name, hp, damage, flying_speed):
        attack_unit.__init__(self, name, hp,0, damage) #클래스 불러올 때 부모클래스 변수 빠뜨리면 좆된다.
        flyable.__init__(self, flying_speed)
    def move(self,location):
        print("{0}: {1}시 방향으로 움직입니다.[속력:{2}]".format(self.name,location,self.flying_speed))



    


#레이스 클래스/80, 20, 5/클로킹 모드: 상대방 유닛을 내것으로 만든다.
class wraith(flyable_attack_unit):
    def __init__(self):
        flyable_attack_unit.__init__(self,"레이스", 80, 20, 5)
        self.clock=False #동일한 레이스에서는 클록이 한 번만 불러지고 상태를 변경할 떄마다 그 변경 상태를 유지하고, 다른 레이스면 초기값으로 다시 부른다. 또한 self가 없다면 다른 함수에서 접근할 수 없다.

    def clocking(self):
        #clock=False 만약 clock가 여기 있다면 항상 false상태이므로 위쪽 함수에 넣는다. init함수는 처음에만 불러지고 초기값만 정한다.
        if self.clock==False:
            print("클로킹을 겁니다.")
            self.clock=True
        elif self.clock==True:
            print("클로킹을 중지합니다.")
            self.clock=False

def game_start():
    print("게임을 시작합니다.")

def game_over():
    print("게임을 종료합니다.")

#실제 게임 시작
game_start()
m1=marine()
m2=marine()
m3=marine()

t1=tank()
t2=tank()

w1=wraith()

#유닛 일괄 관리
attack_unit=[]
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동
for unit in attack_unit:
    unit.move(1)

tank.seize_developed=True
print("[알림]:탱크 시즈모드 개발이 완료되었습니다.")

#공격 모드 준비(마린:스팀팩, 탱크: 시즈모드, 레이스: 클로킹모드)
for unit in attack_unit:
    if isinstance(unit,marine): #유닛 중 마린 클래스에 있는 것을 선택
        unit.stimpack()
    elif isinstance(unit, tank):
        unit.seize_mode()
    elif isinstance(unit,wraith):
        unit.clocking()

# 전군 공격
for unit in attack_unit:
    unit.attack(1)

#전군 피해
for unit in attack_unit:
    unit.damaged(randint(5,21)) 

#게임 종료 
game_over()
