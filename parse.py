import json

def parse(section):
	with open(section+".json") as datafile:
		data = json.load(datafile)

	topics = []
	for x in data:
		topics.append(x['topic'])

	return topics

def main():
	parse("quant")

if __name__ == "__main__":
	main()