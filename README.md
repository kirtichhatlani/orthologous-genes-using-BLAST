# Orthologous-genes-using-BLAST
Reciprocal best BLAST hits are pairs of sequences where the best BLAST hit for each sequence is the other sequence. Consider you have a sequence A from species sA whose best hit in species sB is the sequence B. A will be considered a reciprocal best hit of B if the best hit of B in species sA is A.
Example: when you BLAST the complete set of human coding sequences against the complete set of mouse coding sequences, the best hit for the human gene histone H3.1 is the mouse gene histone H3.1 and vice versa. These two genes would be considered reciprocal best hits and orthologous. This is an overly simplistic way of defining orthologous. If, for example, there had been a gene duplication event in mouse lineage yielding two copies of the histone H3 gene, then simply picking one as the ortholog for the human version would be a rather bad idea.

Requirements:
BLAST+ for running makeblastdb and blast. (blast+ executables are assumed to be under your PATH)

Required input files:
Input file 1 - Species 1 FASTA file
Input file 2 - Species 2 FASTA file

Execution of the script:
./kchhatlani6_find_orthologs.py -i1 <Input file 1> -i2 <Input file 2> -o <Output file name> –t <Sequence type – n/p>

Output file:
A file comprising the reciprocal BLAST hits of the two species in output format 6. 

