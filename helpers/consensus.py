def pretty_consensus(up: int, down: int, size=12, denominator=100) -> str:
    """
    Pretty Consensus
    ----------------

    Generates a loading bar for the current consensus of upvotes and downvotes.

    :param up: The amount of upvotes.
    :param down: The amount of downvotes.
    :param size: The size of the loading bar.
    :param denominator: The denominator of the loading bar.
    """

    total_votes = up + down
    percentage = 0 if total_votes == 0 else (up / total_votes) * denominator

    hashes = '█' * int(round((percentage/denominator) * size))
    spaces = '▒' * (size - len(hashes))

    return f"{hashes + spaces} {round(percentage, 2)}% \nTotal votes: {total_votes}"

def percentage_consensus(up: int, down: int, denominator=100) -> int:
    total_votes = up + down
    return 0 if total_votes == 0 else (up / total_votes) * denominator
