from probability_functions import urn_probability_of_retrieval

x = ["r","r","r","r","b","b","b"]
y = ["r","r","r","r","r","b","b","b","b"]
z = ["r","r","r","r","b","b","b","b"]


chain_to_find_1 = ["r","r","b"]
chain_to_find_2 = ["r","b","r"]
chain_to_find_3 = ["b","r","r"]

final_probability = (urn_probability_of_retrieval(chain_to_find_1, x, y, z) +
                    urn_probability_of_retrieval(chain_to_find_2, x, y, z) +
                    urn_probability_of_retrieval(chain_to_find_3, x, y, z))

print(final_probability)