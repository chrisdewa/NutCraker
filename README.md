# NutCraker
A small MD5 bruteforcer

## Features:
- Customizable password length and characters
- Cli commands

## Planned features (in no order):
- Multiprocessing
- Release on pypi
- Silent mode (skip showing progress)

## How to use:
### As a Module:
```python
from nutcraker import MD5Craker
test = 'chris'
test_hash = MD5Craker.md5(test)
pwd = MD5Craker(test_hash).attack()
print('Password:', pwd or 'Not Found')
```

### From cli:
```
python -m nutcraker 6b34fe24ac2ff8103f6fce1f0da2ef57
```

# Notes:
This project was made just for fun.
Use it at your own risk.
From the licence:
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
