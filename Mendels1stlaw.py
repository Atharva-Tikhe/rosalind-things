# mendel's first laws representing the probabilites of offsprings having dominant phenotype
import numpy as np

AA = np.array([[0, 0]])
Aa = np.array([[0, 1]])
aa = np.array([[1, 1]])
each_prob = []
each_dominant_fraction = []
sum_prob = []

def probability_dom(k,m,n):
    input = [k,m,n]
    counter = 0
    for ii in range(len(input)):
        print(ii)
        for iii in range(len(input)):
            t = k + m + n
            
            if ii != iii:
                probability = (input[ii]/t) * (input[iii]/(t-1))
            else:
                probability = (input[ii]/t) * ((input[iii]-1)/(t-1))
            each_prob.append(probability)
            counter += 1
    print(each_prob)

    for iT in [AA,Aa,aa]:
        for i in [AA,Aa,aa]:
            matrix = iT.T * i
            dominant_fraction = np.sum(matrix == 0) / 4
            each_dominant_fraction.append(dominant_fraction)
    print(each_dominant_fraction)

    for n in range(0,counter):
        sum_prob.append(each_dominant_fraction[n]*each_prob[n])
    print(sum(sum_prob))

            
probability_dom(26,21,20)