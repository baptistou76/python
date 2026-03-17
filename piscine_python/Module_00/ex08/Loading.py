def ft_tqdm(lst):
    """
    Reproduce the behavior of tqdm function.
    It will generate a laoding bar and show the percentage completed.
    """
    total = len(lst)
    bar_len = 50
    for i, elem in enumerate(lst, 1):
        percent = i / total
        filled_len = int(bar_len * percent)
        bar = '=' * filled_len + '>' + ' ' * (bar_len - filled_len)
        print(f"\r{int(percent*100)}%|[{bar}]| {i}/{total}",
              end='', flush=True)
        yield elem
    print()
