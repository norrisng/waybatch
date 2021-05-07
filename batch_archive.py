from argparse import ArgumentParser
import wayback_helper


def batch_archive():

    # Parse a given text file
    parser = ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        raw_url_list = f.read()

    urls = raw_url_list.split('\n')
    urls = [line for line in urls if line != '']   # strip empty lines

    num_threads = 4

    print(f'Archiving {len(urls)} URLs with {num_threads} threads...')
    wayback_helper.archive_urls(urls, num_threads=num_threads)
