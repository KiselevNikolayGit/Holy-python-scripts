tempo = """.t-{} [
	font-size: {}pt;
]

"""

full = ""

for rul in range( 1, 10 ):
	full += tempo.format( rul * 4, rul * 4 )

full = full.replace( "[", "{" )
full = full.replace( "]", "}" )

print( full )