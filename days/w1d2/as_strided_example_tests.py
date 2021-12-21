from collections import namedtuple

test_input_a = torch.tensor([[ 0,  1,  2,  3,  4],
                             [ 5,  6,  7,  8,  9],
                             [10, 11, 12, 13, 14],
                             [15, 16, 17, 18, 19]])

TestCase = namedtuple('TestCase', ['output', 'size', 'stride'])

test_cases = [
  TestCase(
    output=torch.tensor([0, 1, 2, 3]),
    size=(1,),
    stride=(1,),
  ),
  TestCase(
    output=torch.tensor([[0, 1, 2],
                         [5, 6, 7]]),
    size=(1,),
    stride=(1,),
  ),
  TestCase(
    output=torch.tensor([[0, 0, 0],
                         [11, 11, 11]]),
    size=(1,),
    stride=(1,),
  ),
  TestCase(
    output=torch.tensor([0, 6, 12, 18]),
    size=(1,),
    stride=(1,),
  ),
  TestCase(
    output=torch.tensor([[[0, 1, 2],
                          [9, 10, 11]]]),
    size=(1,),
    stride=(1,),
  ),
  TestCase(
    output=torch.tensor([[[[0, 1],
                           [2, 3]],
                          [[4, 5],
                           [6, 7]]],
                         [[[12, 13],
                           [14, 15]],
                          [[16, 17],
                           [18, 19]]]]),
    size=(1,),
    stride=(1,),
  ),
]

def is_equal_test(*, output, expected, test_name='Test'):
  successful = torch.allclose(expected.to(float), output.to(float))
  if successful:
    print(f'{test_name} passed!')
  else:
    print(f'{test_name} failed')
    print(f'Output:\n{output}')
    print(f'Expected:\n{expected}')

if __name__ == '__main__':
    for i, (expected, size, stride) in enumerate(test_cases):
      output = torch.as_strided(test_input_a, size=size, stride=stride)
      is_equal_test(test_name=i, output=output, expected=expected)
