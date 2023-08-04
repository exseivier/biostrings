###biostrings

## Python wrapper package to create DNA data structures like those of R Biostring package. This Python package also include some functions to filter, split sequences and write them to file.


---

## List of functions and classes.

# class DNA:
	:Data structure to hold sequences. It contains 6 slots, first is seq which holds all sequences in a concatenated form. the last 5 slots contains the ids, start and end positions, hide information, and sequence length.

# class lkdList:
	:Data structure to hold a linked list of headers.

# class DNAstuffs:
	:A class with common functions used as parent in child classes loadDNASeqs and splitBioString.
functions.
	: freeDNA. Used to free dynamic allocated memory used in DNA data  structure.
	: getSeq. Used to get a sequence by id.
	: getObject. Returns the DNA data structure object.
	: writeNoHideToFile. Used to write the non-hided sequences to file.
	: filterBioseq. Functions used to drop out those sequences which had a BLASTn hit.

# class loadDNASeqs:
	: A class with functions that creates the DNA data structure.
	: It uses the DNAstuffs functions.

# class splitBioString:
	: A class with functions to split the DNA data structure in fragments of determined size at each determined step.
	: It uses the DNAStuffs functions.

# class lkdList:
	: A class used to create the linked list with the sequence headers.
functions.
	: getObject. Function that returns the linked list object.
	: findIt. Function that finds a header and returns True if it exists in list, otherwise, returns False.
	: freeLkdList. Function that free dynamic allocated memory used to build the linked list.
