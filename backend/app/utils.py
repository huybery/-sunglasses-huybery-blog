from flask import url_for

def make_public_post(post):
	"""
	不直接返回任务的 ids，我们直接返回 URI
	"""
	new_post = {}
	for field in post:
		if field == 'id':
            # _external 表示是否添加 localhost
			# new_post['uri'] = url_for('post', id=post.get('id'), _external=True)
			new_post['uri'] = url_for('post', id=post.get('id'))            
		else:
			new_post[field] = post[field]
	return new_post	