# coding=utf-8

#
# Copyright (C) Quranic Arabic Corpus, 2014.
# Rafid K. Abdullah, rafidka@gmail.com (Developer of this file)
# Kais Dukes, sckd@leeds.ac.uk (Original developer of Quranic Arabic Corpus)
#
# This file is part of the Quranic Arabic Corpus.
#
# This is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# the Quranic Arabic Corpus. If not, see <http://www.gnu.org/licenses/>.
#

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

from django.test import TestCase
from phonetic import unicode_to_phonetic


class PhonemEncodingTests(TestCase):
  def test_rafid_khalid(self):
    """
    Tests that 1 + 1 always equals 2.
    """
    rafid_khalid_in_unicode = u'\u0631\u0627\u0641\u062F ' + \
                              u'\u062E\u0627\u0644\u062F'
    rafid_khalid_transcribed = unicode_to_phonetic(rafid_khalid_in_unicode)
    self.assertEqual(rafid_khalid_transcribed, u'rāfd ẖāld')


  def test_tarnscribing_the_name_of_god(self):
    allah_in_unicode = u'\u0671\u0644\u0644\u0651\u064E\u0647\u0650'
    allah_transcribed = unicode_to_phonetic(allah_in_unicode)
    self.assertEqual(allah_transcribed, u'al-lahi')

  def test_transcribing_alrahimi(self):
    alrahimi_in_unicode = \
      u'\u0671\u0644\u0631\u0651\u064E\u062D\u0650\u064A\u0645\u0650'
    alrahimi_transcribed = unicode_to_phonetic(alrahimi_in_unicode)
    self.assertEqual(alrahimi_transcribed, u'al-raḥīmi')

  def test_basmala(self):
    basmala_unicode = \
      u'\u0628\u0650\u0633\u0652\u0645\u0650 ' + \
      u'\u0671\u0644\u0644\u0651\u064E\u0647\u0650 ' + \
      u'\u0671\u0644\u0631\u0651\u064E\u062D\u0652\u0645\u064E\u0670\u0646\u0650 ' + \
      u'\u0671\u0644\u0631\u0651\u064E\u062D\u0650\u064A\u0645\u0650'
    basmala_transcribed = unicode_to_phonetic(basmala_unicode)
    # TODO: Is it possible to make it clear that bismi is actually the letter
    # Ba' followed by an Alif which is not pronounced?
    # TODO: We need to find a way to distinguish between light and bold Lam.
    # TODO: الرحمن should be transcribed as 'ar-raḥmāni'.
    # TODO: الرحيم should be transcribed as 'ar-raḥīmi'.
    self.assertEqual(basmala_transcribed, u'bismi al-lahi al-raḥmāni al-raḥīmi')
