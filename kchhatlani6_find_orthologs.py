#!/usr/bin/python
import argparse
import subprocess
import shlex 

parser = argparse.ArgumentParser()
parser.add_argument("-i1", help = "Input fasta file 1.")
parser.add_argument("-i2", help = "Input fasta file 2.")
parser.add_argument("-o", help = "output filename.")
parser.add_argument("-t", help = "Put n for nucleotide sequence and p for protein sequence.")
args = parser.parse_args()

file1 = args.i1
file2 = args.i2
output_file = args.o
input_seq_type = args.t   

#Creating  databases  using makeblastdb and query each set against the opposite database
if input_seq_type == "n":
	file1_db = subprocess.check_output(shlex.split("makeblastdb -in " + str(file1) + " -dbtype nucl -out db1"))
	final1 = subprocess.check_output(shlex.split("blastn -db db1 -query " + str(file2) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out outputfile_1"))
	file2_db = subprocess.check_output(shlex.split("makeblastdb -in " + str(file2) + " -dbtype nucl -out db2"))
	final2 = subprocess.check_output(shlex.split("blastn -db db2 -query " + str(file1) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out outputfile_2")) 
	
	#Grabbing the first two columns from output and comparing them
	cola = []                  
	colb = []
    	with open("outputfile_1") as fh1:
    		for line in fh1.readlines():
    			if line.startswith("lcl"):
    				cola.append(line.split()[0])
    			if line.startswith("lcl"):
    				colb.append(line.split()[1])
	list_1 = []
    	for i,j in zip(cola,colb):
    		list_1.append(i+"\t"+j+"\n")
	
	col1 = []                  
	col2 = []
   	with open("outputfile_2") as fh2:
    		for line in fh2.readlines():
    			if line.startswith("lcl"):
    				col1.append(line.split()[0])         
    			if line.startswith("lcl"):
    				col2.append(line.split()[1])          
	list_2 = []
    	for i,j in zip(col1,col2):
    		list_2.append(j+"\t"+i+"\n") #Inversing the list to find reciprocals      

	output_list = []
    	for x in list_1:                         
    		if x in list_2:
    			output_list.append(x) #Finding best hits               

elif input_seq_type == "p":

        file1_db =subprocess.check_output(shlex.split("makeblastdb -in " + str(file1) + " -dbtype prot -out db1"))
        final1 =subprocess.check_output(shlex.split("blastp -db db1 -query " + str(file2) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out outputfile_1"))
        file2_db =subprocess.check_output(shlex.split("makeblastdb -in " + str(file2) + " -dbtype prot -out db2"))
        final2 =subprocess.check_output(shlex.split("blastp -db db2 -query " + str(file1) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out outputfile_2"))

	cola = []
        colb  = []
        with open("output_file_1") as fh1:
        	for line in fh1.readlines():
                	if line.startswith("lcl"):
                    		cola.append(line.split()[0])
                	if line.startswith("lcl"):
                    		colb.append(line.split()[1])

	list_1 = []
        for i,j in zip(cola,colb):
        	list_1.append(i+"\t"+j+"\n")

        col1 = []
        col2 = []
	with open("outputfile_2") as fh2:
        	for line in fh2.readlines():
                	if line.startswith("lcl"):
                    		col1.append(line.split()[0])
                	if line.startswith("lcl"):
                    		col2.append(line.split()[1])
	
	list_2 = []
        for i,j in zip(col1,col2):
        	list_2.append(j+"\t"+i+"\n") #Inversing the list to find reciprocals

        output_list = []
	for x in outputlist_1:      
        	if x in outputlist_2:
                	output_list.append(x) #Finding best hits 

with open(output_file, 'w') as output_fh:
	for orthologs in output_list:
		output_fh.writelines(orthologs)

final=subprocess.check_output(shlex.split("rm outputfile_1 outputfile_2 db1.ndb  db1.nin  db1.nsq  db1.nto  db2.nhr  db2.not  db2.ntf  db1.nhr  db1.not  db1.ntf  db2.ndb  db2.nin  db2.nsq  db2.nto"))
