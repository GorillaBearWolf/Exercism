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
