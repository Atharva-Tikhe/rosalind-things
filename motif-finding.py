rseq = 'GATATGCTGATATATATGGCAT'
rmotif = 'ATAT'


seqlist = [x for x in rseq]

motiflist = [x for x in rmotif]

# print(seqlist)
# print(motiflist)

index = 0

# print(seqlist[index:index + len(rmotif) + 1])


test = seqlist[index:index + len(rmotif) + 1]

print(test)

for i in test:
    if i not in rmotif:
        test.remove(i)
        print(test)
        print(index)
    elif i in rmotif:
      pass



j = 1
# print(rseq[j:j + len(motiflist) + 1])
# for i in range(len(rseq)):
#
#     if seqlist[i:i + len(motiflist) + 1] == motiflist:
#         print(i)
#