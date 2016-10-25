import mock
import unittest
import sys
import os
import itertools

sys.path.insert(0, 'C:\Users\LukaszP\Documents\Repos\WiFi_perf')

from analyzelog import AnalyzeLog as AL
from analyzelog import EH


class TestAnalyzeLog(unittest.TestCase):
    def setUp(self):
        
        self.file_full = 'output_full.txt'
        self.file_output = 'output.txt'
        self.input_filename = 'input.txt'
        self.thread_id = 'test_thread_id'

        self.durat_time = '5'

        self.logmock = mock.MagicMock(name='analyzelog', spec=AL)
        self.ehmock = mock.MagicMock(name='errorhandler', type=EH)
        
    def tearDown(self):
        if os.path.isfile(self.file_full):
            os.remove(self.file_full)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)

        self.logmock.reset_mock()

    @mock.patch('analyzelog.EH')
    @mock.patch('analyzelog.open')
    def test_getalldata(self, mock_open, mock_eh):
        mock_eh.return_value = True
        filling_input_file(self.input_filename)
        self.logmock.FILE_FULL = self.file_full
        result = AL.get_all_data(self.logmock, self.input_filename,
                                         self.thread_id)
        self.assertTrue(result)
        
        mock_open.side_effect = IOError
        result = AL.get_all_data(self.logmock, self.input_filename,
                                         self.thread_id)
        self.assertFalse(result)

        mock_open.reset_mock()
        mock_open.side_effect = Exception('Exception')
        result = AL.get_all_data(self.logmock, self.input_filename,
                                         self.thread_id)
        self.assertFalse(result)
        mock_open.reset_mock()

    @mock.patch('analyzelog.Iperf')
    @mock.patch('analyzelog.EH')
    def test_getmeanvalue(self, mock_eh, mock_iperf):
        mock_iperf.DURATION_TIME = self.durat_time
        mock_eh.return_value = True
        udp_test_row = 'test_row'
        notf_row = 'notfoundrow'
        dur_time = int(self.durat_time)
        dur_time_minus = (dur_time - 1)
        patterns = ['Server Report',
                    '0.0-%s' % dur_time,
                    '0.0- %s' % dur_time_minus,
                    '0.0- %s' % dur_time,
                    '0.0-%s' % dur_time_minus]

        # ///test patterns[1] pass///
        self.logmock.reg_exp_analyze.return_value = 'OK'
        self.logmock.FILE_OUTPUT = self.file_output

        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[1])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)

        self.assertTrue(patterns[1] in str(self.logmock.mock_calls))
        self.assertTrue(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test patterns[2] pass///
        self.logmock.reg_exp_analyze.return_value = 'OK'
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[2])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertTrue(patterns[2] in str(self.logmock.mock_calls))
        self.assertTrue(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test patterns[3] pass///
        self.logmock.reg_exp_analyze.return_value = 'OK'
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[3])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertTrue(patterns[3] in str(self.logmock.mock_calls))
        self.assertTrue(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test patterns[4] pass///
        self.logmock.reg_exp_analyze.return_value = 'OK'
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[4])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertTrue(patterns[4] in str(self.logmock.mock_calls))
        self.assertTrue(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test patterns[0] (udp) pass///
        self.logmock.reg_exp_analyze.return_value = 'OK'
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[0] +'\n')
            input_file.write(udp_test_row)
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertTrue(udp_test_row in str(self.logmock.mock_calls))
        self.assertTrue(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test endflag = False///
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(notf_row)
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertFalse(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test result = 'Not Found!'///
        self.logmock.reg_exp_analyze.return_value = 'Not Found!'
        self.logmock.FILE_OUTPUT = self.file_output
        self.logmock.DURATION_TIME = self.durat_time
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[4])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertTrue(patterns[4] in str(self.logmock.mock_calls))
        self.assertFalse(result)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test Exception///
        self.logmock.reg_exp_analyze.side_effect = Exception
        self.logmock.FILE_OUTPUT = self.file_output
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[1])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertFalse(result)
        self.assertTrue(self.logmock.mock_calls)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

        # ///test IOError///
        self.logmock.reg_exp_analyze.side_effect = IOError
        self.logmock.FILE_OUTPUT = self.file_output
        
        with open(self.input_filename, 'a') as input_file:
            input_file.write(patterns[1])
        
        result = AL.get_mean_value(self.logmock, self.input_filename,
                                   self.thread_id)
        self.assertFalse(result)
        self.assertTrue(self.logmock.mock_calls)
        if os.path.isfile(self.file_output):
            os.remove(self.file_output)
        if os.path.isfile(self.input_filename):
            os.remove(self.input_filename)
        self.logmock.reset_mock()

    def test_regexpanalyze(self):
        filling_input_file(self.input_filename)
        exp_vals = []
        with open(self.input_filename, 'r') as origf:
            for row in origf:
                exp_vals.append(row.strip())
                
        with open(self.input_filename, 'r') as origf:
            i = 0
            for row in origf:
                result = AL.reg_exp_analyze(self.logmock, row)
                self.assertEqual(result, exp_vals[i])
                i += 1


def filling_input_file(filename):
    with open(filename, 'a') as input_file:
        bandw_units = ['Mbits/sec', 'kbits/sec', 'bits/sec']
        bandw_val = ['1', '10', '100', '1000', '10000', '100000']
        notfound_val = 'Not Found!'
        cart_val = itertools.product(bandw_val, bandw_val)
        input_list = []
        
        for i in cart_val:
            input_list.append(i[0] +'.' +i[1] +' ')
        cart_val = itertools.product(input_list, bandw_units)
        
        for i in cart_val:
            input_file.write(i[0] +i[1] +'\n')
        
        input_file.write(notfound_val +'\n')
            
            
if __name__ == '__main__':
    unittest.main()
