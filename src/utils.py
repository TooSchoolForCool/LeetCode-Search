def parse_args(argv):
    """Parse Alfred Arguments
    Args:
        argv: A list of arguments, in which there are only two 
            items, i.e., [mode, {query}].

            The 1st item determines the search mode, there are
            two options:
                1) search by `topic`
                2) search by `problem content/name/index`
            
            The 2nd item is a string which is the user entered 
            from Alfred, which as known as {query}.

    Return:
        A argument dictionary, which contains following fields:
            - mode: topic/problem
            - difficulty: easy/medium/hard
            - query: <query content>
    """
    args = {}

    # determine search mode
    if(argv[0].lower() == "--topic"):
        args["mode"] = "topic"
    else:
        args["mode"] = "problem"

    # parsing query arguments
    query_args = argv[1].split(' ')

    # get difficulty (only take the highest level if
    # multi-level are selected)
    args["difficulty"] = None

    if ("-e" in query_args) or ("--easy" in query_args):
        args["difficulty"] = "Easy"
    if ("-m" in query_args) or ("--medium" in query_args):
        args["difficulty"] = "Medium"
    if ("-h" in query_args) or ("--hard" in query_args):
        args["difficulty"] = "Hard"

    # get query content, any word start with '-' will be ignored
    query_content = ""
    for arg in query_args:
        if arg and arg[0] != '-':
            query_content += arg + " "

    args["query"] = query_content[:-1]

    return args


def is_match(dst, src):
    if dst in src:
        return True
    else:
        return False