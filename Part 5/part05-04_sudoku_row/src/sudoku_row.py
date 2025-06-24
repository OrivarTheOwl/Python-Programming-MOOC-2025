def row_correct(soduko: list, row_no: int):
    number_list = []
    for index in soduko[row_no]:
         if index != 0:
              if index in number_list:
                   return False
              number_list.append(index)
    return True




