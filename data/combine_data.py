import csv

def combine_data(paths, outpath):
	data = []
	labels = []

	outdata = []

	features = []

	header = False


	for file in paths:
		with open(file, 'r') as in_file:
			reader = csv.reader(in_file, delimiter=';')

			line_count = 0

			for row in reader:
				temprow = row
				if line_count == 0:
					if header is False:
						temprow.append('color')
						outdata.append(temprow)
						header = True

					pass
				else:
					temp = int(row[-1])
					val = None

					if temp < 4:
						row[-1] = 0
					if temp < 7:
						row[-1] = 1
					else:
						row[-1] = 2

					if 'red' in file:
						row.append(0)
					else:
						row.append(1)	
					outdata.append(row)

				line_count += 1

	with open(outpath, 'w') as outfile:
		writer = csv.writer(outfile, delimiter=',')

		writer.writerows(outdata)


if __name__ == '__main__':

	data_paths = ['winequality-red.csv', 'winequality-white.csv']

	outpath = r'winequality.csv'

	combine_data(data_paths, outpath)

