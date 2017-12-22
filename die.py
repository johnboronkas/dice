from random import randint
from enum import Enum
import numpy as np

def open_roll(low, high, total=0):
	roll = randint(low, high)
	total += roll
	if roll != high:
		return total
	else:
		return open_roll(low, high, total - 1)

def score(rolls):
	score = [np.percentile(rolls, 10), np.percentile(rolls, 25), np.percentile(rolls, 50), np.percentile(rolls, 75), np.percentile(rolls, 90)]
	score.append(score[SIdx.Bot.value]*0.2 + score[SIdx.Low.value]*0.25 + score[SIdx.Mid.value]*0.3 + score[SIdx.High.value]*0.2 + score[SIdx.Top.value]*0.05)
	return score
		
runs = 1000000

RIdx = Enum(value='RIdx', names='Name Low High Rolls Scores', start=0)
SIdx = Enum(value='SIdx', names='Bot Low Mid High Top Score', start=0)
results = [
	('d4', 		1, 		4, 		[0]*runs,	[0]*len(SIdx)),
	('d4+2', 	1+2,	4+2,	[0]*runs,	[0]*len(SIdx)),
	('d4+4', 	1+4,	4+4,	[0]*runs,	[0]*len(SIdx)),
	('d4+8', 	1+8,	4+8,	[0]*runs,	[0]*len(SIdx)),
	('d6', 		1, 		6, 		[0]*runs,	[0]*len(SIdx)),
	('d6+2', 	1+2, 	6+2, 	[0]*runs,	[0]*len(SIdx)),
	('d6+4', 	1+4, 	6+4, 	[0]*runs,	[0]*len(SIdx)),
	('d6+8', 	1+8, 	6+8, 	[0]*runs,	[0]*len(SIdx)),
	('d8', 		1, 		8, 		[0]*runs,	[0]*len(SIdx)),
	('d8+2', 	1+2, 	8+2, 	[0]*runs,	[0]*len(SIdx)),
	('d8+4', 	1+4, 	8+4, 	[0]*runs,	[0]*len(SIdx)),
	('d8+8', 	1+8, 	8+8, 	[0]*runs,	[0]*len(SIdx)),
	('d10', 	1, 		10, 	[0]*runs,	[0]*len(SIdx)),
	('d10+2', 	1+2, 	10+2, 	[0]*runs,	[0]*len(SIdx)),
	('d10+4', 	1+4, 	10+4, 	[0]*runs,	[0]*len(SIdx)),
	('d10+8', 	1+8, 	10+8, 	[0]*runs,	[0]*len(SIdx)),
	('d12', 	1, 		12, 	[0]*runs,	[0]*len(SIdx)),
	('d12+2', 	1+2, 	12+2, 	[0]*runs,	[0]*len(SIdx)),
	('d12+4', 	1+4, 	12+4, 	[0]*runs,	[0]*len(SIdx)),
	('d12+8', 	1+8, 	12+8, 	[0]*runs,	[0]*len(SIdx)),
	('d20', 	1, 		20, 	[0]*runs,	[0]*len(SIdx)),
	('d20+2', 	1+2, 	20+2, 	[0]*runs,	[0]*len(SIdx)),
	('d20+4', 	1+4, 	20+4, 	[0]*runs,	[0]*len(SIdx)),
	('d20+8', 	1+8, 	20+8, 	[0]*runs,	[0]*len(SIdx)),
]

for run in range(runs):
	for die in range(len(results)):
		d = results[die]
		d[RIdx.Rolls.value][run] = open_roll(d[RIdx.Low.value], d[RIdx.High.value])

for result in range(len(results)):
	scores = score(results[result][RIdx.Rolls.value])
	results[result][RIdx.Scores.value][SIdx.Bot.value] = scores[SIdx.Bot.value]
	results[result][RIdx.Scores.value][SIdx.Low.value] = scores[SIdx.Low.value]
	results[result][RIdx.Scores.value][SIdx.Mid.value] = scores[SIdx.Mid.value]
	results[result][RIdx.Scores.value][SIdx.High.value] = scores[SIdx.High.value]
	results[result][RIdx.Scores.value][SIdx.Top.value] = scores[SIdx.Top.value]
	results[result][RIdx.Scores.value][SIdx.Score.value] = scores[SIdx.Score.value]

results.sort(key=lambda r: r[RIdx.Scores.value][SIdx.Score.value])
for result in results:
	print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
		result[RIdx.Name.value],
		int(result[RIdx.Scores.value][SIdx.Bot.value]),
		int(result[RIdx.Scores.value][SIdx.Low.value]),
		int(result[RIdx.Scores.value][SIdx.Mid.value]),
		int(result[RIdx.Scores.value][SIdx.High.value]),
		int(result[RIdx.Scores.value][SIdx.Top.value]),
		round(result[RIdx.Scores.value][SIdx.Score.value], 2),
	))
