

import os
import sys
import json
import unittest

# import cpuinfo.py which is in parent directory
sys.path.append('..')
import cpuinfo


class CPUInfoProcCpuinfoTester(cpuinfo.CPUInfoProcCpuinfo):
	def __init__(self, file_name):
		self.file_name = file_name

	def _get_data(self):
		with open(self.file_name, 'r') as f:
			data = json.load(f)

		data['proc_cpu_info'] = '\n'.join(data['proc_cpu_info'])
		return data


class TestProcCpuInfo(unittest.TestCase):
	def setUp(self):
		pass

	def test_x86_64(self):
		info_getter = CPUInfoProcCpuinfoTester('proc_cpuinfo_x86_64.json')
		info = info_getter.get_fields()

		self.assertEqual(info['vendor_id'], 'GenuineIntel')
		self.assertEqual(info['brand'], 'Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz')

		self.assertEqual(info['hz_advertised'], '1.9000 GHz')
		self.assertEqual(info['hz_actual'], '2.3756 GHz')
		self.assertEqual(info['hz_advertised_raw'], (1900000000, 0))
		self.assertEqual(info['hz_actual_raw'], (2375627000, 0))

		self.assertEqual(info['arch'], 'X86_64')
		self.assertEqual(info['bits'], 64)
		self.assertEqual(info['count'], 4)
		self.assertEqual(info['raw_arch_string'], 'AMD64')

		self.assertEqual(info['l2_cache_size'], '6144 KB')
		self.assertEqual(info['l2_cache_line_size'], 0)
		self.assertEqual(info['l2_cache_associativity'], 0)

		self.assertEqual(info['stepping'], 1)
		self.assertEqual(info['model'], 69)
		self.assertEqual(info['family'], 6)
		self.assertEqual(info['processor_type'], 0)
		self.assertEqual(info['extended_model'], 0)
		self.assertEqual(info['extended_family'], 0)
		self.assertEqual(info['flags'], ['apic', 'clflush', 'cmov', 'constant_tsc', 'cx8', 'de', 'fpu', 'fxsr', 'lahf_lm', 'lm', 'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nopl', 'nx', 'pae', 'pat', 'pge', 'pni', 'pse', 'pse36', 'rdtscp', 'rep_good', 'sep', 'sse', 'sse2', 'ssse3', 'syscall', 'tsc', 'vme'])

	def test_arm(self):
		info_getter = CPUInfoProcCpuinfoTester('proc_cpuinfo_arm.json')
		info = info_getter.get_fields()

		self.assertEqual(info['vendor_id'], 'ARM')
		self.assertEqual(info['brand'], 'ARMv6-compatible processor rev 7 (v6l)')

		self.assertEqual(info['hz_advertised'], '1.9000 GHz')
		self.assertEqual(info['hz_actual'], '2.3756 GHz')
		self.assertEqual(info['hz_advertised_raw'], (1900000000, 0))
		self.assertEqual(info['hz_actual_raw'], (2375627000, 0))

		self.assertEqual(info['arch'], 'ARM_6')
		self.assertEqual(info['bits'], 32)
		self.assertEqual(info['count'], 4)
		self.assertEqual(info['raw_arch_string'], 'armv6-a')

		self.assertEqual(info['l2_cache_size'], 0)
		self.assertEqual(info['l2_cache_line_size'], 0)
		self.assertEqual(info['l2_cache_associativity'], 0)

		self.assertEqual(info['stepping'], 0)
		self.assertEqual(info['model'], 0)
		self.assertEqual(info['family'], 0)
		self.assertEqual(info['processor_type'], 0)
		self.assertEqual(info['extended_model'], 0)
		self.assertEqual(info['extended_family'], 0)
		self.assertEqual(info['flags'], ['edsp', 'fastmult', 'half', 'java', 'swp', 'thumb', 'tls', 'vfp'])


if __name__ == '__main__':
	unittest.main()

