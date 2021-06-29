def format_thousands(n: int) -> str:
    """Format Numbers"""
    return f"{n:,}"


if __name__ == "__main__":
    print(format_thousands(10000000))
