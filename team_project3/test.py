import random

a, b = random.sample(range(10), 2)

print(a, b)

c = [1,2,3]

c.remove(1,2,3)
print(c)\
    
    
    
    
 
    child1[index1:index2] = father.genes[index1:index2]
    child2[index1:index2]= mother.genes[index1:index2]
    print(child1,child2)
    print(father.genes, mother.genes)
    for i in father.genes[index1:index2]:
        if i in father.genes[:index1] or father.genes[index2:]:
            father.genes[father.genes.index(i)] = mother.genes[child1.index(i)]
    for i in mother.genes[index1:index2]:
        if i in mother.genes[:index1] or mother.genes[index2:]:
            mother.genes[mother.genes.index(i)] = father.genes[child2.index(i)]
        
    print(father.genes, mother.genes)
    
    for j in father.genes:
        while father.genes.count(j) > 1:
            father.genes.remove(j)
    print(father.genes)
    for k in mother.genes:
        while mother.genes.count(j) > 1:
              mother.genes.remove(k)
    print(mother.genes)
    
    print(father.genes, mother.genes)
    
    child1, child2 = father.genes, mother.genes
   
    #child1 = list(set(child1))
    #child2 = list(set(child2))
    for i in child1:
         if i == -1:
             child1.remove(-1)
    for i in child2:
         if i == -1:
             child2.remove(-1)
        
            
    print(child1, child2)