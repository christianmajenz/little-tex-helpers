#######################################################################################################################################################################################
## Python script to remove comments from LaTeX documents.                                                                                                                            ##
## You can specify a minimal number of % characters that will be treated as visual helper line to keep the overview in the code. %--- will also be treated as visual element.        ##
## Starts by removing parts that are inactivated using \iffalse \fi, and then continues to take care of the parts commented out using %.                                             ##
## You can choose whether to remove comments in the header as well, or only in the body.                                                                                             ##
#######################################################################################################################################################################################


# get user input: filename, how many %s are too many, include header?
filename=raw_input("TeX-file to remove comments from, without the extension \".tex\"")
minpercent=input("How many % characters do you use at least for visual structuring elements in the code?")
cleanheader=raw_input("Do you want to purge the header as well (y/n)?")


# read file
file=open(filename+".tex", "r")
lines=file.readlines()
file.close()

# remove parts that are inactivated using \iffalse \fi
linenum=0
iniffalse=False
while len(lines)>linenum:
	if lines[linenum].startswith("\\iffalse"):
		iniffalse=True
	localiniffalse=iniffalse
	if lines[linenum].startswith("\\fi"):
		iniffalse=False
	if localiniffalse:
		lines.pop(linenum)
		linenum-=1
	linenum+=1


# set linenumber back to 0
linenum=0
# skip the header if desired
if cleanheader!='y':
	while not lines[linenum].startswith('\\begin{document}\n'):
		linenum+=1

# remove comments starting with fewer than minpercent % characters
# make reference string
ref=""
for i in range(minpercent):
	ref+='%'
#loop over lines
while len(lines)>linenum:
	# where is the %?
	pos=lines[linenum].find('%')
	#if there is a %:
	if pos!=-1:
		# if the % is not the start of a visual element	
		if not (lines[linenum][pos:].startswith('%---')|lines[linenum][pos:].startswith(ref)):
			# if the % is the first character, remove the line.
			if pos==0:
				lines.pop(linenum)
				linenum-=1
				# else, remove the comment only
			else:
				lines[linenum]=lines[linenum][:pos-1]+"\n"
	linenum+=1



# write a new comment-free file
file=open(filename+"_no_comments.tex", "w")
file.writelines(lines)
file.close()

# success indicator
print("success! new TeX-file "+filename+"_no_comments.tex produced.")