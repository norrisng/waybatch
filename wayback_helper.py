import queue
import threading
import time
from datetime import datetime

import waybackpy
from waybackpy.exceptions import WaybackError, URLError


def archive_urls(url_list: [], num_threads=4):
    """
    Archives a list of URLs on the Wayback Machine.
    Multithreaded for efficiency.
    :param url_list:    list of URLs to archive
    :param num_threads: number of parallel archive requests. Defaults to 3
    """

    archive_queue = queue.Queue()

    def worker(work_queue):
        while not work_queue.empty():
            a_url = work_queue.get()

            thread_id = threading.get_ident()

            if a_url == '':
                work_queue.task_done()
            else:
                print(f'[#{thread_id}] Processing {a_url}')

                if a_url is None:
                    break
                # elif work_queue.empty():
                #     return

                try:
                    wb = Wayback()
                    start_time = time.time()
                    wb.archive_page(a_url)
                    processing_time = time.time() - start_time
                    print(f'[#{thread_id}] Completed in {round(processing_time, 5)} seconds')
                except URLError as e:
                    print(f'[#{thread_id}] Invalid URL: {a_url}')
                    work_queue.task_done()
                except WaybackError as e:
                    print(f'Error! Stack trace as follows:\n{e}')

                work_queue.task_done()

    for url in url_list:
        archive_queue.put(url)

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(archive_queue, ))
        t.start()
        threads.append(t)

    archive_queue.join()


class Wayback:

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'

    def _wayback_setup(self, url) -> waybackpy.Url:
        """
        Helper function for setting up the waybackpy object.
        :param url: URL to deal with
        :return: waybackpy object
        """
        try:
            return waybackpy.Url(url, self.USER_AGENT)
        except URLError as e:
            raise e

    def is_archived(self, url: str) -> bool:
        """
        Checks if a given URL has been archived.
        Raises waybackpy.exceptions.URLError if the url is incorrectly formatted
        :param url: the URL to check
        :return:    True if it exists, False otherwise
        """
        wayback = self._wayback_setup(url)
        num_archives = wayback.total_archives()
        if num_archives > 0:
            return True
        else:
            return False

    def archive_date(self, url: str) -> datetime:
        wayback = self._wayback_setup(url)
        try:
            return wayback.newest().timestamp
        except WaybackError:
            pass

    def archive_page(self, url: str, no_dup=True):
        """
        Archives a webpage.
        :param url: URL of webpage to archive
        :param no_dup: if True, then don't archive if it already exists
        """
        wayback = self._wayback_setup(url)
        try:
            if no_dup:
                if self.is_archived(url):
                    return
            archive = wayback.save()
        except WaybackError as e:
            raise e

    def get_archive(self, url: str) -> str:
        wayback = self._wayback_setup(url)
        try:
            archive = wayback.newest()
        except URLError:
            return None
        return archive.get()
