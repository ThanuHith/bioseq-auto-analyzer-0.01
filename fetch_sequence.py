import os
from Bio import Entrez, SeqIO

Entrez.email = "thirdchannel303@gmail.com"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results", "sequences")

os.makedirs(RESULTS_DIR, exist_ok=True)

def fetch_from_ncbi(gene_name):
    handle = Entrez.esearch(db="nucleotide", term=gene_name, retmax=1)
    record = Entrez.read(handle)
    handle.close()

    seq_id = record["IdList"][0]

    fetch_handle = Entrez.efetch(
        db="nucleotide",
        id=seq_id,
        rettype="fasta",
        retmode="text"
    )

    seq_record = SeqIO.read(fetch_handle, "fasta")
    fetch_handle.close()

    sequence = str(seq_record.seq)

    file_path = os.path.join(RESULTS_DIR, f"{gene_name}.fasta")

    with open(file_path, "w") as f:
        f.write(seq_record.format("fasta"))

    return sequence
