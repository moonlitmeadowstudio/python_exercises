# BEGIN (write your solution here)
def to_rna(dna):
    dna_to_rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna = ""
    for i in dna:
        rna += dna_to_rna.get(i)
    return rna
# END


print(to_rna('ACGTGGTCTTAA'))
# 'UGCACCAGAAUU'