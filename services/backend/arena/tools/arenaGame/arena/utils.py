

#############################################################################################################
#	BATTLE
#############################################################################################################

def getStat(base, iv, lvl):
	return (2 * base + iv * 7) * lvl / 100 + 5

def getHpStat(base, iv, lvl):
	return (2 * base + iv * 7) * lvl / 100 + lvl + 10