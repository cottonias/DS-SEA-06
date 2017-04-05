# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 19:50:34 2017

This code is used to parse the file "chipotle.tsv" and analyze the data.

@author: cottonias
"""
# Import tab delimited file
import pandas as pd
food = pd.read_csv('chipotle.tsv', sep='\t')

food.head()
food.tail()
food.describe() # count the # of order_ids

food.item_name.value_counts() # shows the count of items

# Or for cleaner code to count only orders with "Burrito"
df = food[food['item_name'].str.contains('Burrito')]
print df.item_name.value_counts() # Chicken burritos are more popular

df = food[food['item_name'].str.contains('Chicken Burrito')].choice_description
df_pinto = df[df.str.contains('Pinto Beans')]
chicken_with_pinto_beans = df_pinto.count()    # 105 orders were for Chicken Burritos with Black Beans

df = food[food['item_name'].str.contains('Chicken Burrito')].choice_description
df_black = df[df.str.contains('Black Beans')]
chicken_with_black_beans = df_black.count()    # 282 orders were for Chicken Burritos with Black Beans
print "For Chicken Burrito orders, %s were with pinto beans and %s with black beans" % (chicken_with_pinto_beans,chicken_with_black_beans)