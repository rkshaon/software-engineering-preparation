text = """
In the 16th century, an age of great marine and terrestrial exploration, 
Ferdinand Magellan led the first expedition to sail around the world. As 
a young Portuguese noble, he served the king of Portugal, but he became 
involved in the quagmire of political intrigue at court and lost the king’s 
favor. After he was dismissed from service by the king of Portugal, he 
offered to serve the future Emperor Charles V of Spain.
"""

space_count = sum([1 for char in text if char == ' '])
print(space_count)
