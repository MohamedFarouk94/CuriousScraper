POST = """
<div class="post">
            <div class="username">$$ASKER$$</div>
            <div class="content">$$QUESTION$$</div>
            <div class="reply">
                <div class="username">Me</div>
                <div class="date">$$DATE$$</div>
                <div class="content">
                    $$ANSWER$$
                </div>
            </div>
        </div>
"""

def create_post(d):
	return POST.replace('$$ASKER$$', d['asker'])\
	.replace('$$QUESTION$$', d['question'])\
	.replace('$$DATE$$', d['date'])\
	.replace('$$ANSWER$$', d['answer'].replace('\n', '<br>\n'))


def replace_posts_in_html(posts, file_name):
	with open('tmp.html', 'r', encoding='utf-8') as file:
		content = file.read()

	return content.replace('$$POSTS$$', posts)
