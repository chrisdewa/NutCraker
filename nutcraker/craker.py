"""
Real password bruteforce cracker for unsalted MD5 hashes

Author: ChrisDewa
Version: v1.0.0
This is only a proof of concept for educational purposes.

MIT License

Copyright (c) 2021 ChrisDewa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from hashlib import md5
from string import ascii_lowercase as abc
from typing import Optional
from multiprocessing import Pool
from tqdm.contrib.itertools import product as prod

__all__ = (
    'MD5Craker',
)

class MD5Craker:
    """
    This class bruteforces MD5 passwords as long as they are shorter than max_len
    Args:
        target (str): the unsalted, plain, md5 hash 
            example: "330ec1cce37e83b5ccd8ce6587de2580" (equals to "pswrd")
        max_len (int): maximum number of characters (defaults to 5)
        chars (str): characters to include in cracking defaults to 
            'abcdefghijklmnopqrstuvwxyz'.
    """
    def __init__(self, target: str, max_len = 5, chars: str = abc):
        self._target = target
        self._limit = max_len+1
        self._chars = chars
    
    def _compare(self, test: list) -> Optional[str]:
        """compares the hash of a joined list of characters with the target"""
        t = ''.join(test)
        if md5(t.encode()).hexdigest() == self._target:
            return t
    
    def attack(self) -> Optional[str]:
        """
        Returns the plain text password for the hash if 
        it's within the max_len limit of the instance.
        """
        for n in range(1,self._limit):
            print(f'[*] Testing passwords with length: {n}')
            for pwd in map(self._compare, 
                         prod(*[self._chars for _ in range(n)])):
                if pwd:
                    break
            if pwd:
                break
        return pwd

    @staticmethod
    def md5(string: str) -> str:
        """
        Returns the md5 hash of a given string
        Useful for testing the class
        """
        return md5(string.encode()).hexdigest()
