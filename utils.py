def read_fasta(fasta_path):
    sequences = ""
    with open(fasta_path) as file:
        for line in file:
            if not line.startswith(">"):
                sequences += line.strip()

    return sequences
