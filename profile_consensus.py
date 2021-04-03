import pandas as pd
import profile_consensus_helper as helper

seq_df = pd.DataFrame(helper.dna_strings)

counted_residues = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
# print(seq_df)
count_list = []
for i in range(len(seq_df)):
    item = seq_df[1][i]
    counted_residues[item] += 1

# buff = []
# for i in counted_residues:
#     buff.append(counted_residues[i])


# count_list.append(buff)
# print(counted_residues)

# # print(seq_df[0]<-column;[1]<-row)

# count_df = pd.DataFrame(counted_residues, index=['A','C','G','T'])

# print(count_list)
print(counted_residues)

profile_df = pd.DataFrame(counted_residues, index=['A','C','G','T'])
print(profile_df)
