
def computer(gravity, noun=12, verb=2):
    """
    ** day 2 part 1 **
    Return: the first integer of the code given an input to elements [1] and [2]
    Parameters: - gravity: the input code of the computer, a list of all ints
                - noun: the value for second element in code, set to default
                   of 12 as given in prompt
                - verb: the value for the thrid element in code, set to default
                    of 2 as given in prompt
    - process opcode in groups of 4 numbers.
    - first digit [0]:
        - if 1: add values from elems [1] and [2] of opcode
            then store in element indicated in elem [3]
        - 2: multiply instead of add the condition for the above case.
        - 99: halt program
    - digits after 1st digit indicate location not value!

    Precondition: The noun and verb values are set to default 12, 2 respectively.

    """

    g_copy = gravity[:]
    g_copy[1] = noun
    g_copy[2] = verb

    n = 4
    i = 0
    #look at sections of 4 ints at a time then update to next four
    while i < len(g_copy):

        opcode = g_copy[i]
        i1,i2,i3 = g_copy[i+1],g_copy[i+2],g_copy[i+3]

        #halt if 99
        if opcode == 99:
            break
        # [0]=1 -> add
        elif opcode == 1:
            g_copy[i3] = g_copy[i1] + g_copy[i2]

        # [0]=2 -> multiply
        elif opcode == 2:
            g_copy[i3] = g_copy[i1] * g_copy[i2]

        #move ot next group of 4
        i += n

    return g_copy[0]


def find_noun_verb(gravity):
    """
    ** day 2 part 2 **
    Return: solution to the answer of "What is 100 * noun + verb?" Wherein noun
        and verb were to be found to produce a target value given in the prompt
    Parameters: gravity - input computer code
    Preconditions: noun and verb are between 0 and 99.
    """
    target = 19690720
    for noun in range(0,100):
        for verb in range(0,100):
            if computer(gravity, noun, verb) == target:
                return (100 * noun + verb)
