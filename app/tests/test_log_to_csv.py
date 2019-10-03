import pytest
import time
import os
from app.log_to_csv import export_data


class TestLogToCSV():

    def test_input_file_exists(self):
        with pytest.raises(Exception):
            export_data('non_existingfolder')

    def _find_test_in_file(self, file, text):
        with open(file, mode='r+') as f:
            for line in f.readlines():
                if text in line:
                    return True
        return False

    def test_file_created(self):
        filename = '/tmp/access-{}.log'.format(time.time())
        content = '207.114.153.6 - - [10/Jun/2015:18:14:56 +0000] "GET /favicon.ico HTTP/1.1"' \
                  ' 200 0 "http://www.gobankingrates.com/banking/find-cds-now/" "Mozilla/5.0 (Windows NT 6.1; WOW64) ' \
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"'
        with open(filename, 'a') as f:
            f.write(content)
        output_file = "{}.csv".format(filename)
        export_data(filename, output_file)
        assert os.path.isfile(output_file)
        assert self._find_test_in_file(output_file, '207.114.153.6')
        assert self._find_test_in_file(output_file, 'US,CA,Desktop,Chrome')
        os.remove(output_file)
        os.remove(filename)


if __name__ == '__main__':
    pytest.main()
