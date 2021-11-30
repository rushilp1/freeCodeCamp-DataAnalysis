import numpy as np

def calculate(list):
  # If a list containing less than 9 elements is passed into the function,
  #   raise a 'ValueError' exception with the message:
  #     "List must contain nine numbers."
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  # Create Row and Column axes variables for better readability
  RowAxis = 1
  ColumnAxis = 0
  # Reshape the provided list into a 3x3 matrix
  matrix = np.reshape(list, (3,3))
  # Calculate 'mean' using NumPY functions (for each axis) and 
  #   convert each result into a list
  mean = [
    np.mean(matrix, axis=ColumnAxis).tolist() ,
    np.mean(matrix, axis=RowAxis).tolist()    ,
    np.mean(matrix, axis=None).tolist()
  ]
  # Calculate 'variance' using NumPY functions (for each axis) and 
  #   convert each result into a list
  variance = [
    np.var(matrix, axis=ColumnAxis).tolist()  ,
    np.var(matrix, axis=RowAxis).tolist()     ,
    np.var(matrix, axis=None).tolist()
  ]
  # Calculate 'standard deviation' using NumPY functions (for each axis) and 
  #   convert each result into a list
  standard_deviation = [
    np.std(matrix, axis=ColumnAxis).tolist()  ,
    np.std(matrix, axis=RowAxis).tolist()     ,
    np.std(matrix, axis=None).tolist()
  ]
  # Calculate 'maximum' using NumPY functions (for each axis) and 
  #   convert each result into a list
  maximum = [
    np.max(matrix, axis=ColumnAxis).tolist()  ,
    np.max(matrix, axis=RowAxis).tolist()     ,
    np.max(matrix, axis=None).tolist()
  ]
  # Calculate 'minimum' using NumPY functions (for each axis) and 
  #   convert each result into a list
  minimum = [
    np.min(matrix, axis=ColumnAxis).tolist()  ,
    np.min(matrix, axis=RowAxis).tolist()     ,
    np.min(matrix, axis=None).tolist()
  ]
  # Calculate 'summation' using NumPY functions (for each axis) and 
  #   convert each result into a list
  summation = [
    np.sum(matrix, axis=ColumnAxis).tolist()  ,
    np.sum(matrix, axis=RowAxis).tolist()     ,
    np.sum(matrix, axis=None).tolist()
  ]
  # Arrange all the calculations into a dictionary as instructed
  calculations = {
    'mean'              : mean                ,
    'variance'          : variance            ,
    'standard deviation': standard_deviation  ,
    'max'               : maximum             ,
    'min'               : minimum             ,
    'sum'               : summation
  }
  # Return the Calculations performed
  return calculations