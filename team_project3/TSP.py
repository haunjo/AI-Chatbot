import random
from tempfile import tempdir
import matplotlib.pyplot as plt
#TSP알고리즘


POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 9		# 하나의 염색체에서 유전자 개수		
fitness = []

Supergene = 0

"""
    
서울 : 0 인천 : 1 대전 : 2 춘천 : 3 강릉 : 4 대구 : 5 울산 : 6 부산 : 7 광주 : 8
    
"""

#distance[x][y] 를 참조하면 x와 y의 거리를 알 수 있음
distance = [
         [0, 30, 140, 75, 168, 237, 303, 325, 268],
         [30, 0, 140, 105, 198, 247, 315, 334, 257],
         [140, 140, 0, 173, 205, 119, 190, 200, 141],
         [75, 105, 173, 0, 102, 238, 293, 323, 313],
         [168, 198, 205, 102, 0, 213, 247, 287, 340],
         [237, 247, 119, 238, 213, 0, 71, 88, 173],
         [303, 315, 190, 293, 247, 71, 0, 44, 222],
         [325, 334, 200, 323, 287, 88, 44, 0, 202],
         [268, 257, 141, 313, 340, 173, 222, 202, 0]
          ]



# 염색체를 클래스로 정의한다. 
class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		# 유전자는 리스트로 구현된다. 
        self.fitness = 0		# 적합도
        if self.genes.__len__()==0:	# 염색체가 초기 상태이면 초기화한다. 
            i = 0
            x = 0
            self.genes.append(x)
            self.genes.append(random.randint(1,8))
            while len(self.genes) < SIZE:
                self.genes.append(self.Find_nearst(self.genes[i+1]))
                i += 1
                 
    #a = 3
    #[75, 105, 173, 0, 102, 238, 293, 323, 313]
    #sorted = [0, 75,102,105, 173, 238, 293,313,323]
    def Find_nearst(self, a):
        nearest = sorted(distance[a])
        for i in nearest[1:]:
            if distance[a].index(i) not in self.genes:
                y = distance[a].index(i)
                return y           
    
    def cal_fitness(self):		# 적합도를 계산한다. 
        self.fitness = 0
        value = 0
        for i in range(len(self.genes)-1):
            value += distance[self.genes[i]][self.genes[i+1]]
        value += distance[self.genes[-1]][0]
        self.fitness = 3000 - value
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
    #print("father", father.genes, "mother", mother.genes)
    idx1, idx2 = random.sample(range(1, SIZE), 2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    #print(idx1,idx2)
    a = father.genes[idx1:idx2]
    b = mother.genes[idx1:idx2]
    #print(a, b)
    child1 = father.genes
    child2 = mother.genes
    #print("child1", child1, "child2", child2)
    for i in b:
        d = child1.index(i)
        temper1 = child1[d]
        child1[d] = child1[idx1 + b.index(i)]
        child1[idx1 + b.index(i)] = temper1
    for j in a:
        c = child2.index(j)
        temper2 = child2[c]
        child2[c] = child2[idx1 + a.index(j)]
        child2[idx1 + a.index(j)] = temper2
    #print("child1", child1, "child2", child2)
    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            target1, target2 = random.sample(range(1,SIZE), 2)
            #temp = c.genes[target1]
            #c.genes[target1] = c.genes[target2]
            #c.genes[target2] = temp
            #c.genes[target1], c.genes[target2] = c.genes[target2], c.genes[target1]
            c.genes[target1], c.genes[target2] = swap(c.genes[target1], c.genes[target2])
       

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b

# 메인 프로그램
population = []
i=0

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

while population[0].cal_fitness() < 2000:
    new_pop = []

    new_pop.append(Chromosome(population[0].genes))
    #엘리트교배, 적합도가 가장 높았던 부모의 유전자를 그대로 가져옴
    print_p(new_pop)
    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식 세대가 부모 세대를 대체한다. 
    # 깊은 복사를 수행한다. 
    #print_p(new_pop)
    population = new_pop.copy();    
    
    # 돌연변이 연산
    #print_p(population)
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    #print(Supergene)
    if population[0].cal_fitness() >= 1500:
        MUTATION_RATE = 0.075
        Supergene = 1
        
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
    
    