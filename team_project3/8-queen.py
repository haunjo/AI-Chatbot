import random
from itertools import combinations
import matplotlib.pyplot as plt

from pyparsing import col

POPULATION_SIZE = 10 	# 개체 집단의 크기
MUTATION_RATE = 0.125		# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수		
fitness = []
Supergene = 0

# 염색체를 클래스로 정의한다. 
class Chromosome:
    def __init__(self, g=[]):
        numbers = [0,1,2,3,4,5,6,7]
        self.genes = g.copy()		# 유전자는 리스트로 구현된다. 
        self.fitness = 0		# 적합도
        if self.genes.__len__()==0:	# 염색체가 초기 상태이면 초기화한다. 
            i = 0
            while i<SIZE:
                a = random.choice(numbers)
                self.genes.append(a)
                numbers.remove(a)
                i = i+1
    
    def cal_fitness(self):
        collision = 0
        self.fitness = 0
        # 적합도를 계산한다.
        # 적합도는 서로 공격하지 않는 퀸 쌍의 개수 == -(서로 공격하는 퀸 쌍의 개수)
        for i in range(SIZE):
            if self.genes.count(i) > 1:
                combi = len(list(combinations(range(self.genes.count(i)),2)))
                #print(combi, "쌍의 충돌 일어남")
                collision = collision + combi
        for i in range(SIZE):
                L = self.genes[i]
                check_board = [0,1,2,3,4,5,6,7]
                R_board = check_board[check_board.index(L):]
                L_board = check_board[:check_board.index(L)+1]
                L_board.reverse()
                test = [9,9,9,9,9,9,9,9]
                test1 = [9,9,9,9,9,9,9,9]
                test[i:len(R_board)] = R_board
                del test[8:]
                test1[i:len(L_board)] = L_board
                del test1[8:]
                test[test.index(L)] = 9
                test1[test1.index(L)] = 9
                #print(test, test1)
                for k in range(SIZE):
                    if test[k] == self.genes[k]:
                        collision = collision + 1
                    if test1[k] == self.genes[k]:
                        collision = collision + 1
        self.fitness = 28 - collision
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

# 염색체와 적합도를 출력한다. 
def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i += 1
    print("")

# 선택 연산
def select(pop):
    max_value  = sum([c.cal_fitness() for c in population])
    #print(max_value)
    pick    = random.uniform(0, max_value)
    current = 0
    
    # 룰렛휠에서 어떤 조각에 속하는지를 알아내는 루프
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c

# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)
    index = random.randint(1, SIZE - 2)
    #print(father.genes, mother.genes, "부모")
    child1 = father.genes[:index-1] + mother.genes[index-1:index+1] + father.genes[index+1:]
    child2 = mother.genes[:index-1] + father.genes[index-1:index+1] + mother.genes[index+1:]
    #print(child1, child2, "자식")
    #child1 = father.genes[:index] + mother.genes[index:] 
    #child2 = mother.genes[:index] + father.genes[index:] 

    #이 연산은 father와 mother에서 각 len=2 의 분량만큼 유전자를 인덱스 슬라이싱으로 자르고
    #서로 바꾸는 연산이다. father.genes[:index-1] + mother.genes[index-1:index+1] + father.genes[index+1:]
    #를 보면 chil1은 중간에 mother의 염색체 2개가 들어간 것을 볼 수 있다.
    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes[i] = random.randint(0,7)

# 메인 프로그램
population = []
i=0

#a = Chromosome()
#a.genes = [3,6,2,7,1,4,0,5]
#print(a.cal_fitness())

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
#population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

while population[0].cal_fitness() < 28:
    new_pop = []

    #엘리트교배, 적합도가 가장 높았던 부모의 유전자를 그대로 가져옴
    new_pop.append(population[0])

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))
    
    #엘리트교배, 적합도가 가장 높았던 부모의 유전자를 그대로 가져옴
    #new_pop.append(population[0])
    
    # 자식 세대가 부모 세대를 대체한다. 
    # 깊은 복사를 수행한다. 
    population = new_pop.copy();    
    
    # 돌연변이 연산
    # 적합도가 27 이상인 유전자가 나오면 그 유전자에 대해서는 돌연변이를 수행하지 않는다.
    for c in population[Supergene:]: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    for x in population[:3]:
        fitness.append(x.cal_fitness())
    count += 1
    if count > 100 :
        plt.plot(fitness)
        plt.show()
        break
    
    #변이확률의 동적변화
    if population[0].cal_fitness() >= 26:
        MUTATION_RATE = 0.075
        Supergene = 1

if population[0].cal_fitness() == 28:
    plt.plot(fitness)
    plt.show()