from Bio.Seq import Seq

def dna_to_rna(dna):
    return dna.replace("T","U")
def rna_to_protein(rna):
    seq = Seq(rna)

    return str(seq.translate(to_stop=True))

