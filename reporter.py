import os

def generate_report(name, dna, analysis, protein):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    REPORTS_DIR = os.path.join(BASE_DIR, "results", "reports")

    if not os.path.isdir(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    report_path = os.path.join(REPORTS_DIR, f"{name}_report.txt")

    with open(report_path, "w") as f:
        f.write(f"Gene Name: {name}\n")
        f.write(f"Sequence Length: {analysis['length']}\n")
        f.write(f"GC Content: {analysis['gc_content']}%\n")
        f.write(f"AT/GC Ratio: {analysis['ac_gc_ratio']}\n")
        f.write(f"Start Codon Found: {analysis['start_codon']}\n")
        f.write(f"Stop Codon Found: {analysis['stop_codon']}\n")
        f.write(f"Protein Length: {len(protein)} amino acids\n")

    # protein file
    PROTEINS_DIR = os.path.join(BASE_DIR, "results", "proteins")
    if not os.path.isdir(PROTEINS_DIR):
        os.makedirs(PROTEINS_DIR)

    protein_path = os.path.join(PROTEINS_DIR, f"{name}_protein.txt")

    with open(protein_path, "w") as p:
        p.write(protein)
