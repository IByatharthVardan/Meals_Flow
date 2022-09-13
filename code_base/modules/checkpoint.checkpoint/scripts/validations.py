import logging
from typing import Any, Dict, List, Text, Tuple

ValidationTuple = Tuple[bool, Text]


def always_fail(**kwargs: Any) -> ValidationTuple:
  return False, 'Always fail'


def always_pass(**kwargs: Any) -> ValidationTuple:
  return True, None


def validate_total(total: Text, **kwargs: Any) -> ValidationTuple:
  if (str(total) == '17.01'):
    logging.info('Total is 17.01 - custom fail!!')
    return False, 'Total is 17.01 - custom fail!!'
  return True, None


def validate_dict_keypath(dict_field: Dict,
                          **kwargs: Any) -> Dict[Text, ValidationTuple]:
  return {
      'dict_field.key1.nestedkey':
      (False, 'Field dict_field had a failure at keypath key1.nestedkey')
  }


def validate_list_index(list_field: List,
                        **kwargs: Any) -> Dict[Text, ValidationTuple]:
  return {'list_field.3': (False, 'Field list_field had a failure at index 3')}


def validate_table_cell(table_field: List,
                        **kwargs: Any) -> Dict[Text, ValidationTuple]:
  return {
      'table_field.0.3_3.9_9':
      (False,
       'Field table_field had a failure for table index 0, row range [3,3], col range [9,9]'
       )
  }


def register() -> Dict[Text, Any]:
  return {
      'always_fail': {
          'fn': always_fail
      },
      'always_pass': {
          'fn': always_pass
      },
      'validate_total': {
          'fn': validate_total
      },
      'validate_dict_keypath': {
          'fn': validate_dict_keypath
      },
      'validate_list_index': {
          'fn': validate_list_index
      },
      'validate_table_cell': {
          'fn': validate_table_cell
      }
  }
