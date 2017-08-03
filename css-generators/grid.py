tempo = ".g{}x{} [width: {}%;]\n"

full = ""

for llu in range( 1, 21 ):
	for rul in range( 1, 21 ):
		if rul >= llu:
			rul = float( rul )
			llu = float( llu )
			full += tempo.format( int( llu ), int( rul ), 100 / rul * llu )

full = full.replace( "[", "{" )
full = full.replace( "]", "}" )

print( full )