import pandas as pd
import os

file = open('sequences.fasta', 'r')
read = file.readlines()

sequences = []
final_seq = []
dna_strings = []

for i in read:
    if i.startswith('>'):
        pass
    else:
        sequences.append(i)

for seq in sequences:
    final_seq.append(seq.split())
x = 0
while x < len(final_seq):
    element = final_seq[x]
    dna_strings.append([nuc for nuc in element[0]])
    x += 1

# print(dna_strings)

dna_string_df = pd.DataFrame(dna_strings)
# print(dna_string_df)

nuc_counts = {'A':0,'C':0,'G':0,'T':0}

buff = []

for col in range(len(dna_string_df.columns)):
    for i in dna_string_df[col]:
        nuc_counts[i] += 1
        if i == dna_string_df[col]:
            print(i)
            
   
print(dna_string_df)
   
# print(buff)
    
# print(nuc_counts)

        
    