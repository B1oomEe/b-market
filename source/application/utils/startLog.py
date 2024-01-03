def startLog(flask_port, db_host, db_name, db_user):
	"""A function for printing deploy info in console"""
	print("~ Starting `B-market` server...\n")
	print(" _______                                             __                    __ \n"+    
		"/       \                                           /  |                  /  |    \n"+
		"$$$$$$$  |         _____  ____    ______    ______  $$ |   __   ______   _$$ |_   \n"+
		"$$ |__$$ | ______ /     \/    \  /      \  /      \ $$ |  /  | /      \ / $$   |  \n"+
		"$$    $$< /      |$$$$$$ $$$$  | $$$$$$  |/$$$$$$  |$$ |_/$$/ /$$$$$$  |$$$$$$/   \n"+
		"$$$$$$$  |$$$$$$/ $$ | $$ | $$ | /    $$ |$$ |  $$/ $$   $$<  $$    $$ |  $$ | __ \n"+
		"$$ |__$$ |        $$ | $$ | $$ |/$$$$$$$ |$$ |      $$$$$$  \ $$$$$$$$/   $$ |/  |\n"+
		"$$    $$/         $$ | $$ | $$ |$$    $$ |$$ |      $$ | $$  |$$       |  $$  $$/ \n"+
		"$$$$$$$/          $$/  $$/  $$/  $$$$$$$/ $$/       $$/   $$/  $$$$$$$/    $$$$/"
		)
	print("--------------------------------------------------------------------------------\n")
	print(f'~ Started server at port: {flask_port}\n')
	print(f'~ Connected `Postgresql` to host: {db_host};\n to database: {db_name};\n from user: {db_user};\n')
	print("~ Requests logline:\n")