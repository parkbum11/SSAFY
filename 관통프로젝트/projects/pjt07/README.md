개발자 : 신민호, 박승범

개발환경 : 가상환경을 쓰지 않음

개발 내용 :

공통 -> 알고리즘 구현

신민호 -> like logic django to script

박승범 -> follow logic django to script

follow 는 어제 workshop에서 나온대로 진행하였습니다. 기존에 있던 django form에 내용을 없애고 script form으로 만들었습니다. 원래는 좋아요를 변경하면 page전체를 reloading 하여 보내주는 방식을 form만 post방식으로 보내는 자바스크립트 방법을 활용하여 구현했습니다.

template

```html
<script>
    const form = document.querySelector('.follow-user')

    form.addEventListener('submit', function (event) {
      event.preventDefault()

      const userId = event.target.dataset.userId
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

      axios.post(`http://127.0.0.1:8000/accounts/follow/${userId}/`, {}, {
        headers : {
          'X-CSRFToken': csrftoken
        }
      })
      .then(function (res) {
        console.log(res)
        const count= res.data.count
        const follow = res.data.follow

        const followButton = document.querySelector(`.follow-${userId}`)
        const followCount = document.querySelector(`#follow-count-${userId}`)

        if (follow) {
          followButton.style.background = '#6c757d'
          followButton.style.borderColor = '#6c757d'
          followButton.innerText = 'Unfollow'
          followCount.innerText = `/ 팔로워 : ${count}`
        } else {
          followButton.style.background = '#007bff'
          followButton.style.borderColor = '#007bff'
          followButton.innerText = 'Follow'
          followCount.innerText = `/ 팔로워 : ${count}`
        }
      })
    })
  </script>
```

view

```python
from django.http import JsonResponse


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                follow = False
            else:
                person.followers.add(user)
                follow = True
            follow_status = {
                'follow' : follow,
                'count' : person.followers.count(),
            }
            return JsonResponse(follow_status)
    return redirect('accounts:profile', person.username)

```

* 변경한 부분만 올렸습니다.

시행착오 : class자체를 바꾸는 방법이 아닌 style을 통해서 unfollow와 follow을 바꾸는 과정에서 css문법이 아니라 색을 지정해줄때 문제가 있어 색의 16진법을 찾아 구현했습니다.



알고리즘 구현은 신민호 교육생가 같이 진행하였습니다.

먼저 fixtures 폴더에 있는 movies.json 을 이미 정의되어 있는 model에 

`python manage.py loaddata movies.json` 을 통해 db에 더미 데이터를 로드 해줬습니다.

이 후는 간단하게 객체로 평점 내림차순으로 12개를 받아 card 형태의 bootstrap으로 꾸며주어 구현하였습니다. 

시간 부족으로 나머지는 건들지 않았습니다.

시행착오 : loaddata를 해주는 instruction을 찾는 것에 약간 시간이 걸렸지만 같이 협업하며 찾았고, 남은 시간에 bootstrap을 해주고 싶었으나 1시간밖에 남지 않아 추천 알고리즘을 보여주는 template만 꾸며 주었습니다.