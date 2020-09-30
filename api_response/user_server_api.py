from django.contrib.auth import get_user_model
from django.core import serializers
from .api_app_settings import USER_RELATED_MODELS
import json

User = get_user_model()


class GetUser:

    def __init__(self):
        pass

    def get_user(self, p_key, keytype='username'):

        if p_key:
            if keytype == 'username':
                user = User.objects.filter(username=p_key)
            elif keytype == 'id':
                user = User.objects.filter(id=p_key)
            else:
                return 'Not a valid key type'
            # ----------------------------------------------
            if user:
                user = user[0]
                user_info = self.__getFullUserDetails(user)
                user_info.update(UserRelatedModelComputation(user).compute_models())
                return user_info
            else:
                return False
        else:
            return False

    def __getFullUserDetails(self, user_model):
        raw_data = serializers.serialize('json', [user_model, ])
        response = json.loads(raw_data)
        data = response[0]['fields']

        for i in ['password', 'is_superuser']:
            del data[i]
        return data


class UserRelatedModelComputation:
    """Compute response for user related models"""

    def __init__(self, user_model):
        self.URM = USER_RELATED_MODELS
        self.user = user_model

    def compute_models(self):
        q_set = {}

        if self.URM:
            for model in self.URM:
                model = model.lower()
                try:
                    # print(model)
                    q_set[model] = getattr(self.user, f'{model}_set').all()
                except AttributeError:
                    try:
                        q_set[model] = getattr(self.user, model)
                    except:
                        pass

        return self.compute_queries(q_set)

    def compute_queries(self, q_set):
        _data = {}

        if q_set:
            # print(q_set)
            for name, query in q_set.items():
                query_data_holder = []
                try:
                    for each_query in query:
                        temp_dic = {}
                        raw_data = serializers.serialize('json', [each_query])
                        response = json.loads(raw_data)[0]
                        temp_dic['id'] = response['pk']
                        temp_dic.update(response['fields'])
                        query_data_holder.append(temp_dic)
                        _data[name] = query_data_holder
                except TypeError:
                    raw_data = serializers.serialize('json', [query])
                    response = json.loads(raw_data)[0]['fields']
                    _data[name] = response

        return _data
