def to_rna(dna_strand):
    translator = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna = ''
    try:
        for dna in dna_strand:
            rna += translator[dna]
    except KeyError:
        raise ValueError('Invalid input!')

    return rna
