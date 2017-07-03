def start( ):
	inp = input( "type num: " )
	try:
		print( "Let's try" )
		check( int( inp ) )
	except ValueError:
		print( inp + " is shit. I give you another chance..." )
		start( )

def check( Num ):
	x = int( Num * '1', 2 )
	trying = input( "num greater than zero? y/n " ).lower( )
	if trying == 'y':
		print( x )
	elif trying == 'n':
		y = x / 2
		print( round( y ) )
	else:
		print( trying + " is shit. I give you another chance..." )
		check( Num )

start( )