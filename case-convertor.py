import sys

# function that reads the lines and converts them in the resulting file
def line_reader_lower(first_file, result_file):
	line = first_file.readline()
	while line:
		result_file.write(line.upper())
		line = first_file.readline()

def line_reader_upper(first_file, result_file):
	line = first_file.readline()
	while line:
		result_file.write(line.lower())
		line = first_file.readline()

# the second command line argument is the the name of the file we want to convert
file_name = sys.argv[2]
# the third command line argument is the name of the result file
result_file_name = sys.argv[3] + ".txt"

"""
the first command line argument is the choice
if it is 0 then the script converts a lowercase file to an uppercase file
if it is 1 then the script does the opposite
"""
convertor_type = sys.argv[1]

if convertor_type == '0':
	print("Converting a lowercase file to an uppercase file...")
	lowercase_file = open(file_name, "r", encoding="utf8")
	uppercase_file = open(result_file_name, "a", encoding="utf8")
	line_reader_lower(lowercase_file, uppercase_file)
	lowercase_file.close()
	uppercase_file.close()
elif convertor_type == '1':
	print("Converting an uppercase file to a lowercase file...")
	uppercase_file = open(file_name, "r", encoding="utf8")
	lowercase_file = open(result_file_name, "a", encoding="utf8")
	line_reader_upper(uppercase_file, lowercase_file)
	lowercase_file.close()
	uppercase_file.close()
else:
	print("Conversion type not available.")

