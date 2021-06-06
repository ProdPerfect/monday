from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import get_complexity_query


class ComplexityTestCase(BaseTestCase):
    def setUp(self):
        super(ComplexityTestCase, self).setUp()

    def test_get_complexity_query(self):
        query = get_complexity_query()
        self.assertEqual('''
        query
        {
            complexity {
                after,
                reset_in_x_seconds
            }
        }'''.replace(" ", ""), query.replace(" ", ""))
