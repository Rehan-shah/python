from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name" , 
                 ["Pikachu" ,"Squritle", 
                  "charmander"] )
table.add_column("Type" , ["Electric","Water","Fire"])
table.align = "l"
print(table)
