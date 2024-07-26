
def find_gene_positions(gene: str, genome: str):
    findings = []  # a list to return the occurences of the gene in genome
    start_index = 0

    if gene in genome:
        while True:
            if gene not in genome[start_index:]:
                break
            index = genome.find(gene, start_index)
            findings.append(index)
            start_index = index + len(gene)
        return findings
        
    else: # there is no gene in genome
        return None
    

if __name__ == "__main__":
    genome = "ATCGAGATCGACGATCGTAGCTAGCTAGCTAGCGATCGA"
    gene1 = "TAGCTA"
    gene2 = "ATCGA"
    gene3 = "X"

    print(find_gene_positions(gene1, genome))
    print(find_gene_positions(gene2, genome))
    print(find_gene_positions(gene3, genome))
    print(type((find_gene_positions(gene3, genome))))