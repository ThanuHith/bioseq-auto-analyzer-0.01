import sys
from fetch_sequence import fetch_from_ncbi
from analysis import analysis_sequence
from converter import dna_to_rna , rna_to_protein
from reporter import generate_report
from utils import read_fasta

def main():
   if len(sys.argv) < 2:
       print("Usage: python main.py <gene_name or fasta file>")
       return
   input_value = sys.argv[1]
   if input_value.endswith(".fasta"):
       sequence = read_fasta(input_value)
       gene_name = input_value.replace(".fasta", "")
   else:
       gene_name = input_value
       sequence = fetch_from_ncbi(gene_name)

   analysis_data = analysis_sequence(sequence)

   rna_seq = dna_to_rna(sequence)  # ✅ DNA string
   protein_seq = rna_to_protein(rna_seq)

   generate_report(gene_name,sequence,analysis_data, protein_seq)

   print("Analysis complete check result folder.")

if __name__ == "__main__":
    main()


