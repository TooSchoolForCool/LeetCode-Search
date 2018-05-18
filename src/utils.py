import argparse

def arg_parse():
    """Argument Parser

    Parse arguments from command line, and perform error checking

    Returns:
        An argument object which contains arguments from cmd line
    """
    parser = argparse.ArgumentParser(prog='Acrobat train')
    parser.add_argument(
        "--mode",
        dest="mode",
        type=str,
        required=True,
        help="Running Mode: [train, test]"
    )
    
    args = parser.parse_args()

    return args