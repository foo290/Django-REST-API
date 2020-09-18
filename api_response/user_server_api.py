from django.contrib.auth.models import User

class GetUser:

    MERGE_PROFILE_INFO = False
    PROFILE_MODEL = None

    def __init__(self):
        pass
    
    def get_user(self, p_key, keytype = 'username'):
        
        if p_key:
            if keytype == 'username':
                user = User.objects.filter(username = p_key)
            elif keytype == 'id':
                user = User.objects.filter(id = p_key)
            else:
                return 'Not a vaid keytype'
            
            # ----------------------------------------------
            # Get user Ops:

            if user:
                user = user[0]
                if not self.MERGE_PROFILE_INFO:
                    # only return FULL user info excluding profile 
                    return self.__getFullUserDetails(user)
                else:
                    if self.PROFILE_MODEL:
                        if type(self.PROFILE_MODEL) == type(''):
                            _profileModel = self.PROFILE_MODEL.lower()
                        else:
                            _profileModel = self.PROFILE_MODEL.__name__.lower()
                        
                        user_info = self.__getFullUserDetails(user)
                        profile_info = self.__getUserMergeProfileDetails(user, _profileModel)
                        user_info.update(profile_info)
                        return user_info
                    else:
                        raise Exception(
                    'Profile information requested without specifying profile model. Please specify profile model in settings.py as : PROFILE_MODEL = your model'
                    )
            else:
                return False
        else:
                return False
        

    def __getFullUserDetails(self, userModel):
        _user_fields = [field.name for field in userModel._meta.fields]
        print(_user_fields)
        for i in ['password', 'is_staff', 'is_superuser']:
            _user_fields.remove(i)

        _vals = [getattr(userModel, attr) for attr in _user_fields]

        keys = _user_fields
        data = {k:v for k,v in zip(keys, _vals)}
        return data
    
    def __getUserMergeProfileDetails(self, userModel, profileModel):
        _profile_fields = [field.name for field in getattr(userModel, profileModel)._meta.fields]
        print(_profile_fields)
        _profile_fields.remove('user')

        _vals = [
            getattr(getattr(getattr(userModel, profileModel), attr), "url") if
             getattr(userModel, profileModel)._meta.get_field(attr).get_internal_type() == 'FileField' else
             getattr(getattr(userModel, profileModel),attr) for 
             attr in _profile_fields
        ]

        keys = _profile_fields
        data = {k:v for k,v in zip(keys, _vals)}
        return data


    
        












