from graphene.test import Client
from core.utils import get_global_id
from lisci.schema import schema
from core.models import Course, LearningActivity, UserData
from django.test import TestCase
from django.contrib.auth.models import User


class GraphqlTest(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.course = Course.objects.create(name='Test Course')
        self.learning_activity = LearningActivity.objects.create(name='Test Activity', course=self.course)
        self.user_data = UserData.objects.create(
            user=self.user,
            learning_activity=self.learning_activity,
            data='Some test data',
            status='In progress'
        )
        self.queries_dict = {
            "user":
                'query{user(id:"%s"){username}}' % get_global_id(User, self.user.id),
            "user_data":
                'query{user_data(id:"%s"){data}}' % get_global_id(UserData, self.user_data.id),
            "learning_activity":
                'query{learning_activity(id:"%s"){name}}' % get_global_id(LearningActivity, self.learning_activity.id),
            "course":
                'query{course(id:"%s"){name}}' % get_global_id(Course, self.course.id),
        }

    def test_queries(self):
        expected_results = {
            "user": {"username": "testuser"},
            "user_data": {"data": "Some test data"},
            "learning_activity": {"name": "Test Activity"},
            "course": {"name": "Test Course"},
        }
        for model_name, query in self.queries_dict.items():
            executed = self.client.execute(query)
            self.assertIsNone(executed.get('errors'))
            self.assertEqual(expected_results[model_name], executed['data'][model_name])

    def test_user_mutations(self):
        user_id = self.user.id

        test_queries = {
            "create_user_type": {
                "query": 'mutation{create_user_type(username:"jan"){obj{username}}}',
                "expected_results": {"obj": {"username": "jan"}}
            },
            "update_user_type": {
                "query": 'mutation{update_user_type(id: %s username:"peter"){obj{username}}}' % user_id,
                "expected_results": {"obj":{"username": "peter"}}
            },
            "delete_user_type": {
                "query": 'mutation{delete_user_type(id: %s){ok}}' % user_id,
                "expected_results": {"ok": True}
            }
        }
        self.run_test_mutation(test_queries)

    def test_user_data_mutations(self):
        user_id = self.user.id
        user_data_id = self.user_data.id

        test_queries = {
            "create_user_data_type": {
                "query": 'mutation{create_user_data_type(data: "test" user_id: %s){obj{data}}}' % user_id,
                "expected_results": {"obj": {"data": "test"}}
            },
            "update_user_data_type": {
                "query": 'mutation{update_user_data_type(id: %s data:"new test"){obj{data}}}' % user_data_id,
                "expected_results": {"obj": {"data": "new test"}}
            },
            "delete_user_data_type": {
                "query": 'mutation{delete_user_data_type(id: %s){ok}}' % user_data_id,
                "expected_results": {"ok": True}
            }
        }
        self.run_test_mutation(test_queries)

    def test_learning_activity_mutations(self):
        activity_id = self.learning_activity.id
        course_id = self.course.id

        test_queries = {
            "create_learning_activity_type": {
                "query": 'mutation{create_learning_activity_type(name:"test"course_id:%d){obj{name}}}' % course_id,
                "expected_results": {"obj": {"name": "test"}}
            },
            "update_learning_activity_type":  {
                "query": 'mutation{update_learning_activity_type(id: %s name:"new test"){obj{name}}}' % activity_id,
                "expected_results": {"obj": {"name": "new test"}}
            },
            "delete_learning_activity_type": {
                "query": 'mutation{delete_learning_activity_type(id: %s){ok}}' % activity_id,
                "expected_results": {"ok": True}
            },
        }
        self.run_test_mutation(test_queries)

    def test_course_mutations(self):
        course_id = self.course.id

        test_queries = {
            "create_course_type": {
                "query": 'mutation{create_course_type(name:"test_name"){obj{name}}}',
                "expected_results": {"obj": {"name": "test_name"}}
            },
            "update_course_type": {
                "query": 'mutation{update_course_type(id: %s name:"test_name_new"){obj{name}}}' % course_id,
                "expected_results": {"obj": {"name": "test_name_new"}}
            },
            "delete_course_type": {
                "query": 'mutation{delete_course_type(id: %s){ok}}' % course_id,
                "expected_results": {"ok": True}
            },
        }
        self.run_test_mutation(test_queries)

    def run_test_mutation(self, test_queries):
        for action, query in test_queries.items():
            executed = self.client.execute(query["query"])
            self.assertIsNone(executed.get('errors'))
            self.assertEqual(query["expected_results"], executed['data'][action])
