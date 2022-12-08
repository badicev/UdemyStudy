from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("Hero name", ["Dark Willow", "Mars", "Invoker", "Mirana", "Luna"])
my_table.add_column("Attribute", ["Intelligence", "Strength", "Intelligence", "Agility", "Agility"])
my_table.align = "l"
print(my_table)