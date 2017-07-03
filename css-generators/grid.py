tempo = ".apart-{}-{} [width: {}%;]\n"

full = ""

for llu in range( 1, 11 ):
	for rul in range( 1, 11 ):
		if rul >= llu:
			rul = float( rul )
			llu = float( llu )
			full += tempo.format( int( llu ), int( rul ), 100 / rul * llu )

full = full.replace( "[", "{" )
full = full.replace( "]", "}" )

print( full )