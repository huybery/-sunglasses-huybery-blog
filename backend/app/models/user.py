"""
model for user
"""
from app import blog
from app import db
from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as JWS
from itsdangerous import SignatureExpired
from itsdangerous import BadSignature

class User(db.Document):
    """
    用户 model 层
    """
    username = db.StringField(require=True)
    password = db.StringField(require=True)

    def hash_password(self, password):
        """
        arguments: password
        return: hashed password
        password Hash 函数
        """
        self.password = custom_app_context.encrypt(password)
        return self.password

    def verify_password(self, password):
        """
        arguments: password
        return True / False
        验证密码是否正确
        """
        return custom_app_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        """
        auguments: expireation: token 有效时间
        returen: serialize token
        生成 token
        """
        serializer = JWS(blog.config['SECRET_KEY'], expires_in=expiration)
        return serializer.dumps({'id': str(self.id)})

    @staticmethod
    def verify_auth_token(token):
        serializer = JWS(blog.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            # valid token, but expired
            print('valid token, but expired')
            return None 
        except BadSignature:
            # invalid token
            print('invalid token')
            return None
        user = User.objects(id=data.get('id'))[0]
        return user