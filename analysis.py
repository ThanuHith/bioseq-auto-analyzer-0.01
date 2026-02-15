def analysis_sequence(seq):
    length = len(seq)

    g = seq.count("G")
    c = seq.count("C")
    a = seq.count("A")
    t = seq.count("T")

    gc_content = ((g + c) / length) * 100
    ac_gc_ratio = (a+t) / (g+c)  if (g+c) != 0 else 0

    start_codon = seq.find("ATG")
    stop_codon = any(condon in seq for condon in ["TAG", "TAA", "TGA"])

    return {
        "length": length,
        "gc_content": round(gc_content,2),
        "ac_gc_ratio":round(ac_gc_ratio,2),
        "start_codon": start_codon,
        "stop_codon": stop_codon,

    }