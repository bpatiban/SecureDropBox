import sys
import os



def sxor(s1,s2):
  return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def generate_xor(input1, input2):
        
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        #f1,f2,f3 with r4,45,r6
	if(input1.endswith("-1") and input2.endswith("R5")):
                filename = input1.replace("-1","R8")
         	print filename
		r8 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
        elif(input1.endswith("-2") and input2.endswith("R4")):
                filename = input1.replace("-2","R7")
         	print filename
		r8 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
	elif(input1.endswith("-3") and input2.endswith("R6")):
                filename = input1.replace("-3","R9")
         	print filename
		r8 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename

def generate_xor2(input1, input2):
        
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        #f1,f2,f3 with r4,45,r6
	if(input1.endswith("R6") and input2.endswith("R7")):
                filename = input1.replace("R6","R67") 
         	print filename
		r67 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r67)
		print "Xoring done " + filename
        elif(input1.endswith("R3") and input2.endswith("R8")):
                filename = input1.replace("R3","R38")
         	print filename
		r38 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r38)
		print "Xoring done " + filename
	elif(input1.endswith("R1") and input2.endswith("R4")):
                filename = input1.replace("R1","R14")
         	print filename
		r14 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r14)
		print "Xoring done " + filename
	if(input1.endswith("R8") and input2.endswith("R9")):
                filename = input1.replace("R8","R89")
         	print filename
		r89 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r89)
		print "Xoring done " + filename
        elif(input1.endswith("R4") and input2.endswith("R5")):
                filename = input1.replace("R4","R45")
         	print filename
		r45 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r45)
		print "Xoring done " + filename
	elif(input1.endswith("R2") and input2.endswith("R6")):
                filename = input1.replace("R2","R26")
         	print filename
		r26 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r26)
		print "Xoring done " + filename
	elif(input1.endswith("R2") and input2.endswith("R5")):
                filename = input1.replace("R2","R25")
         	print filename
		r25 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r25)
		print "Xoring done " + filename
	if(input1.endswith("R3") and input2.endswith("R7")):
                filename = input1.replace("R3","R37")
         	print filename
		r37 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r37)
		print "Xoring done " + filename
        elif(input1.endswith("R1") and input2.endswith("R9")):
                filename = input1.replace("R1","R19")
         	print filename
		r19 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r19)
		print "Xoring done " + filename
	





def main():
	import sys
	#input1 = "card1.jpg-1"
	#input2 = "card1.jpgR5"
        selected_file = sys.argv[1]
	L1 = list()
	L2 = list()
	L3 = list()
	os.chdir("/home/jui/cloud_")
	#L1: Stores random files r1-6
	for files in os.listdir("."):
		for i in range(6):
	  		if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L1.insert(i,files)

	
	#L2: Stores all the files
	   			
	for files in os.listdir("."):
		for i in range(3):
	  		if (files.startswith(selected_file) and files.endswith("-"+str(i+1))):
	     			L2.insert(i,files)
    #f1,f2,f3 with r4,45,r6
	#L2
	for p in L2: 
          for q in L1:
               if(p.endswith("-1") and (q.endswith("R5"))):
                       generate_xor(p,q)
               if(p.endswith("-2") and (q.endswith("R4"))):
                        generate_xor(p,q)
               if(p.endswith("-3") and (q.endswith("R6"))):
                        generate_xor(p,q)
	
	#L3: Store R1,R2,R3,r4,r5,r6,r7,r8,r9 in List 3	
	for files in os.listdir("."):
		for i in range(9):
	  		if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)
              
	for p in L3: 
          for q in L3:
               if(p.endswith("R6") and (q.endswith("R7"))):
                       generate_xor2(p,q)
               if(p.endswith("R3") and (q.endswith("R8"))):
                        generate_xor2(p,q)
               if(p.endswith("R1") and (q.endswith("R4"))):
                        generate_xor2(p,q)
	       if(p.endswith("R8") and (q.endswith("R9"))):
                       generate_xor2(p,q)
               if(p.endswith("R4") and (q.endswith("R5"))):
                        generate_xor2(p,q)
               if(p.endswith("R2") and (q.endswith("R6"))):
                        generate_xor2(p,q)
	       if(p.endswith("R2") and (q.endswith("R5"))):
                       generate_xor2(p,q)
               if(p.endswith("R3") and (q.endswith("R7"))):
                        generate_xor2(p,q)
               if(p.endswith("R1") and (q.endswith("R9"))):
                        generate_xor2(p,q)




if __name__=="__main__":
    main()
       










