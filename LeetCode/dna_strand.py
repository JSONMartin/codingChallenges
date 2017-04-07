def DNA_strand(dna):
    encodings = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    return "".join([encodings[x] for x in dna])


DNA_strand("ATTGC")
