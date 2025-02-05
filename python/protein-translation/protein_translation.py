<<<<<<< Updated upstream
def proteins(strand):
    protein_dict = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP',
    }

    codon_list = [
        strand[i:i+3] for i in range(0, len(strand), 3)
    ]

    protein_name_list = []

    for codon in codon_list:
        if protein_dict[codon] == 'STOP':
            break
        else:
            protein_name_list.append(protein_dict[codon])


    return protein_name_list
||||||| Stash base
=======
def translate_proteins(rna):
    proteins = []
    for i in range(0, len(rna), 3):
        if ("UAA", "UAG", "UGA") in rna[i:i + 3]:
            return proteins
        if ("AUG") in rna[i:i + 3]:
            proteins.append("Methionine")
        if ("UUU", "UUC") in rna[i:i + 3]:
            proteins.append("Phenylalanine")
        if ("UUA", "UUG") in rna[i:i + 3]:
            proteins.append("Leucine")
        if ("UCU", "UCC", "UCA", "UCG") in rna[i:i + 3]:
            proteins.append("Serine")
        if ("UAU", "UAC") in rna[i:i + 3]:
            proteins.append("Tyrosine")
        if ("UGU", "UGC") in rna[i:i + 3]:
            proteins.append("Cysteine")
        if ("UGG") in rna[i:i + 3]:
            proteins.append("Tryptophan")

    return proteins
>>>>>>> Stashed changes
