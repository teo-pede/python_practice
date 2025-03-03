"""
using pokeapi.co (https://pokeapi.co/docs/v2#genders) to get data:

1. Exercise: Write function to get all pokemons from the API.
    fn name: get_pokemons
    input: None
    output: list of pokemons <list>
    
2. Exercise: Write function to print the pokemon evolution chain in a prettify way.
    fn name: print_evolution_chain
    input: pokemon <str>
    output: None
    print:
        |- pokemon1
            |- pokemon2
                |- pokemon3
                ...
                
3. Exercise: Write the same function as in point 1 using asyncio module - parallel request. (https://docs.python.org/3/library/asyncio.html)
    fn name: get_pokemons_async
    input: None
    output: list of pokemons <list>
"""