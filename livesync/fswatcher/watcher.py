from watchdog.observers import Observer
import os
import logging; log = logging.getLogger(__name__)


class FileWatcher(object):
    def __init__(self):
        self.handlers = set()
        self.observer = Observer()

    def _schedule_all(self):
        for handler in self.handlers:
            for path in handler.watched_paths:
                path = os.path.abspath(path)
                if not os.path.exists(path):
                    log.warn("Not adding path {}".format(path))
                    continue
                self.observer.schedule(handler, path, recursive=True)

    def add_handler(self, handler):
        self.handlers.add(handler)

    def start(self):
        self._schedule_all()
        self.observer.start()

    def stop(self):
        self.observer.stop()
