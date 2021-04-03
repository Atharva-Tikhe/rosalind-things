import time
actual_index = 0 # using this makes it easier to globalize the current index
results = []

def find_motif_index(sequence, motif):
    start = time.perf_counter() # start counter
    global actual_index 
    global results
    # sequence_list = [x for x in sequence]
    #print(len(sequence_list)) check
    for index in range(len(sequence)):
        actual_index = index
        motif_frame = sequence[index: index + len(motif)] # motif frame
        # print(motif_frame)
        frame_string = motif_frame
        result = frame_matching(frame_string, motif)
        if result != None:
            print(result, end=' ')
            # results.append(result)
           
    end = time.perf_counter()
    return end-start


def frame_matching(frame_string : str, motif: str):
    # print(f'frame string coming from the other function {frame_string}')
    global actual_index
    for frame_index in frame_string:
        if frame_index in motif:
            if frame_string == motif:
                return actual_index + 1
                

timed_sample = find_motif_index("CCACTTTTCTTAGGGTCGAAGGACGGTCGAAGGTCGAAGTGGTCGAATCACCGGTC\
GAATGGGGTCGAAATGGTCGAATTGGTCGAAGCGGTCGAAGGTCGAAGGTCGAATATTTGGGTCGAAGGTCGAACGGGT\
CGAAAAGGTCGAAAATGGTATGGTCGAAGCTTGGGTCGAACGCGGTCGAATGGTCGAAATCTGGTCGAAGTGGGTCGGTCGAAAGGTCGAAGGTCGAAG\
GTCGAAAAGGTCGAACGTCTACCCAGGTCGAAATCGGTCGAAAAAGGTCGAAGGTCGAAGATATGGTCGAAAGGTCGAAGTGGGTCGAATTGCCTCCTCGGGGTC\
GAAATCCTTTGGTCGAACGGTCGAATGGTCGAAGGTCGAACTCGTATATTGATAGTTACCAGGTCGAAGCGGTCGAAGGTCGAATTGAATGGGGTTCATTAGGTCG\
AACTACCATGGGTCACGGTCGAAAGGTCGAACGTGGTCGAACAAGGTCGAATTAGGTCGAACCCAAAACCGGGTCGAAGAGGTCGAACGAGGTCGAAATGTGCCCGGTCGAAGCGGGTCGAAGGTCGA\
AAGGTCGAAAGGTCGAAAGGTCGAATAGGTCGAATCTGGGGTCGAAAGGTCGAATGGTCGAACTGAGCGGGAATCGGTCGAACTAGGTCGAAGGTCGAAACTCGGTCGAACCGGTCGAAATGGTCGAACGGGTCG\
AAGGTCGAAGGCTCGGGTCGAAGGAATCTACCTTAGGTCGAACGGGGTCGAATAGGTCGAAGGTCGAATAGGGTCGAAGGTCGAAGGGTCGAATAGTCATAGGTCGAAGGTCGAAGGTCGAATCGGTCGAAGGTCGAA\
AGGTCGAATGGGTCGAATTCGGTCGAATGGGGTCGAATGGTCGAACTTTAAAGGTCGAACCACTTTTCTTAGGGTCGAAGGACGGTCGAAGGTCGAAGTGGTCGAATCACCGGTC\
GAATGGGGTCGAAATGGTCGAATTGGTCGAAGCGGTCGAAGGTCGAAGGTCGAATATTTGGGTCGAAGGTCGAACGGGT\
", "GGTCGAAGG")

print(f'\ntime : {timed_sample}')




